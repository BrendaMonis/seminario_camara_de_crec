#!/usr/bin/env python3
import datetime
from datetime import time

data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

def umidade(t):
        umidade=0.0003*t*3 - .0106*t*2 + 0.0562*t + 0.7811
        return umidade


with open('dados_umidade.txt', 'w') as teste:
        x = 0
        while x <= 24:
                if umidade(x) < 0.61:
                        asp = 1
                        desum = 0
                        teste.write(
                        '{}: Umidade Relativa: {}% Aspersor: {} Desumidificador: {}\n'.format(
                        data, round(umidade(x)*100 +2*x, 2), asp, desum)) 
                        #umidade(x)*100 - 2
                elif umidade(x) > 0.67: 
                        asp = 0
                        desum = 1
                        teste.write(
                        '{}: Umidade relativa: {}% Aspersor: {} Desumidificador: {}\n'.format(
                        data, round(umidade(x+2)*100 , 2), asp, desum))
                        # Desumidificador ligado até chegar na umidade correta 
                else:
                        asp = 0
                        desum = 0
                        teste.write(
                        '{}: Umidade relativa: {}% Aspersor: {} Desumidificador: {}\n'.format(
                        data, round(umidade(x)*100 , 2), asp, desum))
                x+= 0.25
