#!/usr/bin/python

import uinput
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init case buttons
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # circle
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) # square
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # triangle
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # cross
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # side1
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # side2

# init events
events = (uinput.KEY_RED, uinput.KEY_GREEN, uinput.KEY_YELLOW, uinput.KEY_BLUE, uinput.KEY_VOLUMEUP, uinput.KEY_VOLUMEDOWN)

# init device
device = uinput.Device(events)

# init button vars
circle = False
square = False
triangle = False
cross = False
side1 = False
side2 = False

# main loop
while True:

  if (not circle) and (not GPIO.input(23)):
    circle = True
    device.emit(uinput.KEY_RED, 1)
  if circle and GPIO.input(23):
    circle = False
    device.emit(uinput.KEY_RED, 0)

  if (not square) and (not GPIO.input(22)):
    square = True
    device.emit(uinput.KEY_GREEN, 1)
  if square and GPIO.input(22):
    square = False
    device.emit(uinput.KEY_GREEN, 0)

  if (not triangle) and (not GPIO.input(24)):
    triangle = True
    device.emit(uinput.KEY_YELLOW, 1)
  if triangle and GPIO.input(24):
    triangle = False
    device.emit(uinput.KEY_YELLOW, 0)

  if (not cross) and (not GPIO.input(5)):
    cross = True
    device.emit(uinput.KEY_BLUE, 1)
  if cross and GPIO.input(5):
    cross = False
    device.emit(uinput.KEY_BLUE, 0)

  if (not side1) and (not GPIO.input(17)):
    side1 = True
    device.emit(uinput.KEY_VOLUMEUP, 1)
  if side1 and GPIO.input(17):
    side1 = False
    device.emit(uinput.KEY_VOLUMEUP, 0)

  if (not side2) and (not GPIO.input(4)):
    side2 = True
    device.emit(uinput.KEY_VOLUMEDOWN, 1) 
  if side2 and GPIO.input(4):
    side2 = False
    device.emit(uinput.KEY_VOLUMEDOWN, 0)

  time.sleep(0.05)
