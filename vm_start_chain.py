#Team Members: Karla Vasquez & Gila Kohanbash
import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket

"""This function (or "callback") will be executed when this client receives a connection
acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
	print("Connected to server (i.e., broker) with result code" +str(rc))
	client.subscribe("kdvasque/ping")
	client.publish("kdvasque/pong", "0")
	
	#Add the custom callback
	client.message_callback_add("kdvasque/ping", callback_on_ping)


def callback_on_ping(client, userdata, message):
	print("Custom callback - Message: "+message.payload.decode())
	msg = int(message.payload.decode())
	msg = msg + 1
	time.sleep(1)
	client.publish("kdvasque/pong", f"{msg}")
	

if __name__=='__main__':
	
	#get IP address
	ip_address="192.168.64.2"
	#create a client object
	client = mqtt.Client()

	#attach the on_connect() callback function defined above to the mqtt client
	client.on_connect = on_connect

	client.connect(host="192.168.64.2", port=1883, keepalive=60)

	"""ask paho-mqtt to spawn a spearate thread to handle incoming and
	outgoing mqtt messages."""
	

	client.loop_forever()
