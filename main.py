from data_collector import *
import matplotlib.pyplot as plt
import os
import pandas as pd
from os import listdir
import winsound
from data_sender import *
from datetime import date
from preprocessor import *
from csv import writer
import glob
from machine_learning import *

dataCollection = True
CheckPort = input("Would you like to Start collecting Data? ")
if CheckPort == "y" or CheckPort == "Y" or CheckPort == "Yes" or CheckPort == "yes":
    # Initialising the Stage and Data Collector
    COMPortMotor = input("Please Enter COM Port for the Stage : ")
    COMPortMotor  = "COM"+COMPortMotor
    print(COMPortMotor )
    currAng, MotorController = Inititialise(COMPortMotor )
    time.sleep(1)
    print("Initialisation of Stage Completed")
    COMPortCollector = input("Please Enter COM Port for Data Collector : ")
    COMPort  = "COM"+COMPortCollector
    print(COMPort)
    # print("Sending Angles")
    # currAng = AngleSet(30, MotorController)
    Increment = input("Please enter the desired Increment in degrees: ")
    RotationAngle = input("Please enter the angle you would like to cover: ")
    DirectionOfRot = input ("Please enter the Direction of Roation (0 = Antliclockwise, 1 = Clockwise: ")
    Method = input("Continuous or Individual Collections? (i for individual & c for Continious)")
    today = date.today()
    print("Today's date:", today)
    TrainingDirectoryName = "TrainingData/" + str(today)
    if os.path.isdir(TrainingDirectoryName):
        print("Adding to Figure Directory")
    else:
        os.mkdir(TrainingDirectoryName)

    while dataCollection:
        Increment = int(Increment)
        div = 2*int(int(RotationAngle)/Increment)+1
        for inc in range(0, div):
            if DirectionOfRot == 1:
                if inc <= (div-1)/2:
                    angle = Increment*inc
                else:
                    angle = int(RotationAngle)-Increment * inc
            else:
                if inc <= (div-1)/2:
                    angle = Increment*inc
                else:
                    angle = (Increment * inc-int(RotationAngle))
            if Method == 'c':
                print("Continuous Data Collection")
                print("Sending Angles")
                currAng = AngleSet(angle, MotorController, currAng)
                # AudioFiles = [f for f in listdir("AudioFiles/")]
                Name = str(currAng)
                print(Name)
                time.sleep(1)
                Period = 10
                print("Startting to Collect Data for: ", Period, '(s)')
                # CheckPeriod = input("Is that Correct?")
                # while CheckPeriod == "n" or CheckPeriod == "N" or CheckPeriod == "no" or CheckPeriod == "No":
                #     Period = input("Please Enter the Desired Time Period: ")
                #     print(Period)
                #     print("Starting to Collect Data for: ", Period, '(s)')
                #     CheckName = input("Is that Correct?")
                # AudioFileName = "AudioFiles/" + Name
                # winsound.PlaySound(AudioFileName, winsound.SND_ASYNC | winsound.SND_ALIAS)
                #
                # CSVName = Name.replace('.wav', '')
                NameTest = True
                TrainingDataDirectory = [f for f in listdir(TrainingDirectoryName)]
                testNum = 1
                while NameTest:
                    CSVNameCheck = "c_" +Name + '-Test'+ str(testNum) + '.csv'
                    if CSVNameCheck in TrainingDataDirectory:
                        print("File Already exist, Trying another name.")
                        testNum = testNum+1
                    else:
                        CSVName = Name + '-Test'+ str(testNum)
                        NameTest = False
                print(CSVName)
                [Channel1,Channel2, Channel3,Channel4, Time] = collectData(COMPort, Period, CSVName, TrainingDirectoryName)
                plt.plot(Time, Channel1)
                plt.show()
                plt.plot(Time, Channel2)
                plt.show()
                plt.plot(Time, Channel3)
                plt.show()
                plt.plot(Time, Channel4)
                plt.show()
                plt.show()
                winsound.PlaySound(None, winsound.SND_PURGE)
                DataCheck = 'y' #input("Are you happy with the Data? ")
                while DataCheck == "n" or DataCheck == "N" or DataCheck == "no" or DataCheck == "No":
                    Nametoremove = "TrainingData/" + CSVName + ".csv"
                    os.remove(Nametoremove)


                    # winsound.PlaySound(AudioFileName, winsound.SND_ASYNC | winsound.SND_ALIAS)
                    [Channel1,Channel2, Channel3,Channel4, Time] = collectData(COMPort, Period, CSVName, TrainingDirectoryName)

                    plt.plot(Time, Channel1)
                    plt.plot(Time, Channel2)
                    plt.plot(Time, Channel3)
                    plt.plot(Time, Channel4)
                    plt.show()
                    # winsound.PlaySound(None, winsound.SND_PURGE)
                    DataCheck = 'y' #input("Are you happy with the Data? ")

            elif Method=='i':
                print("Individual Data Collection")
                print("Sending Angles")
                currAng = AngleSet(angle, MotorController, currAng)
                # AudioFiles = [f for f in listdir("AudioFiles/")]
                Name = str(currAng)
                print(Name)
                time.sleep(1)
                Period = 3
                print("Startting to Collect Data for: ", Period, '(s)')
                # CheckPeriod = input("Is that Correct?")
                # while CheckPeriod == "n" or CheckPeriod == "N" or CheckPeriod == "no" or CheckPeriod == "No":
                #     Period = input("Please Enter the Desired Time Period: ")
                #     print(Period)
                #     print("Starting to Collect Data for: ", Period, '(s)')
                #     CheckName = input("Is that Correct?")
                # AudioFileName = "AudioFiles/" + Name
                # winsound.PlaySound(AudioFileName, winsound.SND_ASYNC | winsound.SND_ALIAS)
                #
                # CSVName = Name.replace('.wav', '')
                NameTest = True
                TrainingDataDirectory = [f for f in listdir(TrainingDirectoryName)]
                testNum = 1
                while NameTest:
                    CSVNameCheck = "i_" + Name + '-Test' + str(testNum) + '.csv'
                    if CSVNameCheck in TrainingDataDirectory:
                        print("File Already exist, Trying another name.")
                        testNum = testNum + 1
                    else:
                        CSVName = Name + '-Test' + str(testNum)
                        NameTest = False

                print(CSVName)
                [Channel1, Channel2, Channel3, Channel4, Time] = collectDataIndividual(COMPort, Period, CSVName,TrainingDirectoryName)
                plt.plot(Time, Channel1)
                plt.show()
                plt.plot(Time, Channel2)
                plt.show()
                plt.plot(Time, Channel3)
                plt.show()
                plt.plot(Time, Channel4)
                plt.show()
                winsound.PlaySound(None, winsound.SND_PURGE)
                DataCheck = 'y'  # input("Are you happy with the Data? ")
                while DataCheck == "n" or DataCheck == "N" or DataCheck == "no" or DataCheck == "No":
                    Nametoremove = "TrainingData/" + CSVName + ".csv"
                    os.remove(Nametoremove)

                    # winsound.PlaySound(AudioFileName, winsound.SND_ASYNC | winsound.SND_ALIAS)
                    [Channel1, Channel2, Channel3, Channel4, Time] = collectDataIndividual(COMPort, Period, CSVName, TrainingDirectoryName)

                    plt.plot(Time, Channel1)
                    plt.plot(Time, Channel2)
                    plt.plot(Time, Channel3)
                    plt.plot(Time, Channel4)
                    plt.show()
                    # winsound.PlaySound(None, winsound.SND_PURGE)
                    DataCheck = 'y'  # input("Are you happy with the Data? ")

                # if currAng == 0 or currAng == 360 or currAng == -360:
                #     currAng, MotorController = Calibrate(COMPortMotor, MotorController)
                #     time.sleep(1)
            else:
                print("Invalid Answer!")
                Method = input("Continuous or Individual Collections? (i for individual & c for Continious)")

            ToContinue = 'y' #input("would you like to Continue with collecting data? ")

        if ToContinue == "n" or ToContinue == "N" or ToContinue == "No" or ToContinue == "no":
            dataCollection = False





