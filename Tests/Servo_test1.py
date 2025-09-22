import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)  
servo_pin = 11             
GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin,50) #2ms pwm sighal
p.start(0)

try:
    while True:
        #sweep 0 to 180 deg
        for duty in range(3,13):
            p.ChangeDutyCycle(duty)
            sleep(0.1)
            
            
        
        #sweep back from 190
        for duty in range(12,2,-1):
            p.ChangeDutyCycle(duty)
            sleep(0.1)
            
except KeyboardInterrupt:
    #stop when ctrlSS+c
    p.stop()
    GPIO.cleanup()
    