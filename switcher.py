import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Push-button switch
GPIO.setup(18, GPIO.OUT)  # LED

try:
    while True:
        # Read the state of the push-button switch
        button_state = GPIO.input(17)

        # If the button is pressed (switch closed), turn on the LED
        if button_state == GPIO.LOW:
            GPIO.output(18, GPIO.HIGH)
            print("Button pressed. LED turned on.")
        else:
            GPIO.output(18, GPIO.LOW)
            print("Button released. LED turned off.")

        # Delay for a short period to debounce the switch
        time.sleep(0.1)



