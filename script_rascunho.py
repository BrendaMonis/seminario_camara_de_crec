#!/usr/bin/env python3
import sys

#Declarando a temperatura do sensor
temp_sensor = sys.argv[1]

if int(sys.argv[1]) == 28:
        print(sys.argv[1], 'a temperatura está ideal')
elif int(sys.argv[1]) < 28:
        print(sys.argv[1], 'a temperatura está inferior a ideal')
else:
        print(sys.argv[1], 'a temperatura está superior a ideal')


#Declarando a umidade
umid_relat = sys.argv[2]

if float(sys.argv[2]) == 0.69:
        print(sys.argv[2], 'a umidade está ideal')
elif float(sys.argv[2]) < 0.69:
        print(sys.argv[2], 'a umidade está inferior a ideal')
else:
        print(sys.argv[2], 'a umidade está superior a ideal')
