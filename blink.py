import time
import board
import digitalio

print("hello blinka!")

led = digitalio.DigitalInOut(board.GPIO2)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(0.05)

