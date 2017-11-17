#import
import time
import RPi.GPIO as GPIO

#settings
GPIO.cleanup
GPIO.setwarnings(False)
y = 26 #PWM-PIN

#info
print("------------------------------------------------")
print("Software-PWM for stepper-motors by Marek Völckel")
print("----> Version 1.4 (WORKING)")
print("----> ")
print("------------------------------------------------")


print("-------")
print("Config")
print("-------")

#frequency input and limiter
a= float(input("Frequenz eingeben (1-1023):"))
if a > 1023:
    print("-----------------------------------------")
    print("Die Frequenz darf nicht über 1023 liegen!")
    print("-----------------------------------------")
    print("----> EXIT <----")
    exit()
#limiter
elif a < 1:
    print("---------------------------------------")
    print("Die Frequenz muss mindestens 1 betragen")
    print("---------------------------------------")
    print("----> EXIT <----")
    exit()


#DutyCile input and limiter
e = float(input("DutyCicle eingeben (1-100):"))
if e > 100:
    print("-----------------------------------------")
    print("Der DutyCicle darf nicht über 100% liegen!")
    print("-----------------------------------------")
    print("----> EXIT <----")
    exit()
#limiter
elif a < 1:
    print("------------------------------------------")
    print("Der DutyCicle muss mindestens 1% betragen!")
    print("------------------------------------------")
    print("----> EXIT <----")
    exit()


#Rotating time input and limiter
t = float(input("Drehzeit in Sekunden:"))
if t > 60:
    print("-----------------")
    print("Drehzeit zu hoch!")
    print("-----------------")
    print("----> EXIT <----")
    exit()
#limiter 
elif t < 2:
    print("----------------------------------------")
    print("Die Drehzeit muss mindestens 2 betragen!")
    print("----------------------------------------")
    print("----> EXIT <----")
    exit()




#Rotating process
GPIO.setmode(GPIO.BOARD)
GPIO.setup(y, GPIO.OUT) 
pwm = GPIO.PWM (y,a)  
pwm.start(e)           
time.sleep(t)
pwm.stop(0)
