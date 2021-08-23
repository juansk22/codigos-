from machine import Pin, PWM
from time import sleep

led_a = PWM(Pin(4), freq=50)
led_b = PWM(Pin(15), freq=50)
led_c = PWM(Pin(2), freq=50)

while True:
    for duty_cycle in range(0, 65535):
        led_a.duty(duty_cycle)
        led_b.duty(duty_cycle)
        led_c.duty(duty_cycle)
        sleep(0.01)
        
    