StartPreprocessing = input("Should I Start the Preprocessing? ")
if StartPreprocessing == "y" or StartPreprocessing == "Y" or StartPreprocessing == "Yes" or StartPreprocessing == "yes":

    
    if os.path.isdir("Figure/Training"):
        print("Adding to Figure Directory")
    else:
        os.mkdir("Figure/Training")
        os.mkdir("Figure/Testing")
        os.mkdir("Figure/Validation")
    for i in os.listdir("TrainingData"):
        DirectoryMasterTraining = "TrainingData/"+i+"/"
        csv_files = glob.glob(os.path.join(DirectoryMasterTraining, "*.csv"))
        for x in csv_files[0:]:
            dataFileName = x

            print(x)
            NAMEunprocessed = x.replace(".csv", "")
            NAMEunprocessed = NAMEunprocessed.split("\\")
            print(NAMEunprocessed)
            print(NAMEunprocessed[1][0])

            NAMEunprocessed = NAMEunprocessed[1].split("_")
            print(NAMEunprocessed)
            if NAMEunprocessed[0] == "c":
                method = 0
                print("True")
            else:
                method = 1
            NAMEunprocessed = NAMEunprocessed[1]
            NAMEunprocessed = NAMEunprocessed.split("-")
            x = NAMEunprocessed[0]
            print(x)
            check = 0

            if os.path.isfile("Tracking/ProcessedData.csv"):
                print("Processed data collector Already exists")

                PDCL = pd.read_csv("Tracking/ProcessedData.csv")
                print(PDCL)
                ProcessedDataChecklist = PDCL.to_numpy()
                ProcessedDataChecklist = ProcessedDataChecklist[:]

                if dataFileName.split("/")[1] in ProcessedDataChecklist:
                    check = 1
                    continue

            if check == 0:
                [FolderTraining, FolderTesting, FolderValidation] = Classifier(x)
                print("it reaches here")
                df = pd.read_csv(dataFileName)
                data = df.to_numpy()
                print(dataFileName)

                if method==0:
                    figure_maker(data, FolderTraining, FolderTesting, FolderValidation, dataFileName)
                    print("Making figure for continuous Data")
                else:
                    #figure_makerMeth2(data, FolderTraining, FolderTesting, FolderValidation, dataFileName)
                    figure_makerMeth2AutoSize(data, FolderTraining, FolderTesting, FolderValidation, dataFileName)
                #TestingPreprocessing(data)

                if os.path.isfile("Tracking/ProcessedData.csv"):
                    with open("Tracking/ProcessedData.csv", 'a+' ,newline='') as f_object:
                        # Pass the CSV  file object to the writer() function
                        writer_object = writer(f_object)
                        # Result - a writer object
                        # Pass the data in the list as an argument into the writerow() function
                        writer_object.writerow([dataFileName.split("/")[1]])
                        # Close the file object
                        f_object.close()
                else:
                    dict = {"File Name": [dataFileName.split("/")[1]]}
                    df = pd.DataFrame(dict)
                    df.to_csv("Tracking/ProcessedData.csv")

            #CheckPoint = input("Would you like to continue? ")
            #plt.close('all')



