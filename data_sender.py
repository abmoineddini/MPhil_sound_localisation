import serial
import time
# arduino = serial.Serial('COM3', 9600, timeout=1)


# while True:
#     line = arduino.readline()
#     print(line)
#     try:
#         string = line.decode()
#     except:
#         print("ignored")
#     else:
#         numS = string.replace("\r\n", '')
#         ArCon = True
#         if numS == "ready":
#             arduino.write(b"rdy")
#
#             while line!="Starting":
#                 line = arduino.readline()
#                 line = line.decode()
#                 line = line.replace("\r\n", '')
#
#             print("Starting")
#             currAng = 0
#             while True:
#                 angle = input("Enter an Angle: ")
#                 angle = str(angle)
#                 arduino.write(angle.encode())
#                 line = arduino.readline()
#                 line = line.decode()
#                 line = line.replace("\r\n", '')
#                 while line!="done":
#                     line = arduino.readline()
#                     print(line)
#                     line = line.decode()
#                     line = line.replace("\r\n", '')
#
#                 while not line.isdigit():
#                     line = arduino.readline()
#                     print(line)
#                     line = line.decode()
#                     line = line.replace("\r\n", '')
#                 currAng = int(line)
#                 print("Speaker is at ", currAng, " Degrees now")
#             print("All Done!")
#


def Inititialise(comPort):
    arduino = serial.Serial(comPort, 9600, timeout=1)
    line = arduino.readline()
    print(line)
    try:
        string = line.decode()
    except:
        print("ignored")
    else:
        numS = string.replace("\r\n", '')

        while numS != "ready":
            line = arduino.readline()
            line = line.decode()
            numS = line.replace("\r\n", '')
        while line != "Starting":
            arduino.write(b"rdy")
            line = arduino.readline()
            line = line.decode()
            line = line.replace("\r\n", '')

        print("Starting")

    return 0, arduino

def AngleSet(Angle, arduino, currAngle):
    angle = Angle
    if angle==0:
        if currAngle>180:
            angle = 360
        else:
            angle = -360
    angle = str(angle)
    arduino.write(angle.encode())
    line = arduino.readline()
    line = line.decode()
    line = line.replace("\r\n", '')
    while line!="done":
        line = arduino.readline()
        print(line)
        line = line.decode()
        line = line.replace("\r\n", '')

    while not line.isdigit():
        line = arduino.readline()
        print(line)
        line = line.decode()
        line = line.replace("\r\n", '')
    currAng = int(line)
    print("Speaker is at ", currAng, " Degrees now")
    return currAng


def Calibrate(comPort, arduino):
    arduino.close()
    arduino = serial.Serial(comPort, 9600, timeout=1)
    line = arduino.readline()
    print(line)
    try:
        string = line.decode()
    except:
        print("ignored")
    else:
        numS = string.replace("\r\n", '')

        while numS != "ready":
            line = arduino.readline()
            line = line.decode()
            numS = line.replace("\r\n", '')
        while line != "Starting":
            arduino.write(b"rdy")
            line = arduino.readline()
            line = line.decode()
            line = line.replace("\r\n", '')

        print("Starting")

    return 0, arduino


