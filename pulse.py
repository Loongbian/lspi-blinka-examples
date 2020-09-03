import time
import board
import pulseio

led = pulseio.PWMOut(board.PWM3, frequency=5000, duty_cycle=0)

while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            print("up    ", end="\r")
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            print("down  ", end="\r")
        time.sleep(0.01)

