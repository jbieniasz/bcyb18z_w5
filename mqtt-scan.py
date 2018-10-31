import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("[+] Connection successful")
	client.subscribe('#', qos=1) # Wszystkie tematy

def on_message(client, userdata, msg):
	print("[+] Topic: {0} - Message: {1}".format(msg.topic, msg.payload))

client = mqtt.Client(client_id = "MqttClient")
client.on_connect = on_connect
client.on_message = on_message
#37.6.228.196
#35.158.21.184
client.connect("35.158.21.184", 1883, 30)
client.loop_forever()