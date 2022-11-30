#!/usr/bin/env python3
import sys
import datetime

#Declarando o sensor de iluminação
sensor_luz = sys.argv[1]
luz = ''
data = datetime.datetime.now()
horas = data.hour
print('horário',horas)

#Adotando a inguagem binário 1= on 0= off

if int(sys.argv[1]) == 1: #Verificando se a luz está ligada  (começando ainda)
        luz is True; print("A luz está ligada") # a luz está ligada
else:
        luz is  False; print('A luz está apagada') # a luz está apagada

#Verificando se a luz deveria estar acesa ou apagada:

if int(sys.argv[1]) == 1:
        if float(horas) <= 6:
                print('Manter a luz acesa') # A luz deve continuar ligada
        elif float(horas) >= 18:
                print('Manter a luz acesa') # A luz deve continuar ligada
        else:
                print('Desligar a luz') # A luz não deveria estar ligada
elif int(horas) == 0:
        if float(horas) > 6 and float(horas) < 18:
                print('Manter a luz apagada') # A luz deve continuar desligada
        else:
                print('Acender a luz') # A luz não deveria estar desligada
