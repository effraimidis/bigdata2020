from kafka import KafkaConsumer

consumer = KafkaConsumer(
	'shakespeare',
	bootstrap_servers=['localhost:9093'],
	auto_offset_reset='earliest',
	enable_auto_commit=True,
	group_id='my-group')

for message in consumer:
	print(message.value)

