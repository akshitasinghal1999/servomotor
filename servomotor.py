import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)

p = GPIO.PWM(40,50)
p.start(7.5)

try:
    while True:
#        p.ChangeDutyCycle(7.5)
#        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        
except:
    print("Error")
    
finally:
    GPIO.cleanup((6,40))