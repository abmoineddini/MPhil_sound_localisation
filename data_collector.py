import serial
import winsound
def collectData(COMPort, Period, Name, DirectoryName):
    arduino = serial.Serial(COMPort , 2000000, timeout=1)
    Channel1 = []
    Channel2 = []
    Channel3 = []
    Channel4 = []
    Time = []
    period = int(Period)
    sR = int(4000/3.5)
    period = period*sR
    for i in range(period):
        line = arduino.readline()

        if line != (''):
            print(line)
            try:
                string = line.decode()
            except:
                print("ignored")
            else:
                numS = string.replace("\r\n", '')
                vals = numS.split(" ")
                if len(vals)>3:
                    if vals[0].isdigit():
                        if vals[1].isdigit():
                            if vals[2].isdigit():
                                if vals[3].isdigit():
                                    Channel1.append(int(vals[0]))
                                    Channel2.append(int(vals[1]))
                                    Channel3.append(int(vals[2]))
                                    Channel4.append(int(vals[3]))
                                    Time.append(i/sR)

    arduino.close()
    import pandas as pd
    dict = {'Time (s)' : Time, 'Channel 1 (V)': Channel1,'Channel 2 (V)': Channel2, 'Channel 3 (V)': Channel3, 'Channel4 (V)': Channel4}

    df = pd.DataFrame(dict)
    dataBaseName = DirectoryName+"/"+"c_" + Name + ".csv"
    df.to_csv(dataBaseName)

    return [Channel1,Channel2, Channel3,Channel4, Time]

####################################Individual Collection Method#######################################
def collectDataIndividual(COMPort, Period, Name, DirectoryName):
    arduino = serial.Serial(COMPort , 2000000, timeout=1)
    Channel1 = []
    Channel2 = []
    Channel3 = []
    Channel4 = []
    Time = []
    period = int(Period)
    sR = int(4000/3.5)
    period = period*sR
    for i in range(period):
        line = arduino.readline()

        if line != (''):
            print(line)
            try:
                string = line.decode()
            except:
                print("ignored")
            else:
                numS = string.replace("\r\n", '')
                vals = numS.split(" ")
                if len(vals)>3:
                    if vals[0].isdigit():
                        if vals[1].isdigit():
                            if vals[2].isdigit():
                                if vals[3].isdigit():
                                    Channel1.append(int(vals[0]))
                                    Channel2.append(int(vals[1]))
                                    Channel3.append(int(vals[2]))
                                    Channel4.append(int(vals[3]))
                                    Time.append(i/sR)

    arduino.close()
    import pandas as pd
    dict = {'Time (s)' : Time, 'Channel 1 (V)': Channel1,'Channel 2 (V)': Channel2, 'Channel 3 (V)': Channel3, 'Channel4 (V)': Channel4}

    df = pd.DataFrame(dict)
    dataBaseName = DirectoryName + "/"+"i_" + Name + ".csv"
    df.to_csv(dataBaseName)

    return [Channel1,Channel2, Channel3,Channel4, Time]

####################################Testing Collection Method#######################################
def collectDataTest(COMPort, Period): #, AudioFileName):
    arduino = serial.Serial(COMPort, 2000000, timeout=1)
    Channel1 = []
    Channel2 = []
    Channel3 = []
    Channel4 = []
    Time = []
    period = int(Period)
    sR = int(4000 / 3.5)
    period = period * sR
    for i in range(period):
        line = arduino.readline()

        if line != (''):
            print(line)
            try:
                string = line.decode()
            except:
                print("ignored")
            else:
                numS = string.replace("\r\n", '')
                vals = numS.split(" ")
                if len(vals) > 3:
                    if vals[0].isdigit():
                        if vals[1].isdigit():
                            if vals[2].isdigit():
                                if vals[3].isdigit():
                                    Channel1.append(int(vals[0]))
                                    Channel2.append(int(vals[1]))
                                    Channel3.append(int(vals[2]))
                                    Channel4.append(int(vals[3]))
                                    Time.append(i / sR)

    arduino.close()



    arduino.close()
    import pandas as pd
    dict = {'Time (s)': Time, 'Channel 1 (V)': Channel1,'Channel 2 (V)': Channel2, 'Channel 3 (V)': Channel3, 'Channel4 (V)': Channel4}

    df = pd.DataFrame(dict)
    dataBaseName = "Temp/Test.csv"
    df.to_csv(dataBaseName)
    print(dataBaseName)
    return [Channel1,Channel2, Channel3,Channel4, Time]