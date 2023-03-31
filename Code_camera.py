#!/usr/bin/env python3
#Código para tirar a foto com o botão e salvar no drive

import subprocess
import sys
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(21, gpio.IN, pull_up_down = gpio.PUD_UP)
gpio.setup(20, gpio.OUT)


try:
    print("Programa rodando")
    print("Ctrl +C para interromper")
    
    while True:
        
        if(gpio.input(21) == 1):
            print("Botao pressionado")
            subprocess.call(["./tirar_foto.sh"], shell=True)
            #subprocess.check_output(["./tirar_foto.sh"], shell=True)
            #subprocess.run
            gpio.output(20, gpio.HIGH)
            time.sleep(0.75)
            gpio.output(20, gpio.LOW)
            print("foto tirada")
        else:
            print("botao desligado")
        
        time.sleep(1)
            
except KeyboardInterrupt:
    pass
gpio.cleanup()
exit()
print("Fim")
