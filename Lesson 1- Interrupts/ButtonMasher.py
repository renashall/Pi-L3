import RPi.GPIO as GPIO
import time

buttonPin = #enter the pin number
press = 0

def setup():
    GPIO.setmode(GPIO.BCM)           # use BCM Numbering
    GPIO.setup(buttonPin, GPIO.IN)   # set the buttonPin to INPUT mode
    GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=interrupt_func, bouncetime=30)

def interrupt_func(channel):
    global press
    press+=1

def loop():
    print("Get ready to mash the button for ten seconds.")
    time.sleep(1)
    print("Go")
    #sleep for the amount of time you want
    #tell the user how many times the pressed the button

def destroy():
    GPIO.remove_event_detect(buttonPin) #remove the interrupt
    GPIO.cleanup()                      # Release all GPIO
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
        destroy()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()