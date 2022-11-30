import datetime
import time		# Controle da frequencia com qual o código é executado
import RPi.GPIO as GPIO
import board
import adafruit_dht # Pacotes dos sensores e controles do Raspberry pi (necessita instalação)
#import biblioteca sensor de umidade do solo

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)	#Ventilador
GPIO.setup(12, GPIO.OUT)	#Aspersor
GPIO.setup(13, GPIO.OUT)	#Desumidificador
sensor = adafruit_dht.DHT11(board.D14) #Pins arbitrários
#GPIO.setup(15, GPIO.OUT)	#Irrigação
#sensor_um_solo = #########(board.15)

while True:
	try:

		temp = sensor.temperature
		humidity = sensor.humidity
		if temp > 28:
			fans=1
			GPIO.output(11,GPIO.HIGH)
		else:
			GPIO.output(11,GPIO.LOW)
			fans=0
		if humidity < 0.61:
			asp = 1
			GPIO.output(12 , GPIO.HIGH)
			time.sleep(1.0)	# ligar o aspersor por muito tempo saturaria o ambiente
			GPIO.output(12 , GPIO.LOW)
		elif humidity > 0.67:
			desum = 1
			asp = 0
			GPIO.output(13 , GPIO.HIGH)
		else :
			desum = 0
			asp = 0
			GPIO.output(13 , GPIO.LOW)
		#soil_moisture = sensor_um_solo.moisture
		#if soil_moisture < 0.49:
			#GPIO.output(15 , GPIO.HIGH)
			# time.sleep(120.0)
			#GPIO.output(15 , GPIO.LOW)
			irrig = 1
		with open('record_dados', 'w') as file:
		 file.write(
		 "{} Temperatura: {}*C Humidity: {}% Ventilador:{} Desumidificador: {} Aspersor: {} ".format(
		 datetime.datetime.now(), temp, humidity*100, fans, desum, asp))
	except RuntimeError as error:
        	print(error.args[0])
        	time.sleep(2.0)
        	continue
	except Exception as error:
        	sensor.exit()
        	raise error
	time.sleep(900.0 - asp) # - irrig