print("Finished Creating Relevant Files")
# quit()

labels = os.listdir("Figure/Training")
labelsInt = []
for i in labels:
    labelsInt.append(int(i))
labelsInt.sort()
labels = []
for i in labelsInt:
    labels.append(str(i))

StartTraining = input("Should I Start the Training? ")
if StartTraining == "y" or StartTraining == "Y" or StartTraining == "yes" or StartTraining == "Yes":

    trainingSTFT = "Figure/Training"
    validationSTFT = "Figure/Validation"
    testingSTFT = "Figure/Testing"

    img_size = 150

    print(labels)
    [STFTModel, acc, val_acc, loss, val_loss]= CNN_Training(trainingSTFT, validationSTFT, 150, LearningRate=0.00005, dataType="STFT", img_size=img_size, label = labels)

    STFTModel.save("DirectionRecCNN")

    for i in range(len(acc)):
        FileAdd = [acc[i], val_acc[i], loss[i], val_loss[i]]
        with open("Tracking/AccuracyHistory.csv", 'a+', newline='') as f_object:
            # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow(FileAdd)
            # Close the file object
            f_object.close()
            FileAdd = []

    STFTModel = tf.keras.models.load_model("DirectionRecCNN")
    # Testinig Peformance
    print("STFT CNN Test result")
    [y_val, predictions] = TestingNetwrok(STFTModel, testingSTFT, img_size, labels)

    for i in range(len(y_val)):
        FileAdd = [y_val[i], predictions[i]]
        with open("Tracking/TestingValidationCNN.csv", 'a+', newline='') as f_object:
            # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow(FileAdd)
            # Close the file object
            f_object.close()
            FileAdd = []



    STFTmodelName = 'STFTModel.yaml'

    Save_CNN(STFTModel, Name=STFTmodelName)

df = pd.read_csv("Tracking/TestingValidationCNN.csv")
CAT = labels
DegNum = int(labels[1])
DegNum = str(DegNum)
data = df.to_numpy()
y_val = data[:,0]
predictions = data[:,1]
fig = plt.figure()
confusion_mtx = tf.math.confusion_matrix(y_val, predictions)
print(confusion_mtx)
con_matrix = np.zeros((len(labels),len(labels)))
for i in range(len(confusion_mtx[1])):
    row = confusion_mtx[i].numpy()
    rowSum = row.sum()
    print(rowSum)
    for j in range(len(row)):
        print(len(row))
        print(row[j])
        con_matrix[i, j] = row[j] / rowSum

sns.heatmap(con_matrix, xticklabels=CAT, yticklabels=CAT,
            annot=True, fmt='.2f', cmap = "OrRd")
plt.rc('font', family='Helvetica')
plt.title('Confusion Matix', fontsize=22)
plt.xlabel('Prediction', fontsize=20)
plt.ylabel('Label', fontsize=20)
ConfunstionMatrixName = "Figures/" + DegNum + "ConfusionMatrixValidation.png"
fig.savefig(ConfunstionMatrixName, transparent=True, bbox_inches='tight',pad_inches=0.25)
plt.show()