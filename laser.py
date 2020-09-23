# Import libraries
import RPi.GPIO as GPIO
import time

def move_servo(myServo1,myServo2):
 servo1.ChangeDutyCycle(2+(myServo1/18))
 servo2.ChangeDutyCycle(2+(myServo2/18))

#Clean things up at the end


print "start"
print "start function"
GPIO.setmode(GPIO.BOARD)
# Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50) # pin 12 for servo2
# Start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

count = 0.0
while (count < 80):
   print 'The count is:', count
   count = count + .4
   move_servo(1,count)
   time.sleep(.04)

count = 0.0
while (count < 80):
   print 'The count is:', count
   count = count + .5
   move_servo(count,80)
   time.sleep(.03)

count = 80
while (count != 1):
   print 'The count is:', count
   count = count - .5
   move_servo(count,80)
   time.sleep(.02)

count = 80
while (count > 1):
   print 'The count is:', count
   count = count -  .5
   move_servo(1,count)
   time.sleep(.03)




servo1.stop()
servo2.stop()
GPIO.cleanup()
time.sleep(.5)
print "Exiting"



