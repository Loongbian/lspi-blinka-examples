import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GPIO2, echo_pin=board.GPIO3)

while True:
    print((sonar.distance,))
    time.sleep(1)
