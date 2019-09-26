import time
import sys
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(angle):


    duty = (1.44 + angle * (0.95/90)) / 20 * 100
    servo.ChangeDutyCycle(duty)
    
while(1):
    angle = input()
    setservo(angle)

