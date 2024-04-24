import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
from section_cutting import *
from os import listdir
from PIL import Image
import os
from os.path import isdir
from scipy.fft import fft, fftfreq
import random

def ProcessIm(Im1, Im2, fileName):
    image1 = Image.open(Im1)
    image1 = image1.rotate(90)

    image2 = Image.open(Im2)
    image1_size = image1.size
    new_image = Image.new('RGB', (2 * image1_size[0], image1_size[1]), (250, 250, 250))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1_size[0], 0))
    new_image.save(fileName)

def ProcessConcat(Im1, Im2, Im3, Im4, fileName):
    image1 = Image.open(Im1)
    image2 = Image.open(Im2)
    image3 = Image.open(Im3)
    image4 = Image.open(Im4)

    image1_size = image1.size

    new_image = Image.new('RGB', (2 * image1_size[0], 2*image1_size[1]), (250, 250, 250))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1_size[0], 0))
    new_image.paste(image3, (0, image1_size[1]))
    new_image.paste(image4, (image1_size[0], image1_size[1]))
    new_image.save(fileName)

def ProcessConcatAuto(Im, fileName):
    image1 = Image.open("Temp/"+Im[0])
    ChannelCount = 1
    if len(Im) > 1:
        image2 = Image.open("Temp/"+Im[1])
        ChannelCount = 2
        if len(Im) > 2:
            image3 = Image.open("Temp/"+Im[2])
            ChannelCount = 3
            if len(Im) > 3:
                image4 = Image.open("Temp/"+Im[3])
                ChannelCount = 4
                if len(Im) > 4:
                    image5 = Image.open("Temp/"+Im[4])
                    ChannelCount = 5
                    if len(Im) > 5:
                        image6 = Image.open("Temp/"+Im[5])
                        ChannelCount = 6
                        if len(Im) > 6:
                            image7 = Image.open("Temp/"+Im[6])
                            ChannelCount = 7
                            if len(Im) > 7:
                                image8 = Image.open("Temp/"+Im[7])
                                ChannelCount = 8
                                if len(Im) > 8:
                                    image9 = Image.open("Temp/" + Im[8])
                                    ChannelCount = 9

    image1_size = image1.size
    BlackImage = np.zeros([image1_size[1], image1_size[0], 3] ,dtype=np.uint8)
    BlackImage = Image.fromarray(BlackImage)

    if ChannelCount == 1:
        new_image = Image.new('RGB', (image1_size[0], image1_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.save(fileName)

    if ChannelCount == 2:
        new_image = Image.new('RGB', (2 * image1_size[0], 2*image1_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(BlackImage, (image1_size[0], 0))
        new_image.paste(image2, (image1_size[0], image1_size[1]))
        new_image.paste(BlackImage, (0, image1_size[1]))
        new_image.save(fileName)

    if ChannelCount == 3:
        new_image = Image.new('RGB', (2 * image1_size[0], 2*image1_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        new_image.paste(image3, (0, image1_size[1]))
        new_image.save(fileName)

    if ChannelCount == 4:
        new_image = Image.new('RGB', (2 * image1_size[0], 2*image1_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        new_image.paste(image3, (0, image1_size[1]))
        new_image.paste(image4, (image1_size[0], image1_size[1]))
        new_image.save(fileName)

    if ChannelCount == 5:
        new_image = Image.new('RGB', (3 * image1_size[0], 2*image1_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        new_image.paste(image3, (0, image1_size[1]))
        new_image.paste(image4, (image1_size[0], image1_size[1]))
        new_image.paste(image5, (2*image1_size[0], 0))
        new_image.save(fileName)

    if ChannelCount == 6:
        new_image = Image.new('RGB', (3 * image1_size[0], 2*image1_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        new_image.paste(image3, (0, image1_size[1]))
        new_image.paste(image4, (image1_size[0], image1_size[1]))
        new_image.paste(image5, (2*image1_size[0], 0))
        new_image.paste(image6, (2*image1_size[0], image1_size[1]))
        new_image.save(fileName)

    if ChannelCount == 7:
        new_image = Image.new('RGB', (4 * image1_size[0], 3*image1_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        new_image.paste(image3, (0, image1_size[1]))
        new_image.paste(image4, (image1_size[0], image1_size[1]))
        new_image.paste(image5, (2*image1_size[0], 0))
        new_image.paste(image6, (2*image1_size[0], image1_size[1]))
        new_image.paste(image7, (0, 2*image1_size[0]))
        new_image.save(fileName)

    if ChannelCount == 9:
        new_image = Image.new('RGB', (3 * image1_size[0], 3 * image1_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        new_image.paste(image3, (0, image1_size[1]))
        new_image.paste(image4, (image1_size[0], image1_size[1]))
        new_image.paste(image5, (2*image1_size[0], 0))
        new_image.paste(image6, (2*image1_size[0], image1_size[1]))
        new_image.paste(image7, (0, 2*image1_size[0]))
        new_image.paste(image8, (image1_size[0], 2*image1_size[1]))
        new_image.paste(image9, (2 * image1_size[0], 2 * image1_size[1]))
        new_image.save(fileName)

    if ChannelCount == 9:
        new_image = Image.new('RGB', (3 * image1_size[0], 3*image1_size[1]), (250, 250, 250))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        new_image.paste(image3, (0, image1_size[1]))
        new_image.paste(image4, (image1_size[0], image1_size[1]))
        new_image.paste(image5, (2*image1_size[0], 0))
        new_image.paste(image6, (2*image1_size[0], image1_size[1]))
        new_image.paste(image7, (0, 2*image1_size[1]))
        new_image.paste(image8, (image1_size[0], 2*image1_size[1]))
        new_image.paste(image9, (2 * image1_size[0], 2 * image1_size[1]))
        new_image.save(fileName)


def figure_maker(data, FolderSTFTTraining, FolderSTFTTesting, FolderValTesting, FileName):
    time = data[150:len(data)-1, 1]
    Ch1 = data[150:len(data)-1, 2]
    Ch2 = data[150:len(data) - 1, 3]
    Ch3 = data[150:len(data) - 1, 4]
    Ch4 = data[150:len(data) - 1, 5]
    Fs = 4000/3.5

    detenCh1 = sig.detrend(Ch1)
    detenCh2 = sig.detrend(Ch2)
    detenCh3 = sig.detrend(Ch3)
    detenCh4 = sig.detrend(Ch4)


    filter = sig.butter(2, [70,550], 'bandpass', fs=Fs, output='sos')
    corrCh1 = sig.sosfilt(filter, detenCh1)
    corrCh1 = (corrCh1*5)/1023
    corrCh2 = sig.sosfilt(filter, detenCh2)
    corrCh2 = (corrCh2*5)/1023
    corrCh3 = sig.sosfilt(filter, detenCh3)
    corrCh3 = (corrCh3*5)/1023
    corrCh4 = sig.sosfilt(filter, detenCh4)
    corrCh4 = (corrCh4*5)/1023

    TrainingDirectory = [f for f in listdir(FolderSTFTTraining)]
    TestDirectory = [f for f in listdir(FolderSTFTTesting)]
    ValidationDirectory = [f for f in listdir(FolderValTesting)]


    countTrain = int(len(TrainingDirectory))
    countTest = int(len(TestDirectory))
    countVal = int(len(ValidationDirectory))

    maxV1 = max(corrCh1)
    normV1 = corrCh1 / maxV1
    maxV2 = max(corrCh2)
    normV2 = corrCh2 / maxV2
    maxV3 = max(corrCh3)
    normV3 = corrCh3 / maxV3
    maxV4 = max(corrCh4)
    normV4 = corrCh4 / maxV4
    seperationPoints = SepWithSTFT(normV1, normV2, normV3, normV4, time, Fs)
    #seperationPoints = [0, len(normV1)-1]

    N = len(seperationPoints)
    Arr = np.arange(N)
    np.random.shuffle(Arr)
    Training = Arr[:round(N*0.8)]
    Validation = Arr[round(N*0.8):round(N*0.9)]
    Testing = Arr[round(N*0.9):round(N*1)]

    for i in range(0,N-1):
        Ch1pp = normV1[int(seperationPoints[i]):int(seperationPoints[i+1])]
        Ch2pp = normV2[int(seperationPoints[i]):int(seperationPoints[i+1])]
        Ch3pp = normV3[int(seperationPoints[i]):int(seperationPoints[i+1])]
        Ch4pp = normV4[int(seperationPoints[i]):int(seperationPoints[i+1])]

        #################################################### STFT Plots##################################################
        ## Channel 1
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch1pp, c=abs(Ch1pp*Ch1pp), s=abs(Ch1pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh1.png', bbox_inches='tight', pad_inches=0)

        f1, t1, Zxx1 = sig.stft(Ch1pp, Fs, nperseg=100)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t1, f1, np.abs(Zxx1), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([90, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh1.png', bbox_inches='tight', pad_inches=0)

        ## Channel 2
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch2pp, c=abs(Ch2pp*Ch2pp), s=abs(Ch2pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh2.png', bbox_inches='tight', pad_inches=0)

        f2, t2, Zxx2 = sig.stft(Ch2pp, Fs, nperseg=100)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t2, f2, np.abs(Zxx2), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([90, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh2.png', bbox_inches='tight', pad_inches=0)

        ##Channel 3
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch3pp, c=abs(Ch3pp*Ch3pp), s=abs(Ch3pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh3.png', bbox_inches='tight', pad_inches=0)

        f3, t3, Zxx3 = sig.stft(Ch3pp, Fs, nperseg=100)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t3, f3, np.abs(Zxx3), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([90, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh3.png', bbox_inches='tight', pad_inches=0)

        ## Channel 4
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch4pp, c=abs(Ch4pp*Ch4pp), s=abs(Ch4pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh4.png', bbox_inches='tight', pad_inches=0)

        f4, t4, Zxx4 = sig.stft(Ch4pp, Fs, nperseg=100)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t4, f4, np.abs(Zxx4), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.xlim([90, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh4.png', bbox_inches='tight', pad_inches=0)

        #################################################### FFT Plots##################################################
        #plt.style.use('dark_background')
        y1 = fft(Ch1pp)
        y2 = fft(Ch2pp)
        y3 = fft(Ch3pp)
        y4 = fft(Ch4pp)


        y1a = y1[80: 550]
        max_value1 = max(abs(y1a))
        Norm_y1 = abs(y1a) / 15 # max_value1
        Norm_y1a = abs(y1a)

        y2a = y2[80: 550]
        max_value2 = max(abs(y2a))
        Norm_y2 = abs(y2a) / 15 # max_value2
        Norm_y2a = abs(y2a)

        y3a = y3[80: 550]
        max_value3 = max(abs(y3a))
        Norm_y3 = abs(y3a) / 15 # max_value3
        Norm_y3a = abs(y3a)

        y4a = y4[80: 550]
        max_value4 = max(abs(y4a))
        Norm_y4 = abs(y4a) / 15 # max_value4
        Norm_y4a = abs(y4a)

        N = len(y4a)
        xf = fftfreq(N, 1/Fs)

        fig1 = plt.figure()
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.scatter(xf, Norm_y1a, c=4**abs(Norm_y1), s=abs(Norm_y1**4)*500)
        #plt.xlim([90, 500])
        plt.ylim([0, 16])
        plt.gray()
        plt.axis('off')
        ax1.set_axis_off()
        plt.tight_layout()
        fig1.savefig('Temp/Ch1fft.png', bbox_inches='tight', pad_inches=0)

        fig2 = plt.figure()
        ax2 = plt.Axes(fig2, [0., 0., 1., 1.])
        plt.scatter(xf, Norm_y2a, c=4**abs(Norm_y2), s=abs(Norm_y2**4)*500)
        #plt.xlim([90, 500])
        plt.ylim([0, 16])
        plt.gray()
        plt.axis('off')
        ax2.set_axis_off()
        plt.tight_layout()
        fig2.savefig('Temp/Ch2fft.png', bbox_inches='tight', pad_inches=0)

        fig3 = plt.figure()
        ax3 = plt.Axes(fig3, [0., 0., 1., 1.])
        plt.scatter(xf, Norm_y3a, c=4**abs(Norm_y3), s=abs(Norm_y3**4)*500)
        #plt.xlim([90, 500])
        plt.ylim([0, 16])
        plt.gray()
        plt.axis('off')
        ax3.set_axis_off()
        plt.tight_layout()
        fig3.savefig('Temp/Ch3fft.png', bbox_inches='tight', pad_inches=0)

        fig4 = plt.figure()
        ax4 = plt.Axes(fig4, [0., 0., 1., 1.])
        plt.scatter(xf, Norm_y4a, c=4**abs(Norm_y4), s=abs(Norm_y4**4)*500)
        #plt.xlim([90, 500])
        plt.ylim([0, 16])
        plt.gray()
        plt.axis('off')
        ax4.set_axis_off()
        plt.tight_layout()
        fig4.savefig('Temp/Ch4fft.png', bbox_inches='tight', pad_inches=0)

        if i in Training:
            nameTrain = str(countTrain)
            countTrain += 1
            FileName = FolderSTFTTraining + "/" + nameTrain + '.png'
            print(FileName)
            #ProcessConcat('Temp/STFTTestingFigureCh1.png', 'Temp/STFTTestingFigureCh2.png', 'Temp/STFTTestingFigureCh3.png', 'Temp/STFTTestingFigureCh4.png', FileName)
            ProcessConcat('Temp/Ch1fft.png', 'Temp/Ch2fft.png','Temp/Ch3fft.png', 'Temp/Ch4fft.png', FileName)

        if i in Validation:
            nameVal = str(countVal)
            countVal += 1
            FileName = FolderValTesting + "/" + nameVal + '.png'
            print(FileName)
            # ProcessConcat('Temp/STFTTestingFigureCh1.png', 'Temp/STFTTestingFigureCh2.png', 'Temp/STFTTestingFigureCh3.png', 'Temp/STFTTestingFigureCh4.png', FileName)
            ProcessConcat('Temp/Ch1fft.png', 'Temp/Ch2fft.png', 'Temp/Ch3fft.png', 'Temp/Ch4fft.png', FileName)

        if i in Testing:
            nameTest = str(countTest)
            countTest += 1
            FileName = FolderSTFTTesting + "/" + nameTest + '.png'
            print(FileName)
            #ProcessConcat('Temp/STFTTestingFigureCh1.png', 'Temp/STFTTestingFigureCh2.png', 'Temp/STFTTestingFigureCh3.png', 'Temp/STFTTestingFigureCh4.png', FileName)
            ProcessConcat('Temp/Ch1fft.png', 'Temp/Ch2fft.png', 'Temp/Ch3fft.png', 'Temp/Ch4fft.png', FileName)

        os.remove("Temp/STFTTestingFigureCh1.png")
        os.remove("Temp/STFTTestingFigureCh2.png")
        os.remove("Temp/STFTTestingFigureCh3.png")
        os.remove("Temp/STFTTestingFigureCh4.png")
        os.remove('Temp/Ch1fft.png')
        os.remove('Temp/Ch2fft.png')
        os.remove('Temp/Ch3fft.png')
        os.remove('Temp/Ch4fft.png')

        ####
        # os.remove("Temp/ScattTestingFigureCh1.png")
        # os.remove("Temp/ScattTestingFigureCh2.png")
        # os.remove("Temp/ScattTestingFigureCh3.png")
        # os.remove("Temp/ScattTestingFigureCh4.png")
        #######
        # from PIL import Image
        # def ProcessIm(Im1, Im2, fileName):
        #     image1 = Image.open(Im1)
        #     image1 = image1.rotate(90)
        #
        #     image2 = Image.open(Im2)
        #     image1_size = image1.size
        #     new_image = Image.new('RGB', (2 * image1_size[0], image1_size[1]), (250, 250, 250))
        #     new_image.paste(image1, (0, 0))
        #     new_image.paste(image2, (image1_size[0], 0))
        #     new_image.save(fileName)
        #
        # if i in Training:
        #     nameTrain = str(countTrain)
        #     countTrain += 1
        #     FileName = FolderSTFTTraining + "/" + nameTrain + '.png'
        #     print(FileName)
        #     ProcessIm('STFTTestingFigure.png', 'ScattTestingFigure.png', FileName)
        #
        # else:
        #     nameTest = str(countTest)
        #     countTest += 1
        #     FileName = FolderSTFTTesting + "/" + nameTest + '.png'
        #     print(FileName)
        #     ProcessIm('STFTTestingFigure.png', 'ScattTestingFigure.png', FileName)
        #
        # os.remove("STFTTestingFigure.png")
        # os.remove("ScattTestingFigure.png")


def Classifier(x):
    # classification = ""
    # for i in x:
    #     if str.isdigit(i):
    #         classification = classification + i
    classification = x

    FolderSTFTTraining = "Figure/Training/"+ classification
    FolderSTFTTesting = "Figure/Testing/"+ classification
    FolderValidation = "Figure/Validation/" + classification

    if isdir(FolderSTFTTraining):
        print("Folders Already Excits!")
    else:
        os.mkdir(FolderSTFTTraining)
        os.mkdir(FolderSTFTTesting)
        os.mkdir(FolderValidation)
    print("Folder for", classification, "made!")
    return [FolderSTFTTraining, FolderSTFTTesting, FolderValidation]


def TestingPreprocessing(data):
    time = data[75:len(data)-1, 1]
    Ch1 = data[75:len(data)-1, 2]
    Ch2 = data[75:len(data) - 1, 3]
    Ch3 = data[75:len(data) - 1, 4]
    Ch4 = data[75:len(data) - 1, 5]
    Fs = 1000

    detenCh1 = sig.detrend(Ch1)
    detenCh2 = sig.detrend(Ch2)
    detenCh3 = sig.detrend(Ch3)
    detenCh4 = sig.detrend(Ch4)


    # filter = sig.butter(2, [95, 500], 'bandpass', fs=1200, output='sos')
    # corrCh1 = sig.sosfilt(filter, detenCh1)
    corrCh1 = (detenCh1*5)/1023
    #corrCh2 = sig.sosfilt(filter, detenCh2)
    corrCh2 = (detenCh2*5)/1023
    #corrCh3 = sig.sosfilt(filter, detenCh3)
    corrCh3 = (detenCh3*5)/1023
    #corrCh4 = sig.sosfilt(filter, detenCh4)
    corrCh4 = (detenCh4 * 5) / 1023

    maxV1 = max(detenCh1)
    normV1 = detenCh1 / maxV1
    maxV2 = max(detenCh2)
    normV2 = detenCh2 / maxV2
    maxV3 = max(detenCh3)
    normV3 = detenCh3 / maxV3
    maxV4 = max(detenCh4)
    normV4 = detenCh4 / maxV4

    Ch1pp = normV1
    Ch2pp = normV2
    Ch3pp = normV3
    Ch4pp = normV4

    ## Channel 1
    fig0 = plt.figure()
    ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
    plt.style.use('dark_background')
    plt.scatter(time, Ch1pp, c=abs(Ch1pp * Ch1pp), s=abs(Ch1pp))
    plt.gray()
    plt.axis('off')
    ax0.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig0.savefig('ScattTestingFigureCh1.png', bbox_inches='tight', pad_inches=0)

    f1, t1, Zxx1 = sig.stft(Ch1pp, Fs, nperseg=1000)
    fig1 = plt.figure(frameon=False)
    ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
    plt.pcolormesh(t1, f1, np.abs(Zxx1), shading='gouraud', cmap='gray')
    plt.axis('off')
    plt.ylim([90, 500])
    ax1.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig1.savefig('STFTTestingFigureCh1.png', bbox_inches='tight', pad_inches=0)

    ## Channel 2
    fig0 = plt.figure()
    ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
    plt.style.use('dark_background')
    plt.scatter(time, Ch2pp, c=abs(Ch2pp * Ch2pp), s=abs(Ch2pp))
    plt.gray()
    plt.axis('off')
    ax0.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig0.savefig('ScattTestingFigureCh2.png', bbox_inches='tight', pad_inches=0)

    f2, t2, Zxx2 = sig.stft(Ch2pp, Fs, nperseg=1000)
    fig1 = plt.figure(frameon=False)
    ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
    plt.pcolormesh(t2, f2, np.abs(Zxx2), shading='gouraud', cmap='gray')
    plt.axis('off')
    plt.ylim([90, 500])
    ax1.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig1.savefig('STFTTestingFigureCh2.png', bbox_inches='tight', pad_inches=0)

    ##Channel 3
    fig0 = plt.figure()
    ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
    plt.style.use('dark_background')
    plt.scatter(time, Ch3pp, c=abs(Ch3pp * Ch3pp), s=abs(Ch3pp))
    plt.gray()
    plt.axis('off')
    ax0.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig0.savefig('ScattTestingFigureCh3.png', bbox_inches='tight', pad_inches=0)

    f3, t3, Zxx3 = sig.stft(Ch3pp, Fs, nperseg=1000)
    fig1 = plt.figure(frameon=False)
    ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
    plt.pcolormesh(t3, f3, np.abs(Zxx3), shading='gouraud', cmap='gray')
    plt.axis('off')
    plt.ylim([90, 500])
    ax1.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig1.savefig('STFTTestingFigureCh3.png', bbox_inches='tight', pad_inches=0)

    ## Channel 4
    fig0 = plt.figure()
    ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
    plt.style.use('dark_background')
    plt.scatter(time, Ch4pp, c=abs(Ch4pp * Ch4pp), s=abs(Ch4pp))
    plt.gray()
    plt.axis('off')
    ax0.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig0.savefig('ScattTestingFigureCh4.png', bbox_inches='tight', pad_inches=0)

    f4, t4, Zxx4 = sig.stft(Ch4pp, Fs, nperseg=1000)
    fig1 = plt.figure(frameon=False)
    ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
    plt.pcolormesh(t4, f4, np.abs(Zxx4), shading='gouraud', cmap='gray')
    plt.axis('off')
    plt.ylim([90, 500])
    ax1.set_axis_off()
    plt.tight_layout()
    plt.show()
    fig1.savefig('STFTTestingFigureCh4.png', bbox_inches='tight', pad_inches=0)

#
#
# def PreprocessingMeth2(data, FolderSTFTTraining, FolderSTFTTesting, dataFileName):
#     time = data[0:len(data)-4000, 1]
#     voltage = data[0:len(data)-4000, 2]
#     Fs = 4000
#
#     TrainingDirectory = [f for f in listdir(FolderSTFTTraining)]
#     TestDirectory = [f for f in listdir(FolderSTFTTesting)]
#     detenV = sig.detrend(voltage)
#
#     filter = sig.butter(2, [95, 1500], 'bandpass', fs=4000, output='sos')
#     corrVoltage = sig.sosfilt(filter, detenV)
#     corrVoltage = (corrVoltage*5)/1023
#
#     maxV = max(corrVoltage)
#     normV = corrVoltage/maxV
#
#     countTrain = int(len(TrainingDirectory))
#     countTest = int(len(TestDirectory))
#
#     fig0 = plt.figure()
#     ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
#     plt.style.use('dark_background')
#     plt.scatter(time, normV, c=abs(normV * normV), s=abs(normV))
#     plt.gray()
#     plt.axis('off')
#     ax0.set_axis_off()
#     plt.tight_layout()
#     plt.show()
#     fig0.savefig('ScattTestingFigure.png', bbox_inches='tight', pad_inches=0)
#
#     f1, t1, Zxx1 = sig.stft(normV, Fs, nperseg=1000)
#     fig1 = plt.figure(frameon=False)
#     ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
#     plt.pcolormesh(t1, f1, np.abs(Zxx1), shading='gouraud', cmap='gray')
#     plt.axis('off')
#     plt.ylim([90, 500])
#     ax1.set_axis_off()
#     plt.tight_layout()
#     plt.show()
#     fig1.savefig('STFTTestingFigure.png', bbox_inches='tight', pad_inches=0)
#
#     Training = [1, 3, 4]
#     # from Image_merge import merge_images
#     # i = randint(1, 4)
#     # if i in Training:
#     #     nameTrain = str(countTrain)
#     #     countTrain += 1
#     #     FileName = FolderSTFTTraining + "/" + nameTrain
#     #     # fig1.savefig(FileName, bbox_inches='tight', pad_inches=0)
#     #     # merge_images('Ch1.png', nameTrain, FolderSTFTTraining)
#     #     merge_images('STFTTestingFigure.png', 'ScattTestingFigure.png', 'ScattTestingFigure.png',
#     #                  'STFTTestingFigure.png', nameTrain, FolderSTFTTraining)
#     # else:
#     #     nameTest = str(countTest)
#     #     countTest += 1
#     #     FileName = FolderSTFTTesting + "/" + nameTest
#     #     # fig1.savefig(FileName, bbox_inches='tight', pad_inches=0)
#     #     # ('Ch1.png', nameTest, FolderSTFTTesting)
#     #     merge_images('STFTTestingFigure.png', 'ScattTestingFigure.png', 'ScattTestingFigure.png',
#     #                  'STFTTestingFigure.png', nameTest, FolderSTFTTesting)
#
#
#     i = randint(1, 4)
#     if i in Training:
#         nameTrain = str(countTrain)
#         countTrain += 1
#         FileName = FolderSTFTTraining + "/" + nameTrain + '.png'
#         print(FileName)
#         ProcessIm('STFTTestingFigure.png', 'ScattTestingFigure.png', FileName)
#
#     else:
#         nameTest = str(countTest)
#         countTest += 1
#         FileName = FolderSTFTTesting + "/" + nameTest + '.png'
#         print(FileName)
#         ProcessIm('STFTTestingFigure.png', 'ScattTestingFigure.png', FileName)
#
#     os.remove("STFTTestingFigure.png")
#     os.remove("ScattTestingFigure.png")

def figure_makerMeth2(data, FolderSTFTTraining, FolderSTFTTesting, FolderValTesting, FileName):
    ChannelNum = len(data[0]) - 1
    time = data[150:len(data)-1, 1]
    Ch1 = data[150:len(data)-1, 2]
    Ch2 = data[150:len(data) - 1, 3]
    Ch3 = data[150:len(data) - 1, 4]
    Ch4 = data[150:len(data) - 1, 5]
    Fs = 4000/3.5

    detenCh1 = sig.detrend(Ch1)
    detenCh2 = sig.detrend(Ch2)
    detenCh3 = sig.detrend(Ch3)
    detenCh4 = sig.detrend(Ch4)


    filter = sig.butter(2, [70,550], 'bandpass', fs=Fs, output='sos')
    corrCh1 = sig.sosfilt(filter, detenCh1)
    corrCh1 = (corrCh1*5)/1023
    corrCh2 = sig.sosfilt(filter, detenCh2)
    corrCh2 = (corrCh2*5)/1023
    corrCh3 = sig.sosfilt(filter, detenCh3)
    corrCh3 = (corrCh3*5)/1023
    corrCh4 = sig.sosfilt(filter, detenCh4)
    corrCh4 = (corrCh4*5)/1023

    TrainingDirectory = [f for f in listdir(FolderSTFTTraining)]
    TestDirectory = [f for f in listdir(FolderSTFTTesting)]
    ValidationDirectory = [f for f in listdir(FolderValTesting)]


    countTrain = int(len(TrainingDirectory))
    countTest = int(len(TestDirectory))
    countVal = int(len(ValidationDirectory))

    maxV1 = max(corrCh1)
    normV1 = corrCh1 / maxV1
    maxV2 = max(corrCh2)
    normV2 = corrCh2 / maxV2
    maxV3 = max(corrCh3)
    normV3 = corrCh3 / maxV3
    maxV4 = max(corrCh4)
    normV4 = corrCh4 / maxV4


    Num = random.randint(0, 10)
    seperationPoints = SepWithSTFT(normV1, normV2, normV3, normV4, time, Fs)
    if len(seperationPoints)>0:
        if len(seperationPoints) <= 2:
            # Ch1pp = normV1[int(seperationPoints[0]):int(seperationPoints[1])]
            # Ch2pp = normV2[int(seperationPoints[0]):int(seperationPoints[1])]
            # Ch3pp = normV3[int(seperationPoints[0]):int(seperationPoints[1])]
            # Ch4pp = normV4[int(seperationPoints[0]):int(seperationPoints[1])]
            Ch1pp = normV1[int(seperationPoints[0]):int(seperationPoints[0]+Fs+10)]
            Ch2pp = normV2[int(seperationPoints[0]):int(seperationPoints[0]+Fs+10)]
            Ch3pp = normV3[int(seperationPoints[0]):int(seperationPoints[0]+Fs+10)]
            Ch4pp = normV4[int(seperationPoints[0]):int(seperationPoints[0]+Fs+10)]
        if len(seperationPoints) > 2:
            # Ch1pp = normV1[int(seperationPoints[1]):int(seperationPoints[2])]
            # Ch2pp = normV2[int(seperationPoints[1]):int(seperationPoints[2])]
            # Ch3pp = normV3[int(seperationPoints[1]):int(seperationPoints[2])]
            # Ch4pp = normV4[int(seperationPoints[1]):int(seperationPoints[2])]
            Ch1pp = normV1[int(seperationPoints[1]):int(seperationPoints[1]+Fs+10)]
            Ch2pp = normV2[int(seperationPoints[1]):int(seperationPoints[1]+Fs+10)]
            Ch3pp = normV3[int(seperationPoints[1]):int(seperationPoints[1]+Fs+10)]
            Ch4pp = normV4[int(seperationPoints[1]):int(seperationPoints[1]+Fs+10)]
        #################################################### STFT Plots##################################################
        ## Channel 1
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch1pp, c=abs(Ch1pp*Ch1pp), s=abs(Ch1pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh1.png', bbox_inches='tight', pad_inches=0)

        f1, t1, Zxx1 = sig.stft(Ch1pp, Fs, nperseg=75)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t1, f1, np.abs(Zxx1), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([70, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh1.png', bbox_inches='tight', pad_inches=0)

        ## Channel 2
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch2pp, c=abs(Ch2pp*Ch2pp), s=abs(Ch2pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh2.png', bbox_inches='tight', pad_inches=0)

        f2, t2, Zxx2 = sig.stft(Ch2pp, Fs, nperseg=75)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t2, f2, np.abs(Zxx2), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([70, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh2.png', bbox_inches='tight', pad_inches=0)

        ##Channel 3
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch3pp, c=abs(Ch3pp*Ch3pp), s=abs(Ch3pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh3.png', bbox_inches='tight', pad_inches=0)

        f3, t3, Zxx3 = sig.stft(Ch3pp, Fs, nperseg=75)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t3, f3, np.abs(Zxx3), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([70, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh3.png', bbox_inches='tight', pad_inches=0)

        ## Channel 4
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch4pp, c=abs(Ch4pp*Ch4pp), s=abs(Ch4pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh4.png', bbox_inches='tight', pad_inches=0)

        f4, t4, Zxx4 = sig.stft(Ch4pp, Fs, nperseg=75)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t4, f4, np.abs(Zxx4), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([90, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh4.png', bbox_inches='tight', pad_inches=0)
        #################################################### FFT Plots##################################################
        # #plt.style.use('dark_background')
        # y1 = fft(Ch1pp)
        # y2 = fft(Ch2pp)
        # y3 = fft(Ch3pp)
        # y4 = fft(Ch4pp)
        #
        #
        # y1a = y1[80: 550]
        # max_value1 = max(abs(y1a))
        # Norm_y1 = abs(y1a) / 15 # max_value1
        # Norm_y1a = abs(y1a)
        #
        # y2a = y2[80: 550]
        # max_value2 = max(abs(y2a))
        # Norm_y2 = abs(y2a) / 15 # max_value2
        # Norm_y2a = abs(y2a)
        #
        # y3a = y3[80: 550]
        # max_value3 = max(abs(y3a))
        # Norm_y3 = abs(y3a) / 15 # max_value3
        # Norm_y3a = abs(y3a)
        #
        # y4a = y4[80: 550]
        # max_value4 = max(abs(y4a))
        # Norm_y4 = abs(y4a) / 15 # max_value4
        # Norm_y4a = abs(y4a)
        #
        # N = len(y4a)
        # xf = fftfreq(N, 1/Fs)
        #
        # fig1 = plt.figure()
        # ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        # plt.scatter(xf, Norm_y1a, c=4**abs(Norm_y1), s=abs(Norm_y1**4)*500)
        # #plt.xlim([90, 500])
        # plt.ylim([0, 16])
        # plt.gray()
        # plt.axis('off')
        # ax1.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig1.savefig('Temp/Ch1fft.png', bbox_inches='tight', pad_inches=0)
        #
        # fig2 = plt.figure()
        # ax2 = plt.Axes(fig2, [0., 0., 1., 1.])
        # plt.scatter(xf, Norm_y2a, c=4**abs(Norm_y2), s=abs(Norm_y2**4)*500)
        # #plt.xlim([90, 500])
        # plt.ylim([0, 16])
        # plt.gray()
        # plt.axis('off')
        # ax2.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig2.savefig('Temp/Ch2fft.png', bbox_inches='tight', pad_inches=0)
        #
        # fig3 = plt.figure()
        # ax3 = plt.Axes(fig3, [0., 0., 1., 1.])
        # plt.scatter(xf, Norm_y3a, c=4**abs(Norm_y3), s=abs(Norm_y3**4)*500)
        # #plt.xlim([90, 500])
        # plt.ylim([0, 16])
        # plt.gray()
        # plt.axis('off')
        # ax3.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig3.savefig('Temp/Ch3fft.png', bbox_inches='tight', pad_inches=0)
        #
        # fig4 = plt.figure()
        # ax4 = plt.Axes(fig4, [0., 0., 1., 1.])
        # plt.scatter(xf, Norm_y4a, c=4**abs(Norm_y4), s=abs(Norm_y4**4)*500)
        # #plt.xlim([90, 500])
        # plt.ylim([0, 16])
        # plt.gray()
        # plt.axis('off')
        # ax4.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig4.savefig('Temp/Ch4fft.png', bbox_inches='tight', pad_inches=0)

        if Num in range(0, 7):
            nameTrain = str(countTrain)
            countTrain += 1
            FileName = FolderSTFTTraining + "/" + nameTrain + '.png'
            print(FileName)
            ProcessConcat('Temp/STFTTestingFigureCh1.png', 'Temp/STFTTestingFigureCh2.png', 'Temp/STFTTestingFigureCh3.png', 'Temp/STFTTestingFigureCh4.png', FileName)
            # ProcessConcat('Temp/Ch1fft.png', 'Temp/Ch2fft.png','Temp/Ch3fft.png', 'Temp/Ch4fft.png', FileName)

        if Num in range(7, 9):
            nameVal = str(countVal)
            countVal += 1
            FileName = FolderValTesting + "/" + nameVal + '.png'
            print(FileName)
            ProcessConcat('Temp/STFTTestingFigureCh1.png', 'Temp/STFTTestingFigureCh2.png', 'Temp/STFTTestingFigureCh3.png', 'Temp/STFTTestingFigureCh4.png', FileName)
            # ProcessConcat('Temp/Ch1fft.png', 'Temp/Ch2fft.png', 'Temp/Ch3fft.png', 'Temp/Ch4fft.png', FileName)

        if Num in range(9, 11 ):
            nameTest = str(countTest)
            countTest += 1
            FileName = FolderSTFTTesting + "/" + nameTest + '.png'
            print(FileName)
            ProcessConcat('Temp/STFTTestingFigureCh1.png', 'Temp/STFTTestingFigureCh2.png', 'Temp/STFTTestingFigureCh3.png', 'Temp/STFTTestingFigureCh4.png', FileName)
            # ProcessConcat('Temp/Ch1fft.png', 'Temp/Ch2fft.png', 'Temp/Ch3fft.png', 'Temp/Ch4fft.png', FileName)

        os.remove("Temp/STFTTestingFigureCh1.png")
        os.remove("Temp/STFTTestingFigureCh2.png")
        os.remove("Temp/STFTTestingFigureCh3.png")
        os.remove("Temp/STFTTestingFigureCh4.png")
        # os.remove('Temp/Ch1fft.png')
        # os.remove('Temp/Ch2fft.png')
        # os.remove('Temp/Ch3fft.png')
        # os.remove('Temp/Ch4fft.png')


def figure_makerTesting(data):
    time = data[150:len(data)-1, 1]
    Ch1 = data[150:len(data)-1, 2]
    Ch2 = data[150:len(data) - 1, 3]
    Ch3 = data[150:len(data) - 1, 4]
    Ch4 = data[150:len(data) - 1, 5]
    Fs = 4000/3.5

    detenCh1 = sig.detrend(Ch1)
    detenCh2 = sig.detrend(Ch2)
    detenCh3 = sig.detrend(Ch3)
    detenCh4 = sig.detrend(Ch4)


    filter = sig.butter(2, [70,550], 'bandpass', fs=Fs, output='sos')
    corrCh1 = sig.sosfilt(filter, detenCh1)
    corrCh1 = (corrCh1*5)/1023
    corrCh2 = sig.sosfilt(filter, detenCh2)
    corrCh2 = (corrCh2*5)/1023
    corrCh3 = sig.sosfilt(filter, detenCh3)
    corrCh3 = (corrCh3*5)/1023
    corrCh4 = sig.sosfilt(filter, detenCh4)
    corrCh4 = (corrCh4*5)/1023


    maxV1 = max(corrCh1)
    normV1 = corrCh1 / maxV1
    maxV2 = max(corrCh2)
    normV2 = corrCh2 / maxV2
    maxV3 = max(corrCh3)
    normV3 = corrCh3 / maxV3
    maxV4 = max(corrCh4)
    normV4 = corrCh4 / maxV4


    seperationPoints = SepWithSTFT(normV1, normV2, normV3, normV4, time, Fs)
    if len(seperationPoints) > 1:
        if len(seperationPoints) <= 2:
            # Ch1pp = normV1[int(seperationPoints[0]):int(seperationPoints[1])]
            # Ch2pp = normV2[int(seperationPoints[0]):int(seperationPoints[1])]
            # Ch3pp = normV3[int(seperationPoints[0]):int(seperationPoints[1])]
            # Ch4pp = normV4[int(seperationPoints[0]):int(seperationPoints[1])]
            Ch1pp = normV1[int(seperationPoints[0]):int(seperationPoints[0]+Fs+10)]
            Ch2pp = normV2[int(seperationPoints[0]):int(seperationPoints[0]+Fs+10)]
            Ch3pp = normV3[int(seperationPoints[0]):int(seperationPoints[0]+Fs+10)]
            Ch4pp = normV4[int(seperationPoints[0]):int(seperationPoints[0]+Fs+10)]
        if len(seperationPoints) > 2:
            # Ch1pp = normV1[int(seperationPoints[1]):int(seperationPoints[2])]
            # Ch2pp = normV2[int(seperationPoints[1]):int(seperationPoints[2])]
            # Ch3pp = normV3[int(seperationPoints[1]):int(seperationPoints[2])]
            # Ch4pp = normV4[int(seperationPoints[1]):int(seperationPoints[2])]
            Ch1pp = normV1[int(seperationPoints[1]):int(seperationPoints[1]+Fs+10)]
            Ch2pp = normV2[int(seperationPoints[1]):int(seperationPoints[1]+Fs+10)]
            Ch3pp = normV3[int(seperationPoints[1]):int(seperationPoints[1]+Fs+10)]
            Ch4pp = normV4[int(seperationPoints[1]):int(seperationPoints[1]+Fs+10)]
        #################################################### STFT Plots##################################################
        ## Channel 1
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch1pp, c=abs(Ch1pp*Ch1pp), s=abs(Ch1pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh1.png', bbox_inches='tight', pad_inches=0)

        f1, t1, Zxx1 = sig.stft(Ch1pp, Fs, nperseg=150)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t1, f1, np.abs(Zxx1), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([70, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        # plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh1.png', bbox_inches='tight', pad_inches=0)

        ## Channel 2
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch2pp, c=abs(Ch2pp*Ch2pp), s=abs(Ch2pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh2.png', bbox_inches='tight', pad_inches=0)

        f2, t2, Zxx2 = sig.stft(Ch2pp, Fs, nperseg=150)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t2, f2, np.abs(Zxx2), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([70, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        # plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh2.png', bbox_inches='tight', pad_inches=0)

        ##Channel 3
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch3pp, c=abs(Ch3pp*Ch3pp), s=abs(Ch3pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh3.png', bbox_inches='tight', pad_inches=0)

        f3, t3, Zxx3 = sig.stft(Ch3pp, Fs, nperseg=150)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t3, f3, np.abs(Zxx3), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([70, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        # plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh3.png', bbox_inches='tight', pad_inches=0)

        ## Channel 4
        # fig0 = plt.figure()
        # ax0 = plt.Axes(fig0, [0., 0., 1., 1.])
        # plt.style.use('dark_background')
        # plt.scatter(time[seperationPoints[i]:seperationPoints[i+1]], Ch4pp, c=abs(Ch4pp*Ch4pp), s=abs(Ch4pp))
        # plt.gray()
        # plt.axis('off')
        # ax0.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig0.savefig('Temp/ScattTestingFigureCh4.png', bbox_inches='tight', pad_inches=0)

        f4, t4, Zxx4 = sig.stft(Ch4pp, Fs, nperseg=150)
        fig1 = plt.figure(frameon=False)
        ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        plt.pcolormesh(t4, f4, np.abs(Zxx4), shading='gouraud', cmap='gray')
        plt.axis('off')
        plt.ylim([90, 500])
        ax1.set_axis_off()
        plt.tight_layout()
        # plt.show()
        fig1.savefig('Temp/STFTTestingFigureCh4.png', bbox_inches='tight', pad_inches=0)
        #################################################### FFT Plots##################################################
        # #plt.style.use('dark_background')
        # y1 = fft(Ch1pp)
        # y2 = fft(Ch2pp)
        # y3 = fft(Ch3pp)
        # y4 = fft(Ch4pp)
        #
        #
        # y1a = y1[80: 550]
        # max_value1 = max(abs(y1a))
        # Norm_y1 = abs(y1a) / 15 # max_value1
        # Norm_y1a = abs(y1a)
        #
        # y2a = y2[80: 550]
        # max_value2 = max(abs(y2a))
        # Norm_y2 = abs(y2a) / 15 # max_value2
        # Norm_y2a = abs(y2a)
        #
        # y3a = y3[80: 550]
        # max_value3 = max(abs(y3a))
        # Norm_y3 = abs(y3a) / 15 # max_value3
        # Norm_y3a = abs(y3a)
        #
        # y4a = y4[80: 550]
        # max_value4 = max(abs(y4a))
        # Norm_y4 = abs(y4a) / 15 # max_value4
        # Norm_y4a = abs(y4a)
        #
        # N = len(y4a)
        # xf = fftfreq(N, 1/Fs)
        #
        # fig1 = plt.figure()
        # ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
        # plt.scatter(xf, Norm_y1a, c=4**abs(Norm_y1), s=abs(Norm_y1**4)*500)
        # #plt.xlim([90, 500])
        # plt.ylim([0, 16])
        # plt.gray()
        # plt.axis('off')
        # ax1.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig1.savefig('Temp/Ch1fft.png', bbox_inches='tight', pad_inches=0)
        #
        # fig2 = plt.figure()
        # ax2 = plt.Axes(fig2, [0., 0., 1., 1.])
        # plt.scatter(xf, Norm_y2a, c=4**abs(Norm_y2), s=abs(Norm_y2**4)*500)
        # #plt.xlim([90, 500])
        # plt.ylim([0, 16])
        # plt.gray()
        # plt.axis('off')
        # ax2.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig2.savefig('Temp/Ch2fft.png', bbox_inches='tight', pad_inches=0)
        #
        # fig3 = plt.figure()
        # ax3 = plt.Axes(fig3, [0., 0., 1., 1.])
        # plt.scatter(xf, Norm_y3a, c=4**abs(Norm_y3), s=abs(Norm_y3**4)*500)
        # #plt.xlim([90, 500])
        # plt.ylim([0, 16])
        # plt.gray()
        # plt.axis('off')
        # ax3.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig3.savefig('Temp/Ch3fft.png', bbox_inches='tight', pad_inches=0)
        #
        # fig4 = plt.figure()
        # ax4 = plt.Axes(fig4, [0., 0., 1., 1.])
        # plt.scatter(xf, Norm_y4a, c=4**abs(Norm_y4), s=abs(Norm_y4**4)*500)
        # #plt.xlim([90, 500])
        # plt.ylim([0, 16])
        # plt.gray()
        # plt.axis('off')
        # ax4.set_axis_off()
        # plt.tight_layout()
        # plt.show()
        # fig4.savefig('Temp/Ch4fft.png', bbox_inches='tight', pad_inches=0)

        FileName = "Temp/Test.png"
        print(FileName)
        ProcessConcat('Temp/STFTTestingFigureCh1.png', 'Temp/STFTTestingFigureCh2.png', 'Temp/STFTTestingFigureCh3.png', 'Temp/STFTTestingFigureCh4.png', FileName)
        # ProcessConcat('Temp/Ch1fft.png', 'Temp/Ch2fft.png','Temp/Ch3fft.png', 'Temp/Ch4fft.png', FileName)
        os.remove("Temp/STFTTestingFigureCh1.png")
        os.remove("Temp/STFTTestingFigureCh2.png")
        os.remove("Temp/STFTTestingFigureCh3.png")
        os.remove("Temp/STFTTestingFigureCh4.png")
        # os.remove('Temp/Ch1fft.png')
        # os.remove('Temp/Ch2fft.png')
        # os.remove('Temp/Ch3fft.png')
        # os.remove('Temp/Ch4fft.png')

def figure_makerMeth2AutoSize(data, FolderSTFTTraining, FolderSTFTTesting, FolderValTesting, FileName):

    TrainingDirectory = [f for f in listdir(FolderSTFTTraining)]
    TestDirectory = [f for f in listdir(FolderSTFTTesting)]
    ValidationDirectory = [f for f in listdir(FolderValTesting)]

    countTrain = int(len(TrainingDirectory))
    countTest = int(len(TestDirectory))
    countVal = int(len(ValidationDirectory))

    data = np.delete(data, 0, 1)
    ChannelNum = len(data[0]) - 1
    print(ChannelNum)
    Fs = 4000 / 3.5
    time = data[200:len(data) - 1, 0]

    row = len(time)
    print(row)
    col = len(data[0]) - 1
    print(col)

    normData = np.empty(shape=(row, col))

    for ch in range(ChannelNum):
        Detrend = sig.detrend(data[200:len(data) - 1, ch + 1])
        # plt.plot(time, Detrend)
        # plt.ylabel('some numbers')
        # plt.show()
        filter = sig.butter(2, [70, 550], 'bandpass', fs=Fs, output='sos')
        corrdet = sig.sosfilt(filter, Detrend)
        corrdet = (corrdet * 5) / 1023

        maxVal = max(corrdet)
        normData[:, ch] = corrdet #/ maxVal

    # row = len(time)
    # print(row)
    # col = 9
    # print(col)
    #
    # normData1 = np.empty(shape=(row, col))
    # Channel1 = np.empty(shape=(row, col))
    # normData1[:, 0] = normData[:, 0]
    # normData1[:, 1] = normData[:, 1]
    # normData1[:, 2] = normData[:, 2]
    # normData1[:, 3] = normData[:, 3]
    # normData1[:, 4] = normData[:, 0] + normData[:, 1]
    # normData1[:, 5] = normData[:, 2] + normData[:, 3]
    # normData1[:, 6] = normData[:, 0] + normData[:, 2]
    # normData1[:, 7] = normData[:, 1] + normData[:, 3]
    # normData1[:, 8] = normData[:, 0] + normData[:, 2]+normData[:, 1] + normData[:, 3]
    # Channel1[:, 0] = normData[:, 0]
    #
    #
    # normData = np.empty(shape=(row, col))
    #
    # normData = normData1
    # ChannelNum = col

    Num = random.randint(0, 10)
    seperationPoints = SepWithSTFTAuto(normData, time, Fs)



    if len(seperationPoints)>1 and len(seperationPoints)<=5:
        for ch in range(ChannelNum):
            if len(seperationPoints) <= 2:
                Ch1pp = normData[int(seperationPoints[0]):int(seperationPoints[0]+Fs+10), ch]

            if len(seperationPoints) > 2:
                Ch1pp = normData[int(seperationPoints[1]):int(seperationPoints[1]+Fs+10), ch]

    ##################################################### STFT Plots##################################################

            f1, t1, Zxx1 = sig.stft(Ch1pp, Fs, nperseg=75)
            fig1 = plt.figure(frameon=False)
            ax1 = plt.Axes(fig1, [0., 0., 1., 1.])
            plt.pcolormesh(t1, f1, np.abs(Zxx1), shading='gouraud', cmap='gray')
            plt.axis('off')
            plt.ylim([70, 500])
            ax1.set_axis_off()
            plt.tight_layout()
            plt.show()
            Figname = 'Temp/STFTTestingFigure'+ str(ch) + '.png'
            fig1.savefig(Figname, bbox_inches='tight', pad_inches=0)


        if Num in range(0, 7):
            nameTrain = str(countTrain)
            countTrain += 1
            FileName = FolderSTFTTraining + "/" + nameTrain + '.png'
            Figures = os.listdir("Temp/")
            print(FileName)
            print(Figures)
            ProcessConcatAuto(Figures, FileName)

            # ProcessConcat('Temp/Ch1fft.png', 'Temp/Ch2fft.png','Temp/Ch3fft.png', 'Temp/Ch4fft.png', FileName)

        if Num in range(7, 9):
            nameVal = str(countVal)
            countVal += 1
            FileName = FolderValTesting + "/" + nameVal + '.png'
            Figures = os.listdir("Temp/")
            print(FileName)
            print(Figures)
            ProcessConcatAuto(Figures, FileName)


        if Num in range(9, 11):
            nameTest = str(countTest)
            countTest += 1
            FileName = FolderSTFTTesting + "/" + nameTest + '.png'
            Figures = os.listdir("Temp/")
            print(FileName)
            print(Figures)
            ProcessConcatAuto(Figures, FileName)

        for i in Figures:
            FigureName = "Temp/"+i
            os.remove(FigureName)

