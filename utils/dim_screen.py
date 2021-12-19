import pigpio
gpio = pigpio.pi()
gpio.set_PWM_dutycycle(19, 60)  #0-255, so 64 is 1/4 duty cycle