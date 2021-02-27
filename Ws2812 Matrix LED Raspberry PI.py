
from RPi import GPIO
import time
#import neopixel
from rpi_ws281x import *
import random
import argparse
# LED strip configuration:

#pip3 install --force-reinstall adafruit-blinka
#sudo pip3 install rpi_ws281x
LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/$
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor$
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
randV1=0
randV2=0
randV3=0
randH1=0
randH2=0
randH3=0





lineH0=[0,31,32,63,64,95,96,127,128,159,160,191,192,223,224,255]
lineH1=[1,30,33,62,65,94,97,126,129,158,161,190,193,222,225,254]
lineH2=[2,29,34,61,66,93,98,125,130,157,162,189,194,221,226,253]
lineH3=[3,28,35,60,67,92,99,124,131,156,163,188,195,220,227,252]
lineH4=[4,27,36,59,68,91,100,123,132,155,164,187,196,219,228,251]
lineH5=[5,26,37,58,69,90,101,122,133,154,165,186,197,218,229,250]
lineH6=[6,25,38,57,70,89,102,121,134,153,166,185,198,217,230,249]
lineH7=[7,24,39,56,71,88,103,120,135,152,167,184,199,216,231,248]
lineH8=[8,23,40,55,72,87,104,119,136,151,168,183,200,215,232,247]
lineH9=[9,22,41,54,73,86,105,118,137,150,169,182,201,214,233,246]
lineH10=[10,21,42,53,74,85,106,117,138,149,170,181,202,213,234,245]
lineH11=[11,20,43,52,75,84,107,116,139,148,171,180,203,212,235,244]
lineH12=[12,19,44,51,76,83,108,115,140,147,172,179,204,211,236,243]
lineH13=[13,18,45,50,77,82,109,114,141,146,173,178,205,210,237,242]
lineH14=[14,17,46,49,78,81,110,113,142,145,174,177,206,209,238,241]
lineH15=[15,16,47,48,79,80,111,112,143,144,175,176,207,208,239,240]


lineV0=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lineV1=[31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16]
lineV2=[32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47]
lineV3=[63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48]
lineV4=[64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79]
lineV5=[95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80]
lineV6=[96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111]
lineV7=[127,126,125,124,123,122,121,120,119,118,117,116,115,114,113,112]
lineV8=[128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143]
lineV9=[159,158,157,156,155,154,153,152,151,150,149,148,147,146,145,144]
lineV10=[160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175]
lineV11=[191,190,189,188,187,186,185,184,183,182,181,180,179,178,177,176]
lineV12=[192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207]
lineV13=[223,222,221,220,219,218,217,216,215,214,213,212,211,210,209,208]
lineV14=[224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239]
lineV15=[255,254,253,252,251,250,249,248,247,246,245,244,243,242,241,240]
strip.begin()

rand1=random.randint(0,255)

for zod in range(0,200):
    randV1=random.randint(0,25)
    randV2=random.randint(0,25)
    randV3=random.randint(0,25)
    randH1=random.randint(0,25)
    randH2=random.randint(0,25)
    randH3=random.randint(0,25)
    for z in range (0,16):
            print(lineV4[z])
            strip.setPixelColorRGB(lineV15[15-z],randV1,randV2,randV3)
            strip.setPixelColorRGB(lineV14[z],randH1,randH2,randH3)
            strip.setPixelColorRGB(lineV13[15-z],randV1,randV2,randV3)
            strip.setPixelColorRGB(lineV12[z],randH1,randH2,randH3)
            strip.setPixelColorRGB(lineV11[15-z],randV1,randV2,randV3)
            strip.setPixelColorRGB(lineV10[z],randH1,randH2,randH3)
            strip.setPixelColorRGB(lineV9[15-z],randV1,randV2,randV3)
            strip.setPixelColorRGB(lineV8[z],randV1,randV2,randV3)
            strip.setPixelColorRGB(lineV7[15-z],randH1,randH2,randH3)
            strip.setPixelColorRGB(lineV6[z],randV1,randV2,randV3)
            strip.setPixelColorRGB(lineV5[15-z],randH1,randH2,randH3)
            strip.setPixelColorRGB(lineV4[z],randV1,randV2,randV3)
            strip.setPixelColorRGB(lineV3[15-z],randH1,randH2,randH3)
            strip.setPixelColorRGB(lineV2[z],randV1,randV2,randV3)
            strip.setPixelColorRGB(lineV1[15-z],randH1,randH2,randH3)
            strip.setPixelColorRGB(lineV0[z],randV1,randV2,randV3)
            strip.show()
            #time.sleep(.12)

    for z in range (0,16):
            print(lineV4[z])
            strip.setPixelColorRGB(lineH15[15-z],5,5,0)
            strip.setPixelColorRGB(lineH14[z],5,0,5)
            strip.setPixelColorRGB(lineH13[15-z],5,5,0)
            strip.setPixelColorRGB(lineH12[z],5,0,5)
            strip.setPixelColorRGB(lineH11[15-z],5,5,0)
            strip.setPixelColorRGB(lineH10[z],5,0,5)
            strip.setPixelColorRGB(lineH9[15-z],5,5,0)
            strip.setPixelColorRGB(lineH8[z],5,0,5)
            strip.setPixelColorRGB(lineH7[15-z],5,5,0)
            strip.setPixelColorRGB(lineH6[z],5,0,5)
            strip.setPixelColorRGB(lineH5[15-z],5,5,0)
            strip.setPixelColorRGB(lineH4[z],5,0,5)
            strip.setPixelColorRGB(lineH3[15-z],5,5,0)
            strip.setPixelColorRGB(lineH2[z],5,0,5)
            strip.setPixelColorRGB(lineH1[15-z],5,5,0)
            strip.setPixelColorRGB(lineH0[z],5,0,5)
            strip.show()
            #time.sleep(.012)
strip.setPixelColorRGB(0,255,0,0)
strip.setPixelColorRGB(255,0,255,0)
strip.show()

