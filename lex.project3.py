#!/usr/bin/env python
# coding: utf-8

# In[3]:


import Adafruit_BBIO.GPIO as GPIO
import time

seg7_a = "P8_7"
seg7_b = "P8_8"
seg7_c = "P8_10"
seg7_d = "P8_12"
seg7_e = "P8_14"
seg7_f = "P8_16"
seg7_g = "P8_18"

count = 0

# initialize the pin as output
GPIO.setup(seg7_a, GPIO.out)
GPIO.setup(seg7_b, GPIO.out)
GPIO.setup(seg7_c, GPIO.out)
GPIO.setup(seg7_d, GPIO.out)
GPIO.setup(seg7_e, GPIO.out)
GPIO.setup(seg7_f, GPIO.out)
GPIO.setup(seg7_g, GPIO.out)


def seven_segment_function(x):
    if (x == 0):
        GPIO.output(seg7_a, GPIO.HIGH)
        GPIO.output(seg7_b, GPIO.HIGH)
        GPIO.output(seg7_c, GPIO.HIGH)
        GPIO.output(seg7_d, GPIO.HIGH)
        GPIO.output(seg7_e, GPIO.HIGH)
        GPIO.output(seg7_f, GPIO.HIGH)
        GPIO.output(seg7_g, GPIO.LOW)

    elif (x == 1):
        GPIO.output(seg7_a, GPIO.LOW)
        GPIO.output(seg7_b, GPIO.HIGH)
        GPIO.output(seg7_c, GPIO.HIGH)
        GPIO.output(seg7_d, GPIO.LOW)
        GPIO.output(seg7_e, GPIO.LOW)
        GPIO.output(seg7_f, GPIO.LOW)
        GPIO.output(seg7_g, GPIO.LOW)

    elif (x == 2):
        GPIO.output(seg7_a, GPIO.HIGH)
        GPIO.output(seg7_b, GPIO.HIGH)
        GPIO.output(seg7_c, GPIO.LOW)
        GPIO.output(seg7_d, GPIO.HIGH)
        GPIO.output(seg7_e, GPIO.HIGH)
        GPIO.output(seg7_f, GPIO.LOW)
        GPIO.output(seg7_g, GPIO.HIGH)

    elif (x == 3):
        GPIO.output(seg7_a, GPIO.HIGH)
        GPIO.output(seg7_b, GPIO.HIGH)
        GPIO.output(seg7_c, GPIO.HIGH)
        GPIO.output(seg7_d, GPIO.HIGH)
        GPIO.output(seg7_e, GPIO.LOW)
        GPIO.output(seg7_f, GPIO.LOW)
        GPIO.output(seg7_g, GPIO.HIGH)

    elif (x == 4):
        GPIO.output(seg7_a, GPIO.LOW)
        GPIO.output(seg7_b, GPIO.HIGH)
        GPIO.output(seg7_c, GPIO.HIGH)
        GPIO.output(seg7_d, GPIO.LOW)
        GPIO.output(seg7_e, GPIO.LOW)
        GPIO.output(seg7_f, GPIO.HIGH)
        GPIO.output(seg7_g, GPIO.HIGH)

    elif (x == 5):
        GPIO.output(seg7_a, GPIO.HIGH)
        GPIO.output(seg7_b, GPIO.LOW)
        GPIO.output(seg7_c, GPIO.HIGH)
        GPIO.output(seg7_d, GPIO.HIGH)
        GPIO.output(seg7_e, GPIO.LOW)
        GPIO.output(seg7_f, GPIO.HIGH)
        GPIO.output(seg7_g, GPIO.HIGH)

    elif (x == 6):
        GPIO.output(seg7_a, GPIO.HIGH)
        GPIO.output(seg7_b, GPIO.LOW)
        GPIO.output(seg7_c, GPIO.HIGH)
        GPIO.output(seg7_d, GPIO.HIGH)
        GPIO.output(seg7_e, GPIO.HIGH)
        GPIO.output(seg7_f, GPIO.HIGH)
        GPIO.output(seg7_g, GPIO.HIGH)

    elif (x == 7):
        GPIO.output(seg7_a, GPIO.HIGH)
        GPIO.output(seg7_b, GPIO.HIGH)
        GPIO.output(seg7_c, GPIO.HIGH)
        GPIO.output(seg7_d, GPIO.LOW)
        GPIO.output(seg7_e, GPIO.LOW)
        GPIO.output(seg7_f, GPIO.LOW)
        GPIO.output(seg7_g, GPIO.LOW)

    elif (x == 8):
        GPIO.output(seg7_a, GPIO.HIGH)
        GPIO.output(seg7_b, GPIO.HIGH)
        GPIO.output(seg7_c, GPIO.HIGH)
        GPIO.output(seg7_d, GPIO.HIGH)
        GPIO.output(seg7_e, GPIO.HIGH)
        GPIO.output(seg7_f, GPIO.HIGH)
        GPIO.output(seg7_g, GPIO.HIGH)

    elif (x == 9):
        GPIO.output(seg7_a, GPIO.HIGH)
        GPIO.output(seg7_b, GPIO.HIGH)
        GPIO.output(seg7_c, GPIO.HIGH)
        GPIO.output(seg7_d, GPIO.HIGH)
        GPIO.output(seg7_e, GPIO.LOW)
        GPIO.output(seg7_f, GPIO.HIGH)
        GPIO.output(seg7_g, GPIO.HIGH)

    else:
        GPIO.output(seg7_a, GPIO.LOW)
        GPIO.output(seg7_b, GPIO.LOW)
        GPIO.output(seg7_c, GPIO.LOW)
        GPIO.output(seg7_d, GPIO.LOW)
        GPIO.output(seg7_e, GPIO.LOW)
        GPIO.output(seg7_f, GPIO.LOW)
        GPIO.output(seg7_g, GPIO.LOW)


# LOOP FOREVER
while Ture:
    seven_segment_funtion(count)
    if (count < 10):
        count = count + 1
    else:
        count = 0

    print(count)
    time.sleep(1.0)

