from kafka import KafkaProducer
import requests
import json

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'

producer = KafkaProducer(
	bootstrap_servers=['localhost:9093'],
	value_serializer= lambda x: json.dumps(x).encode('utf-8'))

response = requests.request('GET', url)
print(response.text)
producer.send('stocks', value=response.text)
