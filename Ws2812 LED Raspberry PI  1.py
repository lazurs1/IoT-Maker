
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
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
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


addLetters=[1,2,3,4,5,6,7,8,31,27,32,36,63,59,65,66,67,68,69,70,71,72,98,99,100,101,102,103,104,105,106,125,117,130,138,156,155,154,153,152,151,150,187,186,185,184,183,182,181,180,179,196,204,219,211,229,230,231,232,233,234,235]
addLetters2=[1,2,3,4,5,6,7,8,31,27,32,36,63,59,65,66,67,68,69,70,71,72,98,99,100,101,102,103,104,105,106,125,117,130,138,156,150,164,165,166,167,168,187,186,185,184,183,182,181,180,170,196,204,219,211,229,235,249,248,247,246,245]
addLetters3=[2,3,4,5,6,7,8,30,27,32,36,59,63,65,68,93,92,91,90,89,88,87,98,99,100,101,102,103,104,105,106,125,117,130,138,156,150,164,165,166,167,168,187,186,185,184,183,182,181,180,196,204,219,211,229,235,249,248,247,246,245]

boxInBox1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,31,16,32,34,35,36,37,38,39,40,41,42,43,44,45,47,63,61,50,48,64,66,68,69,70,71,72,73,74,75,77,79,95,93,91,84,82,80,96,98,100,102,103,104,105,107,109,111,127,125,123,121,118,116,114,112,128,130,132,134,137,139,141,143,159,157,155,153,152,151,152,150,148,146,144,160,162,164,171,173,175,191,189,187,186,185,184,183,182,181,180,178,176,192,194,205,207,223,221,220,219,218,217,216,215,214,213,212,211,210,208,224,239,255,254,253,252,251,250,249,248,247,246,245,244,243,242,241,240]
boxInBox2=[30,29,28,27,26,25,24,23,22,21,20,19,18,17,33,46,62,60,59,58,57,56,55,54,53,52,51,49,65,67,76,78,94,92,90,89,88,87,86,85,83,81,97,99,101,106,108,110,126,124,120,119,122,117,115,113,129,131,133,135,136,138,140,142,158,156,154,149,147,145,161,165,166,167,168,169,170,172,174,190,188,179,177,193,195,196,197,198,199,200,201,202,203,204,206,222,209,225,226,227,228,229,230,231,232,233,234,235,236,237,238]
#odd1=[127,128,126,129,125,130,124,131,100,155,5,26,37,58,69,90,165,186,197,218,229,250,102,153,120,135,119,136,105,150,85,75,51,45,17,15,150,170,180,204,210,238,240]
odd1=[127,128,126,129,125,130,124,131,100,155,5,26,37,58,69,90,165,186,197,218,229,250,102,153,120,135,119,136,105,150,85,75,51,45,17,15,150,170,180,204,210,238,240,118,137,117,138,116,139,115,140,114,141,113,142,112,143]
odd1x=[123,132,101,154,121,134]
odd1x1=[122,133]

fu=[0,1,2,3,4,5,8,9,31,29,21,32,43,44,45,46,47,53,64,65,66,67,68,69,90,96,97,98,99,100,101,104,105,106,107,108,109,110,111,119,112,128,129,130,131,132,133,136,143,159,154,151,150,149,148,147,146,145,144,183,182,181,180,179,178,177,176,192,193,194,195,196,197,207,221,222,208,225,228,232,233,234,235,236,237,238,239,255,250,72,73,160,165]

ship1=[7,8,25,22,37,42,59,56,55,52,67,70,73,76,93,90,85,82,97,100,103,104,107,110,127,124,121,118,115,112,182,131,134,137,140,143,158,155,152,151,148,145,162,165,170,173,188,185,182,179,196,199,200,203,218,213,230,233,248,247]

pattern1=[6,9,24,23,96,111,126,113,129,142,159,144,231,231,232,249,246]
pattern2=[0,15,30,17,34,45,60,51,68,75,90,85,102,105,120,119,135,136,153,150,165,170,187,180,195,204,221,210,225,238,255,240]
pattarn3=[2,13,28,19,32,36,43,47,62,58,53,49,66,70,73,77,92,88,87,83,100,107,122,117,133,138,155,148,163,167,168,172,189,185,182,178,193,197,202,206,223,219,212,208,227,236,253,242]
pattern4=[4,11,26,21,38,41,56,55,64,79,94,81,98,109,124,115,131,140,157,146,161,174,191,176,199,200,217,214,229,234,251,224]


