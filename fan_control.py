#!/usr/bin/python

# MIT License

# Copyright (c) 2023 Naidan Demberel

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# from https://github.com/optimistiCli/pine64_fan/blob/master/pine64_fan.py

from time import sleep
import RPi.GPIO as GPIO

CPU_TEMP_PATH = '/sys/devices/virtual/thermal/thermal_zone0/temp'
PIN_NUMBER = 23  # GPIO23
TEMP_OFF = 40000 # 40C
TEMP_ON = 60000  # 60C

rotating = False

def fan_on():
    global rotating

    GPIO.output(PIN_NUMBER, True)
    rotating = True

def fan_off():
    global rotating

    GPIO.output(PIN_NUMBER, False)
    rotating = False

def should_stop(cpu_temp):
     if cpu_temp < TEMP_OFF:
          return True

     else:
	  return False

def should_start(cpu_temp):
     if cpu_temp > TEMP_ON:
          return True

     else:
	  return False

def run():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_NUMBER, GPIO.OUT)

    fan_off()

    while True:
        cpu_temp_file = open(CPU_TEMP_PATH)
	cpu_temp = int(cpu_temp_file.read())
	cpu_temp_file.close()

        if rotating and should_stop(cpu_temp):
             fan_off()
        elif not rotating and should_start(cpu_temp):
             fan_on()

        sleep(1)

if __name__ == "__main__":
	run()

