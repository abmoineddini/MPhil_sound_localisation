import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.signal as sig
from random import randint

def SectionCutting(V, t, FileName):
    seperation = []
    seperation.append(0)
    time = t
    voltage = V

    uplowBoundNull = 0.1
    perofMaxVal = 0.7
    binSize = 100
    perNullDen = 0.6
    perMaxDen = 0.7
    # Total_Size = len(voltage-100)
    # # plt.plot(t, voltage)
    # # plt.show()
    #
    # detenV = sig.detrend(voltage)
    #
    # filter = sig.butter(2, [95, 1500], 'bandpass', fs=4000, output='sos')
    # corrVoltage = sig.sosfilt(filter, detenV)

    # plt.plot(t, fderenV)
    # plt.show()

    t = time[0: 70000]
    fderenV = V[0: 70000]

    maxVal = max(fderenV)

    Nullpeaks, _ = sig.find_peaks(fderenV, height=(-uplowBoundNull, uplowBoundNull))
    # smallPeaks, _ = sig.find_peaks(fderenV, distance= 4000, height=(0.01, 0.05))
    peaks, _ = sig.find_peaks(fderenV, height=perofMaxVal*maxVal)
    plt.plot(t, fderenV, linewidth=0.05)
    plt.scatter(t[peaks], fderenV[peaks], color='red')
    # plt.scatter(t[smallPeaks], fderenV[smallPeaks], color='black')
    # plt.scatter(t[largePeaks], fderenV[largePeaks], color='green')
    plt.show()
    # PEAKS = np.array(peaks)

    f, (a0, a1, a2) = plt.subplots(3, 1, gridspec_kw={'height_ratios': [10,3,3]})

    #plt.subplot(3, 1, 1)
    a0.plot(t, fderenV, linewidth=0.1, label="Signal")
    a0.scatter(t[Nullpeaks], fderenV[Nullpeaks], color='red', label="Low amplitude peaks")
    a0.scatter(t[peaks], fderenV[peaks], color='green', label="Large amplitude peak")
    #a0.xlabel('Time (s)', fontsize=20)
    # a0.set_ylabel('Voltage (V)', fontsize=20)
    # a0.set_xlabel('Time (s)', fontsize=20)
    # a0.xaxis.tick_top()
    # a0.xaxis.set_label_position('top')
    # a0.legend(loc='upper right')
    # a0.set_xlim([0, 17.5])
    # plt.subplot(3, 1, 2)
    NullpeakDensity, NullpeakRange, _ = a1.hist(Nullpeaks, bins=binSize, facecolor='r', alpha=1, edgecolor='k', linewidth=1)
    # a1.set_title('low amplitude Peak Distribution Density', fontsize=20)
    #a1.set_ylabel('Density', fontsize=20)
    # a1.set_xticks([])
    # a1.set_xlim([0, 70000])
    #plt.subplot(3, 1, 3)
    peakDensity, peakRange, _ = a2.hist(peaks, bins=binSize, facecolor='g', alpha=1, edgecolor='k', linewidth=1)
    # a2.set_title('Signal Peak Distribution Density', fontsize=20)
    # f.text(-0.025, 0.3, 'Density', va='center', rotation='vertical', fontsize=20)
    # #a2.set_ylabel('Density', fontsize=20)
    # a2.set_xticks([])
    # a2.set_xlim([0, 70000])
    # #f.tight_layout()

    # plt.title('Voltage-Time graph of the raw data', fontsize=24)
    # plt.rc('font', family='Helvetica')

    # plt.subplots_adjust(left=0.1,
    #                     bottom=0.1,
    #                     right=0.9,
    #                     top=0.9,
    #                     wspace=0,
    #                     hspace=0.6)
    # f.savefig('Figures/DataDistribtion.png', bbox_inches='tight', pad_inches=0.25)
    plt.show()


    NullmaxDensity  = max(NullpeakDensity)
    maxDensity  = max(peakDensity)

    # print(NullpeakDensity)
    # print(NullpeakRange)
    # print(peakDensity)
    # print(peakRange)

    interestingNullPeakDis = []
    interestingPeakDis = []
    for i in range(len(peakDensity)):
        if NullpeakDensity[i]>= perNullDen* NullmaxDensity:
            interestingNullPeakDis.append(i)

    for i in range(len(peakDensity)):
        if peakDensity[i]>= perMaxDen*maxDensity:
            interestingPeakDis.append(i)

    # print(interestingNullPeakDis)
    # print(interestingPeakDis)

    for i in range(len(interestingNullPeakDis)):
        if interestingNullPeakDis[i] in interestingPeakDis:
            interestingNullPeakDis[i] = ''
    chekcer = True
    while chekcer:
        if '' in interestingNullPeakDis:
            interestingNullPeakDis.remove('')
        else:
            chekcer = False
    # print(interestingNullPeakDis)

    # print(NullpeakRange)
    NullpeakRange = np.insert(NullpeakRange, 0, 0)


    for i in range(len(interestingNullPeakDis)):
        place = interestingNullPeakDis[i]+2
        seperation.append(int((NullpeakRange[place])))
    #print(seperation)


    for i in range(5):
        for i in range(0,len(seperation)-1):
            if seperation[i]+3000 >= seperation[i+1]:
                NewSep = (seperation[i] + seperation[i+1])/2 - randint(50, 500)
                seperation[i] = ''
                seperation[i+1] = int(NewSep)

        chekcer = True
        while chekcer:
            if '' in seperation:
                seperation.remove('')
            else:
                chekcer = False

    from mutagen.wave import WAVE
    fileName = FileName.replace("TrainingData\\", '')
    AudioFileName = fileName.split('-')
    AudioFileName = "AudioOriginal/"+AudioFileName[0]+'.wav'

    audio = WAVE(AudioFileName)
    audio_info = audio.info
    length = int(audio_info.length)

    for i in range(0,len(seperation)-1):
        if seperation[i] + length*4000*0.7 >= seperation[i + 1]:
            seperation[i+1] = 0

    chekcer = True
    while chekcer:
        if 0 in seperation:
            seperation.remove(0)
        else:
            chekcer = False
    fig1 = plt.figure()
    #print(seperation)
    plt.plot(t, fderenV, linewidth=0.1, label="Signal")
    plt.scatter(t[seperation], fderenV[seperation], color='red', label = "Seperation Points")
    # plt.rc('font', family='Helvetica')
    # plt.xlabel('Time (s)', fontsize=20)
    # plt.ylabel('Voltage (V)', fontsize=20)
    # plt.xlim([0,17.5])
    # fig1.savefig('Figures/SectionedPoints.png', bbox_inches='tight', pad_inches=0.25)
    plt.show()

    #print(len(seperation))
    #print(len(voltage))

    displacemetData = 750
    whileChecker = True
    while whileChecker:
        if seperation[len(seperation)-1]+70000<=len(voltage):
            #print("old Seperation : ",seperation[len(seperation) - 1])
            t = time[seperation[len(seperation)-1]-displacemetData: seperation[len(seperation)-1]+80000]
            fderenV = voltage[seperation[len(seperation)-1]-displacemetData: seperation[len(seperation)-1]+80000]

            maxVal = max(fderenV)

            NewSection = []

            Nullpeaks, _ = sig.find_peaks(fderenV, height=(-uplowBoundNull, uplowBoundNull))
            peaks, _ = sig.find_peaks(fderenV, height=perofMaxVal * maxVal)


            plt.plot(t, fderenV, linewidth=0.05)
            plt.scatter(t[Nullpeaks], fderenV[Nullpeaks], color='red')
            plt.scatter(t[peaks], fderenV[peaks], color='green')

            NullpeakDensity, NullpeakRange, _ = plt.hist(Nullpeaks, bins=binSize, facecolor='r', alpha=1, edgecolor='k', linewidth=1)

            peakDensity, peakRange, _ = plt.hist(peaks, bins=binSize, facecolor='g', alpha=1, edgecolor='k', linewidth=1)
            # plt.show()
            plt.close()

            NullmaxDensity = max(NullpeakDensity)
            maxDensity = max(peakDensity)

            # print(NullpeakDensity)
            # print(NullpeakRange)
            # print(peakDensity)
            # print(peakRange)

            interestingNullPeakDis = []
            interestingPeakDis = []
            for i in range(len(peakDensity)):
                if NullpeakDensity[i] >= perNullDen * NullmaxDensity:
                    interestingNullPeakDis.append(i)

            for i in range(len(peakDensity)):
                if peakDensity[i] >= perMaxDen * maxDensity:
                    interestingPeakDis.append(i)

            #print(interestingNullPeakDis)
            #print(interestingPeakDis)

            for i in range(len(interestingNullPeakDis)):
                if interestingNullPeakDis[i] in interestingPeakDis:
                    interestingNullPeakDis[i] = ''
            chekcer = True
            while chekcer:
                if '' in interestingNullPeakDis:
                    interestingNullPeakDis.remove('')
                else:
                    chekcer = False
            #print(interestingNullPeakDis)

            # print(NullpeakRange)
            NullpeakRange = np.insert(NullpeakRange, 0, 0)

            for i in range(len(interestingNullPeakDis)):
                place = interestingNullPeakDis[i] + 2
                NewSection.append(int((NullpeakRange[place])))
            #print(seperation)
            for j in range(10):
                for i in range(len(NewSection) - 1):
                    if NewSection[i] + length * 4000*0.7 >= NewSection[i + 1] and NewSection[i] + length * 4000*0.7 <= NewSection[i + 1]:
                        NewSection[i + 1] = 0

                chekcer = True
                while chekcer:
                    if 0 in NewSection:
                        NewSection.remove(0)
                    else:
                        chekcer = False

            for j in range(10):
                for i in range(0, len(NewSection) - 1):
                    if NewSection[i] + 2000 >= NewSection[i + 1]:
                        NewSep = (NewSection[i] + NewSection[i + 1]) / 2 - randint(50, 100)
                        NewSection[i] = ''
                        NewSection[i + 1] = int(NewSep)

                chekcer = True
                while chekcer:
                    if '' in NewSection:
                        NewSection.remove('')
                    else:
                        chekcer = False

            for i in range(2):
                for i in range(len(NewSection) - 1):
                    if NewSection[i] + length * 4000*0.7 >= NewSection[i + 1]:
                        NewSection[i + 1] = 0

                chekcer = True
                while chekcer:
                    if 0 in NewSection:
                        NewSection.remove(0)
                    else:
                        chekcer = False


            #print("NewSelection")
            #print(NewSection)
            plt.plot(t, fderenV, linewidth=0.05)
            plt.scatter(t[NewSection], fderenV[NewSection], color='red')
            plt.show()
            #plt.close()
            #print("New parts to add : " , NewSection)
            #print(len(NewSection))

            previousSep = seperation[len(seperation) - 1]
            for i in range(1,len(NewSection)):
                seperation.append(NewSection[i]+previousSep-displacemetData)
        else:
            whileChecker = False
    #print("New seperation : ", seperation)
    return(seperation)


