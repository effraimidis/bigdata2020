from kafka import KafkaProducer

producer = KafkaProducer(
	bootstrap_servers=['localhost:9093'])

with open('shakespeare.txt') as f:
        lines = f.readlines()
        for line in lines:
                producer.send('shakespeare', value=line)
