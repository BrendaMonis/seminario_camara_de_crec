#!/usr/bin/env python3
import sys

#Declarando o sensor de iluminação
sensor_luz = sys.argv[1]
luz = ''
horas = sys.argv[2]

#Adotando a inguagem binário 1= on 0= off

if int(sys.argv[1]) == 1: #Verificando se a luz está ligada  (começando ainda)
        luz is True; print("A luz está ligada") # a luz está ligada
else:
        luz is  False; print('A luz está apagada') # a luz está apagada

#Verificando se a luz deveria estar acesa ou apagada:

if int(sys.argv[1]) == 1 and float(sys.argv[2]) < 12:
        Print('A luz está ligada e deve ser continuar assim') # A luz deveria estar ligada
elif int(sys.argv[1]) == 1 and float(sys.argv[2]) > 12:
        print('A luz está ligada, porém deve ser desligada') # A luz não deveria estar ligada
elif int(sys.argv[1]) == 0 and float(sys.argv[2]) > 12:
        print('A luz está desligada e deve ser continuar assim') # A luz deveria estar desligada
else:
        print('A luz está desligada, porém deve ser ligada') # A luz não deveria estar desligada
