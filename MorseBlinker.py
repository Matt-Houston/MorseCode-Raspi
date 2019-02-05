import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.OUT)

def Long():
	GPIO.output(18, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(18, GPIO.LOW)
	time.sleep(0.25)
	#Function for "long" blink of led
def Short():
	GPIO.output(18, GPIO.HIGH)
	time.sleep(0.125)
	GPIO.output(18, GPIO.LOW)
	time.sleep(0.25)
	#Function for "short" blink of led

lines = list()
file = open("MorseDecoder.txt", "r")

lines = file.readlines()

print("enter some text to be displayed in morse code: ") #getting user input
userinput=raw_input()

for letter in userinput: #getting each letter of user input - as a number
	letter.lower()
	number = ord(letter)-97
	for character in lines[number]:
		#interpret each letter using decoder
		if character == ".":
			Short()
		elif character == "-":
 			Long()
		else:
			pass

file.close()
GPIO.cleanup()

