#!/usr/bin/env python3
import sys

#Declarando a temperatura do sensor
temp_sensor = sys.argv[1]

if int(sys.argv[1]) == 28:
        print(sys.argv[1], 'a temperatura está ideal') #ver novamente a temperatura
elif int(sys.argv[1]) < 28:
        print(sys.argv[1], 'a temperatura está inferior a ideal') #Precisa ligar aquecedor
else:
        print(sys.argv[1], 'a temperatura está superior a ideal') #Precisa ligar aspersor
#Loop para temperatura


#Declarando a umidade relativa do ar via sensor
umid_relat = sys.argv[2]

if float(sys.argv[2]) == 0.69:
        print(sys.argv[2], 'a umidade está ideal') #Ver novamente a umidade
elif float(sys.argv[2]) < 0.69:
        print(sys.argv[2], 'a umidade está inferior a ideal') #Precisa ligar aspersor
else:
        print(sys.argv[2], 'a umidade está superior a ideal') #Precisa ligar ventilador (pensar melhor)
#Loop para umidade

#Declarando a umidade do solo via sensor
umid_solo = sys.argv[3]

if float(sys.argv[3]) ==0.49:
        print(sys.argv[3], 'a umidade está ideal') #Ver novamente a umidade
elif float(sys.argv[3]) < 0.49:
        print(sys.argv[3], 'a umidade está inferior a ideal') #Precisa irrigar
else:
        print(sys.argv[3], 'a umidade está superior a ideal') #Precisa desligar irrigação
#Loop para umidade
