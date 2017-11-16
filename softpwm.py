import RPi.GPIO as gpio
gpio.setup(26,gpio.OUT) #PWM PIN
pwm = gpio.PWM (26, 2)  # Frequenz: 2 Hertz
pwm.start(50)           # Duty-Cycle: 50%
time.sleep(10)

pwm.ChangeFrequency(800)    #Frequenz: 800
pwm.DutyCycle(50)           #DutyCycle: 50%