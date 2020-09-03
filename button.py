import time
import board
import digitalio

print("hello blinka!")

btn = digitalio.DigitalInOut(board.GPIO2)
btn.direction = digitalio.Direction.INPUT

while True:
    print("btn is {}".format(btn.value))
    time.sleep(0.2)