def SectionCuttingTesting(V, t):
    seperation = []

    t = t
    fderenV = V

    maxVal = max(fderenV)

    Nullpeaks, _ = sig.find_peaks(fderenV, height=(-0.07, 0.07))
    #print(Nullpeaks)
    #print(type(Nullpeaks))
    Nullpeaks = np.transpose(Nullpeaks)
    peaks, _ = sig.find_peaks(fderenV, height=0.5*maxVal)


    f, (a0, a1, a2) = plt.subplots(3, 1, gridspec_kw={'height_ratios': [7, 2, 2]})
    #plt.subplot(3, 1, 1)
    a0.plot(t, fderenV, linewidth=0.05)
    # a0.scatter(t[Nullpeaks], fderenV[Nullpeaks], color='red')
    # a0.scatter(t[peaks], fderenV[peaks], color='green')

    #plt.subplot(3, 1, 2)
    NullpeakDensity, NullpeakRange, _ = a1.hist(Nullpeaks, bins=60, facecolor='r', alpha=1, edgecolor='k', linewidth=1)

    #plt.subplot(3, 1, 3)
    peakDensity, peakRange, _ = a2.hist(peaks, bins=60, facecolor='g', alpha=1, edgecolor='k', linewidth=1)
    f.tight_layout()
    # plt.show()


    NullmaxDensity  = max(NullpeakDensity)
    maxDensity  = max(peakDensity)

    interestingNullPeakDis = []
    interestingPeakDis = []
    for i in range(len(peakDensity)):
        if NullpeakDensity[i]>= 0.8* NullmaxDensity:
            interestingNullPeakDis.append(i)

    for i in range(len(peakDensity)):
        if peakDensity[i]>= 0.5* maxDensity:
            interestingPeakDis.append(i)


    for i in range(len(interestingNullPeakDis)):
        if interestingNullPeakDis[i] in interestingPeakDis:
            interestingNullPeakDis[i] = ''
    chekcer = True
    while chekcer:
        if '' in interestingNullPeakDis:
            interestingNullPeakDis.remove('')
        else:
            chekcer = False


    NullpeakRange = np.insert(NullpeakRange, 0, 0)


    for i in range(len(interestingNullPeakDis)):
        place = interestingNullPeakDis[i]+2
        seperation.append(int((NullpeakRange[place])))
    #print(seperation)


    for i in range(5):
        for i in range(0,len(seperation)-1):
            if seperation[i]+3000 >= seperation[i+1]:
                NewSep = (seperation[i] + seperation[i+1])/2 - randint(50, 500)
                seperation[i] = ''
                seperation[i+1] = int(NewSep)

        chekcer = True
        while chekcer:
            if '' in seperation:
                seperation.remove('')
            else:
                chekcer = False
    diffLow = []

    # if len(seperation) >= 2:
    #     for i in seperation:
    #         if i < interestingPeakDis[0]:
    #             diffLow.append(interestingPeakDis[0]-i)
    #
    #     if len(diffLow) > 1:
    #         seperation[0] = seperation[1]
    #         seperation[1] = seperation[2]

    #plt.plot(t, fderenV)
    #plt.scatter(t[seperation], fderenV[seperation], color='red')
    #plt.show()
    #seperation[len(seperation)]=interestingPeakDis[len(interestingPeakDis)]+1000
    #print(seperation)
    return(seperation)


