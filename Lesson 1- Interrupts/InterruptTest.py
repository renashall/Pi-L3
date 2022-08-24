import RPi.GPIO as GPIO
import time

buttonPin = #set the button pin number
press = 0

def setup():
    GPIO.setmode(GPIO.BCM)           # use BCM Numbering
    GPIO.setup(buttonPin, GPIO.IN)   # set the button as an input
    #create the interrupt

def interrupt_func(channel):
    global press
    press+=1
    print("Button at pin", channel, "pressed", press, "times")

def loop():
    while(True):
        continue
    
def destroy():
    #remove the interrupt
    GPIO.cleanup()                      # Release all GPIO
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()