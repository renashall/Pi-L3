import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import random

camera = PiCamera()

buttons = []
ledPin = 

picture_path = "picture/"
video_path = "video/"

picture = 0
video = 0

capturing = 
recording = 

filter_on = False
filters = ['negative', 'sketch', 'oilpaint','pastel', 'film', 'blur']

def setup():
    GPIO.setmode(GPIO.BCM)       # use BCM Numbering
    GPIO.setup(buttons, GPIO.IN)   # set the ledPin to OUTPUT mode
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    
    GPIO.add_event_detect(buttons[0], GPIO.RISING, callback=start_recording, bouncetime=200)
    GPIO.add_event_detect(buttons[1], GPIO.RISING, callback=stop_recording, bouncetime=200)
    GPIO.add_event_detect(buttons[2], GPIO.RISING, callback=take_picture, bouncetime=200)
    GPIO.add_event_detect(buttons[3], GPIO.RISING, callback=toggle_filter, bouncetime=200)
    
    #set the camera resolution
    #set the camera framerate
    #start the camera preview

def take_picture(channel):
    global picture, capturing
    
    if not capturing:
        capturing = True
        time.sleep(2)
        #take the picture
        picture += 1
        print("Picture saved.")
        capturing = False

def start_recording(channel):
    global recording, video
    
    if not recording:
        recording = True
        #start the recording
        video += 1
        GPIO.output(ledPin, GPIO.HIGH)

def stop_recording(channel):
    global recording
    
    if recording:
        recording = False
        #stop the recording
        GPIO.output(ledPin, GPIO.LOW)
        print("Video saved.")

def toggle_filter(channel):
    global filter_on
    
    if not filter_on:
        filter_on = True
        #set the effect to a random filter
    else:
        filter_on = False
        #turn off the filter

def destroy():
    if recording:
        camera.stop_recording()
    camera.stop_preview()
    GPIO.cleanup()                      # Release all GPIO
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        while(True):
            continue
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
