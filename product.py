from confluent_kafka import Producer
import socket
conf = {'bootstrap.servers': "my-kafka-0.my-kafka-headless.kafka.svc.cluster.local:9092",
        'client.id': socket.gethostname()}

producer = Producer(conf)
topic = "test"
for i in range(0,10):
    
  producer.produce(topic, key="message"+str(i), value="HELLO-ULRICH"+str(i))
  producer.flush()
