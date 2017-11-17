import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT) #PWM PIN
pwm = GPIO.PWM (26,900)  # Frequenz: 2 Hertz
pwm.start(50)           # Duty-Cycle: 50%
time.sleep(10)

#pwm.ChangeFrequency(950)    #Frequenz: 900
#pwm.ChangeDutyCycle(50)           #DutyCycle: 50%

GPIO.cleanup

