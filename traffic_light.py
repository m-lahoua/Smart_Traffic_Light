import RPi.GPIO as GPIO
import time
# Configuration des broches du
# Raspberry pi avec le schéma BCM
GPIO.setmode(GPIO.BCM)
# Définir les pins des capteurs PIR
sensor1 = 17
sensor2 = 27
# Défnir les pins des LEDs
led_GPIOs=[22,26,5,23,6,24]
red1=22
red2=26
yellow1=5
yellow2=23
green1=6
green2=24

# Définir les pins GPIO en pins GPIO.input et pins GPIO.output
GPIO.setup(sensor1, GPIO.IN)
print("motion sensor one in GPIO", sensor1, "is active.")
GPIO.setup(sensor2, GPIO.IN)
print("motion sensor two in GPIO", sensor2, "is active.")
for gpio in led_GPIOs:
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.output(gpio,GPIO.LOW)
    print("The led in GPIO", gpio, "is active.")
    GPIO.output(gpio,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(gpio,GPIO.LOW)
    time.sleep(0.5)

# La logique de détection des Infrarouges et les comportements 
try:
    while True:
        if GPIO.input(sensor1):
            print("motion has been detected in line 1.")
            GPIO.output(green2,GPIO.LOW)
            GPIO.output(yellow2,GPIO.HIGH)
            time.sleep(3)
            GPIO.output(yellow2,GPIO.LOW)
            GPIO.output(red2,GPIO.HIGH)
            GPIO.output(green1,GPIO.HIGH)   
            GPIO.output(red1,GPIO.LOW)
            GPIO.output(yellow1,GPIO.LOW)
            time.sleep(10)
            GPIO.output(led_GPIOs,GPIO.LOW)
        elif GPIO.input(sensor2):
            print("motion has been detected in line 2.")
            GPIO.output(green1,GPIO.LOW)
            GPIO.output(yellow1,GPIO.HIGH)
            time.sleep(3)
            GPIO.output(yellow1,GPIO.LOW)
            GPIO.output(red1,GPIO.HIGH)
            GPIO.output(green2,GPIO.HIGH)   
            GPIO.output(red2,GPIO.LOW)
            GPIO.output(yellow2,GPIO.LOW)
            time.sleep(10)
            GPIO.output(led_GPIOs,GPIO.LOW)
        else :
            print("no motion detected in both lanes")
            time.sleep(10)
except KeyboardInterrupt:
    GPIO.cleanup()