def SepWithSTFT(normV1, normV2, normV3, normV4, t, Fs):
    inst = 100
    f1, t1, Zxx1 = sig.stft(normV1, Fs, nperseg=inst)
    fig1 = plt.figure(frameon=False)
    ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
    plt.pcolormesh(t1, f1, np.abs(Zxx1), shading='gouraud')
    # plt.axis('off')
    # plt.ylim([0, 200])
    ax1.set_axis_off()
    plt.tight_layout()
    # plt.show()

    f2, t2, Zxx2 = sig.stft(normV2, Fs, nperseg=inst)
    fig1 = plt.figure(frameon=False)
    ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
    plt.pcolormesh(t2, f2, np.abs(Zxx2), shading='gouraud')
    # plt.axis('off')
    # plt.ylim([0, 200])
    ax1.set_axis_off()
    plt.tight_layout()
    plt.show()

    f3, t3, Zxx3 = sig.stft(normV3, Fs, nperseg=inst)
    fig1 = plt.figure(frameon=False)
    ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
    plt.pcolormesh(t3, f3, np.abs(Zxx3), shading='gouraud')
    # plt.axis('off')
    # plt.ylim([0, 200])
    ax1.set_axis_off()
    plt.tight_layout()
    plt.show()

    f4, t4, Zxx4 = sig.stft(normV4, Fs, nperseg=inst)
    fig1 = plt.figure(frameon=False)
    ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
    plt.pcolormesh(t4, f4, np.abs(Zxx4), shading='gouraud')
    # plt.axis('off')
    # plt.ylim([0, 200])
    ax1.set_axis_off()
    plt.tight_layout()
    plt.show()

    z1 = abs(Zxx1)
    z2 = abs(Zxx2)
    z3 = abs(Zxx3)
    z4 = abs(Zxx4)
    count = 0

    for i in f1:
        if round(i) == 80:
            #print(count)
            minFreq = count
            continue
        count = count + 1

    #print(f1[minFreq])
    maxz1 = max(z1[minFreq])
    maxz2 = max(z2[minFreq])
    maxz3 = max(z3[minFreq])
    maxz4 = max(z4[minFreq])
    z = [z1[minFreq], z2[minFreq], z3[minFreq], z4[minFreq]]
    Zs = [maxz1, maxz2, maxz3, maxz4]
    maxZ = max(Zs)
    indexZ = Zs.index(maxZ)
    #print(indexZ)
    z = z[indexZ]
    #z = z[1]
    #print(z)
    upperLim = max(z) * 0.55
    Nullpeaks, _ = sig.find_peaks(z, height=upperLim)
    plt.plot(t1, z)
    plt.scatter(t1[Nullpeaks], z[Nullpeaks])
    # plt.plot(f2, z2)
    # plt.plot(f3, z3)
    # plt.plot(f4, z4)
    # plt.show()

    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    plt.plot(t, normV1, label="Channel 1", linewidth=0.5, alpha=0.3)
    plt.scatter(t1[Nullpeaks], z[Nullpeaks], color='k')
    # plt.show()

    adjPe = inst / 2
    Sectioning = Nullpeaks*adjPe
    # f1, t1, Zxx1 = sig.stft(normV1[Nullpeaks[0] * adjPe: Nullpeaks[1] * adjPe], Fs, nperseg=inst)
    # fig1 = plt.figure(frameon=False)
    # ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
    # plt.pcolormesh(t1, f1, np.abs(Zxx1), shading='gouraud')
    # # plt.axis('off')
    # # plt.ylim([0, 200])
    # ax1.set_axis_off()
    # plt.tight_layout()
    # plt.show()
    plt.close()
    return Sectioning

