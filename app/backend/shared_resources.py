import datetime
import time
import threading

from app                         import app
from app.backend.file_management import WRITE_LOGFILE_SYSTEM
from app.backend.email           import SEND_EMAIL

process_management_queue = []


""" ################ """
"""  mqtt functions  """
""" ################ """

mqtt_message_queue          = []
mqtt_incoming_messages_list = []


def REFRESH_MQTT_INPUT_MESSAGES_THREAD():

	try:
		Thread = threading.Thread(target=REFRESH_MQTT_INPUT_MESSAGES)
		Thread.start()  
		
	except Exception as e:
		WRITE_LOGFILE_SYSTEM("ERROR", "Thread | Refresh MQTT Messages | " + str(e)) 
		SEND_EMAIL("ERROR", "Thread | Refresh MQTT Messages | " + str(e)) 


def REFRESH_MQTT_INPUT_MESSAGES():   
	
	while True:
	
		try:

			# get the time check value
			time_check = datetime.datetime.now() - datetime.timedelta(seconds=60)
			time_check = time_check.strftime("%Y-%m-%d %H:%M:%S")

			for message in mqtt_incoming_messages_list:

				time_message = datetime.datetime.strptime(message[0],"%Y-%m-%d %H:%M:%S")   
				time_limit   = datetime.datetime.strptime(time_check, "%Y-%m-%d %H:%M:%S")

				# remove saved message after 60 seconnds
				if time_message <= time_limit:
					mqtt_incoming_messages_list.remove(message)

		except Exception as e:
			print(e)
			
		time.sleep(1)


""" ################# """
"""  system messages  """
""" ################# """

device_connetion_mqtt        = False
device_connetion_zigbee2mqtt = False

def SET_DEVICE_CONNECTION_MQTT(value):
	global device_connetion_mqtt
	device_connetion_mqtt = value

def GET_DEVICE_CONNECTION_MQTT():
    global device_connetion_mqtt
    return device_connetion_mqtt 

def SET_DEVICE_CONNECTION_ZIGBEE2MQTT(value):
	global device_connetion_zigbee2mqtt
	device_connetion_zigbee2mqtt = value	

def GET_DEVICE_CONNECTION_ZIGBEE2MQTT():
    global device_connetion_zigbee2mqtt
    return device_connetion_zigbee2mqtt	