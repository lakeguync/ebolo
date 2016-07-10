#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
import random
import subprocess
import sys
import time

slogans = [
"I am e-bolo.",
"You must be an afficianado of western fashion.",
"I am stylish... but i am not, I am not... affordable. I am e-bolo.",
"e-bolo is function... fashion... tradition... and sophistication.",
"Make yourself great again... with e-bolo.",
"Hello. I am e-bolo ... The Future of Electronic Fashion.",
"Do you want to take a selfie... with e-bolo? Hash-tag... formal... western... wear.",
"You can look but you cannot... touch... my... e-bolo.",
"If it feels good... do it... with e-bolo."
]

boloPrefixes = [
"... ", 
"the... ", 
"an... ", 
"your... ", 
"America's Favorite... the... "
]

WHIPCRACK_WAV="whipcrack.wav"

DEVNULL = open(os.devnull, 'wb')
DEBUG_LOG = True

def debugLog(s = ""):
    if DEBUG_LOG:
        print("LOG: " + s)

def callCommand(command, shell=False):
    debugLog(" ".join(command))
    try:
        subprocess.call(command, stdout=DEVNULL, stderr=DEVNULL, shell=shell)
        #subprocess.call(command, stdout=DEVNULL, stderr=DEVNULL, timeout=20, shell=shell)
    except:
        e = sys.exc_info()[0]
        print( "Error: %s" % e )


def whipCrack():
    command = ['aplay', WHIPCRACK_WAV]
    callCommand(command)


def randomizedEspeak(sentence = ""):
    command = ['espeak', 
            ('-s %d' % (random.randrange(120) + 100)),
            ('-p %d' % (random.randrange(50) + 25)), 
            '\"%s\"' % sentence]
    callCommand(command)

def say(sentence = ""):
    randomizedEspeak(sentence)

def glitchyBolo():
    ebolo = "e-bolo"
    if random.randint(0,1):
        e = 1 + random.randrange(10)
        o = 1 + random.randrange(6)
        ebolo = ("e"*e)[:e] + " bol" + ("o"*o)[:o]
    return ebolo

def randomBoloPrefix():
    a = ""
    if random.randint(0,1):
        a = boloPrefixes[random.randrange(len(boloPrefixes))]
    return a

def randomSlogan():
    slogan = slogans[random.randrange(len(slogans))]
    debugLog("slogan = \"%s\"" % slogan)
    return slogan

def sayBolo(sentence):
    sentence = sentence.replace("e-bolo", randomBoloPrefix() + glitchyBolo())
    say(sentence)

def eboloButtonAction():
    debugLog('E-bolo Button Pressed')
    slogan = randomSlogan()
    sayBolo(slogan)
    whipCrack()

def testWithoutButton():
    while True:
        eboloButtonAction()
        time.sleep(1)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            eboloButtonAction()
            time.sleep(0.2)

main()

#testWithoutButton()


