import serial
import numpy as np
import time
from csv import writer

from preprocessor import *
import cv2
import tensorflow as tf
from data_collector import *
from tkinter import *
from data_sender import *
import random as rnd
import winsound

ws = Tk()
ws.title('Directional Recognition')
ws.geometry('1000x0750')
ws.config(bg='#000000')

mylabel = Label(ws,
                text="...",
                bg='#000000',
                fg='#ffffff',
                font='Times 100',
                width=50,
                height=10)

mylabel.pack()
ws.update()

countDown = 100
test = True

#COMPort = input("Please enter the COM port: ")
model = tf.keras.models.load_model("DirectionRecCNN")

FileAdd = []

# FirstCounter = True
# line = arduino.readline()
# if FirstCounter:
#     for i in range(8000):
#         line = arduino.readline()
#         print(line)
#     FirstCounter = False
COMPortMotor = "COM5"
currAng, MotorController = Inititialise(COMPortMotor)
time.sleep(1)
ws.update()
labels = os.listdir("Figure/Training")
labelsInt = []
for i in labels:
    labelsInt.append(int(i))
labelsInt.sort()
labelsOrd = []
for i in labelsInt:
    labelsOrd.append(str(i))
Increment = labelsInt[1]-labelsInt[0]
COMPort = 'COM6'
#arduino = serial.Serial(COMPort, 2000000, timeout=1)
while test:
    div = rnd.randint(0, 12)
    angle = div * Increment

    currAng = AngleSet(angle, MotorController, currAng)
    Name = str(currAng)
    time.sleep(3)
    Period = 3
    [Channel1, Channel2, Channel3, Channel4, Time] = collectDataTest(COMPort, Period)
    plt.show()
    plt.plot(Time, Channel1)
    plt.plot(Time, Channel2)
    plt.plot(Time, Channel3)
    plt.plot(Time, Channel4)
    plt.show()
    df = pd.read_csv("Temp/Test.csv")
    data = df.to_numpy()
    figure_makerTesting(data)
    PnGFile = "Temp/Test.png"
    while not os.path.isfile(PnGFile):
        [Channel1, Channel2, Channel3, Channel4, Time] = collectDataTest(COMPort, Period)
        plt.plot(Time, Channel1)
        plt.plot(Time, Channel2)
        plt.plot(Time, Channel3)
        plt.plot(Time, Channel4)
        plt.show()
        df = pd.read_csv("Temp/Test.csv")
        data = df.to_numpy()
        figure_makerTesting(data)
    # plt.plot(Time, Voltage)
    # plt.show()
    # TestingPreprocessing(Voltage, Time)
    img_size = 64

    def Preprocess(path):
        img_arr = cv2.imread(path)[..., ::-1]
        resized_arr = cv2.resize(img_arr, (img_size, img_size))
        norm_arr = np.array(resized_arr) / 255
        return norm_arr.reshape(-1, img_size, img_size, 3)


    predict = model.predict([Preprocess("Temp/Test.png")])
    print(predict)
    predictVal = np.argmax(predict)
    os.remove("Temp/Test.png")
    os.remove("Temp/Test.csv")
    text = labelsOrd[predictVal]
    preVal = labelsOrd[predictVal]
    Soundplay = True

    if countDown == 0:
        Test = False

    mylabel.config(text=text)

    FileAdd = [currAng, preVal]
    with open("Tracking/BlindTest.csv", 'a+', newline='') as f_object:
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(FileAdd)
        # Close the file object
        f_object.close()
        FileAdd =[]
    mylabel.pack()
    ws.update()
    if currAng <180:
        angle = 360
    elif currAng ==180:
        angle = 170
        currAng = AngleSet(angle, MotorController, currAng)
        angle = 360
    else:
        angle = -360
    currAng = AngleSet(angle, MotorController, currAng)
    time.sleep(5)
    mylabel.config(text='...')
    mylabel.pack()
    ws.update()
