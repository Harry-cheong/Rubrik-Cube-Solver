import paho.mqtt.client as mqtt
import random
import time

class client_computer():
        # MQTT Presets
    broker = 'localhost'
    port = 1883
    topic = 'rubrikcube/cubeface'
    client_id = 'Harry \'s computer'
    username = 'algorithm'
    password = '12345'
    timeout_reconnect = 60

    # The callback for when the client receives a CONNACK response from the server.
    def __init__(self):
        self.topic = 'rubrikcube/cubeface'
        self.ev3_present = False

        client = mqtt.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = self.on_connect
        client.connect(self.broker, self.port, self.timeout_reconnect)
        self.client = client
    
    def checkforev3(self):
        while True:
            self.publish(self.client, 'comp')
            self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.topic)

    def publish(self, client, message):
        msg_count = 0
        time.sleep(1)
        result = client.publish(self.topic, message)
        # result: [0, 1]
        status = result[0]
        # if status == 0:
        #     print(f"Send `{message}` to topic `{self.topic}`")
        # else:
        #     print(f"Failed to send message to topic {self.topic}")

    # The callback for when a PUBLISH message is received from the server.
    def swap_channel(self):
        pass

    def on_message(self, client, userdata, msg):
        print(msg.payload)  
        print(userdata)    

compclient = client_computer()

compclient.checkforev3()