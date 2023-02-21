#Team Members: Karla Vasquez & Gila Kohanbash
import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives
a connection acknowledgement packet response from the server. """

def on_connect(client, userdata, flags, rc):
	"""Once our client has successfully connected, it makes sense to subscribe
	to all the topics of interest. Also, subscribing in on_connect() means that 
	if we lose the connection and the library reconnects for us, this callback
	will be called again thus renewing the subscriptions"""

	client.subscribe("kdvasque/pong")

	#Add the custom callback by indicating the topic and the name of the callback
	client.message_callback_add("kdvasque/pong", callback_on_pong)

"""This object (functions are objects!) serves as the default callback for
messages received when another node publishes a message this client is
subscribed to. By "default,"" we mean that this callback is called if a custom
callback has not been registered using paho-mqtt's message_callback_add()."""

#when listening, what to do with message
def callback_on_pong(client, userdata, msg):
	print("Custom callback - Message: "+msg.payload.decode())
	msg = int(msg.payload.decode())
	msg = msg + 1
	time.sleep(1)
	client.publish("kdvasque/ping", msg)



if __name__=='__main__':
	#create a client object
	client = mqtt.Client()
	
	#attach the on_connect() callback function defined above to the mqtt client
	client.on_connect = on_connect
	client.connect(host="192.168.64.2", port=1883, keepalive=60)
	client.loop_forever()
