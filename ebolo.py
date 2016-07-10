import RPi.GPIO as GPIO
import time
import random
import subprocess

slogans = [
"I am e-bolo.",
"Hello you afficianado of western fashion. I am e-bolo.",
"I am stylish... but i am not, I am not... affordable. I am e-bolo.",
"e-bolo is function... fashion... tradition... and sophistication.",
"Make yourself great again... with e-bolo.",
"Hello. I am e-bolo ... The Future of Wearable Fashion.",
"Do you want to take a selfie with e-bolo? Hash-tag... formal... western... wear",
"You can look but you cannot... touch... my... e-bolo",
"If it feels good... do it... with e-bolo"
]

def whipcrack():
    subprocess.call(['aplay', 'whipcrack.wav'])

def say(sentence = ""):
    subprocess.call(['espeak', 
                     ('-s %d' % (random.randrange(120) + 100)),
                     ('-p %d' % (random.randrange(50) + 25)), 
                     '\"%s\"' % sentence])

def glitchybolo():
    e = 1 + random.randrange(10)
    o = 1 + random.randrange(6)
    articles = ["...", "the...", "an...", "your...", "america's sweetheart... the..."]
    a = articles[random.randrange(len(articles))]
    return a + ("e"*e)[:e] + " bol" + ("o"*o)[:o]

def saybolo(sentence):
    if random.randint(0,1):
        sentence = sentence.replace("e-bolo", glitchybolo())
    say(sentence)

def testWithoutButton():
    while True:
        slogan = slogans[random.randrange(len(slogans))]
        print(slogan)
        saybolo(slogan)
        whipcrack()
        time.sleep(1)

def main():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	while True:
		input_state = GPIO.input(18)
		if input_state == False:
			slogan = slogans[random.randrange(len(slogans))]
			print(slogan)
			saybolo(slogan)
			whipcrack()
			print('Button Pressed')
			time.sleep(0.2)



main()


