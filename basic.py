# LED
from gpiozero import LED
from time import sleep
# Button
from gpiozero import Button

led = LED(17)
button = Button(2)

while True:
    button.wait_for_press()
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    