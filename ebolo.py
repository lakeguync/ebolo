#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
import random
import subprocess
import sys
import time

slogans = [
"I am e-bolo, The Electronic... Bolo... Neck Tie.",
"I am e-bolo, The Electronic... Bolo... Neck Tie. You can wear me and I will make your life so much better.",
"I am e-bolo, The Electronic... Bolo... Neck Tie. I am HD, GPS, Why Fi, Four Gee, Three Gee, Five Gee, A-M F-M, A-C D-C, Blue tooth enabled and cable-ready.",
"Howdy",
"Gidd ee... up...",
"Wanted... Dead... or Alive... e-bolo",
"My cord is braided from the finest Italian leather",
"e-bolo will make you a pioneer of taste and sophistication",
"Neck... ties... are pass say",
"Be a horse of a different color... with e-bolo",
"Did you know I am the offical neck wear of Arizona?",
"It is time to hit the road. Battery is fully charged.",
"You must be an afficianado of western fashion.",
"I am stylish... but i am not, I am not... affordable. I am e-bolo.",
"e-bolo is function... fashion... tradition... and sophistication.",
"e-bolo is essential function... e bolo is the future... e bolo is fully-featured... e bolo is slightly flammable... e bolo is ultimate fashion... and ultimate sophistication. ",
"Make yourself great again... with e-bolo.",
"Make yourself great again... with e-bolo.",
"Hello. I am e-bolo ... The Future of Electronic Fashion.",
"Do you want to take a selfie... with e-bolo? Hash-tag... formal... western... wear.",
"Do you want to take a selfie... with e-bolo? Hash-tag... formal... western... wear.",
"You can look but you cannot... touch...  my... e bolo",
"If it feels good... do it... with e-bolo."
]


boloPrefixes = [
"the... ", 
"an... ", 
"your... ",
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
            ('-s %d' % (random.randrange(50) + 120)),
            ('-p %d' % (random.randrange(50) + 25)), 
            '\"%s\"' % sentence]
    callCommand(command)

def say(sentence = ""):
    randomizedEspeak(sentence)

def glitchyBolo():
    ebolo = "e-bolo"
    if random.randint(0,1):
        e = 1 + random.randrange(10)
        #o = 1 + random.randrange(6)
        #ebolo = ("e"*e)[:e] + " bol" + ("o"*o)[:o]
        o = 1 + random.randrange(6)
        ebolo = ("e"*e)[:e] + " bolo"
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
        time.sleep(0.05)

main()

#testWithoutButton()