def SepWithSTFTAuto(data, time, Fs):
    inst = 100
    normV1 = data[0:len(time), 0]
    f, t, Zxx = sig.stft(normV1, Fs, nperseg=inst)
    fig = plt.figure(frameon=False)
    ax1 = plt.Axes(fig, [0., 0., 1., 1.])
    plt.pcolormesh(t, f, np.abs(Zxx), shading='gouraud')
    ax1.set_axis_off()
    plt.tight_layout()
    plt.show()

    z1 = abs(Zxx)

    count = 0
    for i in f:
        if round(i) == 80:
            #print(count)
            minFreq = count
            continue
        count = count + 1

    # print(f[minFreq])

    z = z1[minFreq]
    # print(z)


    upperLim = max(z) * 0.50
    Nullpeaks, _ = sig.find_peaks(z, height=upperLim)
    plt.plot(t, z)
    plt.scatter(t[Nullpeaks], z[Nullpeaks])
    plt.show()

    def truncate(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    plt.plot(time, normV1, label="Channel 1", linewidth=0.5, alpha=0.3)
    plt.scatter(t[Nullpeaks], z[Nullpeaks], color='k')
    plt.show()
    print(Nullpeaks)

    if len(Nullpeaks) >1:
        adjPe = int(inst / 2)

        Sectioning = Nullpeaks*adjPe
        f, t, Zxx = sig.stft(normV1[Nullpeaks[0] * adjPe: Nullpeaks[1] * adjPe], Fs, nperseg=inst)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t, f, np.abs(Zxx), shading='gouraud')
        # plt.axis('off')
        # plt.ylim([0, 200])
        ax1.set_axis_off()
        plt.tight_layout()
        plt.show()
    else:
        Sectioning = [0]
    return Sectioning
