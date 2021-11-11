from kafka import KafkaConsumer
from kafka import TopicPartition

consumer = KafkaConsumer(bootstrap_servers='IP:PORT')

# assign the consumer to read from partition 0
consumer.assign([TopicPartition('foobar', 0)])

for msg in consumer:
    print (msg)




 