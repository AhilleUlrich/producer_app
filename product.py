from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)
topic = "test"
for i in range(0,10):
    
  producer.produce(topic, key="messagezeze"+str(i), value="HELLO"+str(i))
  producer.flush()
