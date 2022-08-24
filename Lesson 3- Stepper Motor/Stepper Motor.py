import RPi.GPIO as GPIO
import time

motorPins = 

Halfstep = 

Fullstep = 

def setup():
    #setup the pins
    #output low
    
def moveOnePeriod(stepType, direction, ms):
    #set the sequence depending on the stepType

    for j in range(len(Sequence)):
        for i in range(len(motorPins)):
            #if the direction is CW
                #output the sequence
            #else
                #output the sequence in the reverse order
            
        if (ms < 3):
            ms = 3
        time.sleep(ms * .001)
        
def moveSteps(steps, stepType = 'Half', direction = 'CW', ms = 3):
    #use a for loop to call moveOnePeriod
    
def loop():
    while True:
        #rotate the motor cw
        #rotate the motor ccw
        
def destroy():
    GPIO.cleanup()
 
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