slowTime=.15
strip.begin()

for zod in range(0,10):
    randV1=random.randint(0,10)
    randV2=random.randint(0,10)
    randV3=random.randint(0,10)
    randH1=random.randint(0,10)
    randH2=random.randint(0,10)
    randH3=random.randint(0,10)
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
#strip.setPixelColorRGB(0,255,0,0)
#strip.setPixelColorRGB(255,0,255,0)
strip.show()


for zz in range (0,256):
    strip.setPixelColorRGB(zz,0,0,0)
strip.show()
    

for loop1 in range (0,10):
    randC1=random.randint(0,5)
    randC2=random.randint(0,5)
    randC3=random.randint(0,5)
    

    for add1 in range(len(addLetters)):
        strip.setPixelColorRGB(addLetters[add1],randC3,randC2,randC1)
    strip.show()
    time.sleep(slowTime)
    for zz in range (0,256):
        strip.setPixelColorRGB(zz,0,0,0)
    #time.sleep(.005)
    strip.show()
    for add1 in range(len(addLetters2)):
        strip.setPixelColorRGB(addLetters2[add1],randC2,randC1,randC3)
    strip.show()
    time.sleep(slowTime)
    for zz in range (0,256):
        strip.setPixelColorRGB(zz,0,0,0)
    strip.show()
    #time.sleep(.005)
    for add1 in range(len(addLetters3)):
        strip.setPixelColorRGB(addLetters3[add1],randC1,randC2,randC3)
    strip.show()
    time.sleep(slowTime)
    for zz in range (0,256):
        strip.setPixelColorRGB(zz,0,0,0)
    strip.show()
    #time.sleep(.75)
    

#Square
for zz in range (0,len(boxInBox1)):
    strip.setPixelColorRGB(boxInBox1[zz],0,0,5)
    strip.show()
    time.sleep(.005)
    
for zz1 in range(len(boxInBox2)):
    strip.setPixelColorRGB(boxInBox2[zz1],0,25,0)
    strip.show()
    time.sleep(.005)
    
for zz in range (0,256):
    strip.setPixelColorRGB(zz,0,0,0)
strip.show()
    #time.sleep(.25)    
print(boxInBox2)

#Logo
for zz in range (0,len(odd1)):
    strip.setPixelColorRGB(odd1[zz],0,0,25)
    strip.show()
for zz in range (0,len(odd1x)):
    strip.setPixelColorRGB(odd1x[zz],0,25,0)
    strip.show()
for zz in range (0,len(odd1x1)):
    strip.setPixelColorRGB(odd1x1[zz],25,0,0)
    strip.show()

#fu 
#for zz in range (0,256):
#    strip.setPixelColorRGB(zz,0,0,0)
#    strip.show()
    #time.sleep(.25)
   
#for zz in range (0,len(fu)):
 #   strip.setPixelColorRGB(fu[zz],17,5,0)
  #  strip.show()


for zz in range (0,len(ship1)):
    strip.setPixelColorRGB(ship1[zz],25,0,0)
    strip.show()
    


for zz in range (0,256):
    strip.setPixelColorRGB(zz,0,0,0)
strip.show()

#pattary 1

for zod in range(0,9999):
    randV1=random.randint(0,25)
    randV2=random.randint(0,25)
    randV3=random.randint(0,25)
    randH1=random.randint(0,25)
    randH2=random.randint(0,25)
    randH3=random.randint(0,25)

    for zz in range (0,len(pattern1)):
        strip.setPixelColorRGB(pattern1[zz],randV1,randH1,randH2)
    strip.show()


    for zz in range (0,len(pattern2)):
        strip.setPixelColorRGB(pattern2[zz],randH3,randV2,randH1)
    strip.show()

    for zz in range (0,len(pattarn3)):
        strip.setPixelColorRGB(pattarn3[zz],randH3,randV2,randV3)
    strip.show()

    for zz in range (0,len(pattern4)):
        strip.setPixelColorRGB(pattern4[zz],randH3,randH2,randH1)
    strip.show()
    print(zod)
    time.sleep(.75)


