import datetime
from datetime import time

data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

def temp(t):
	temp = 0.0004*t**4 - 0.0292*t**3 +0.5633*t**2 - 2.8169*t + 24.06
	return temp

with open('testedados.txt', 'w') as teste:
	x = 0
	while x <= 24:
		if temp(x) <= 28:
			fan = 0
			teste.write(
			'{}: Temperatura: {}C° Ventilador: {}\n'.format(
			data, round(temp(x), 2), fan))
		else:
			fan = 1
			teste.write(
			'{}: Temperatura: {}C° Ventilador: {}\n'.format(
			data, round((temp(x-1) - 2), 2), fan))
		x+= 0.25

