#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, GPIO.PUD_DOWN)

GPIO.setup(27, GPIO.OUT, initial=0)

try:
    while True:
        if (GPIO.input(17) == 1):
            GPIO.output(27,1)
        else:
            GPIO.output(27,0)
            
except KeyboardInterrupt:
     GPIO.cleanup()
