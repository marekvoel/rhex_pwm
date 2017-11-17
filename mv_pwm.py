import time
import RPi.GPIO as GPIO
print("----------")
print("Software-PWM for stepper-motors by Marek Völckel")
print("----------")
'''Variables'''
a = (input("Frequenz eingeben:"))
e = (input("DutyCicle eingeben:"))
y = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(y, GPIO.OUT) #PWM PIN
pwm = GPIO.PWM (y,a)  # Frequenz: 2 Hertz
pwm.start(e)           # Duty-Cycle: 50%
time.sleep(10)

#pwm.ChangeFrequency(950)    #Frequenz: 900
#pwm.ChangeDutyCycle(50)           #DutyCycle: 50%

GPIO.cleanup