#!/usr/bin/env python3
import sys

#Declarando o sensor de iluminação
sensor_luz = sys.argv[1]
horas = sys.argv[2]
#Adotando a inguagem binário 1= on 0= off

if int(sys.argv[1]) ==1: #Verificando se a luz está ligada  (começando ainda)
        luz = True # a luz está ligada
        luz_True = input("A luz deveria estar ligada?[s/n]")
                if sys.argv[2] < 12:
                        luz_True == "s" # A luz deveria estar ligada
                else:
                        luz_True == 'n' # A luz não deveria estar ligada
                        print('desligar a luz')
else:
        luz = False # a luz está apagada
        luz_False = input("A luz deveria estar desligada?[s/n]")
                if sys.argv[2] > 12:
                        luz_False == "s" # A luz deveria estar desligada
                else:
                        luz_False == 'n' # A luz não deveria estar desligada
                        print('acender a luz')
