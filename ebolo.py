import RPi.GPIO as GPIO
import time
import random
import subprocess

slogans = [
"I am %s.",
"hello you naughty afficianado of western fashion. I am %s.",
"I am stylish... but i am not, I am not... affordable. I am %s.",
"%s is function... fashion... tradition... and sophistication.",
"Make yourself great again... with %s.",
"Hello. I am %s ... The Future of Wearable Fashion.",
"Do you want to take a selfie with %s? hashtag... formal... western... wear",
"You can look but you cannot... touch... my... %s",
"If it feels good... Do it... with %s"
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
	say(sentence % glitchybolo())
	
	
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



