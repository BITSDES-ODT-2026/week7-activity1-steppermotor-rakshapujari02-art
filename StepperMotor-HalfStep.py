from machine import Pin
import time

IN1 = Pin(12, Pin.OUT)
IN2 = Pin(25, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(18, Pin.OUT)

while True:

    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    time.sleep(0.008)


    IN1.value(1)
    IN2.value(1)
    IN3.value(0)
    IN4.value(0)
    time.sleep(0.008)


    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(0)
    time.sleep(0.008)


    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)
    time.sleep(0.008)

  
    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    time.sleep(0.008)

    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(1)
    time.sleep(0.008)

    
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    time.sleep(0.008)

  
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    time.sleep(0.008)

