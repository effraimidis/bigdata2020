from kafka import KafkaClient
from kafka import KafkaProducer
import requests
import csv, json
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo&datatype=csv'
#url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

#client = KafkaClient(hosts='localhost:9093')
#producer = SimpleProducer(client)

producer = KafkaProducer(bootstrap_servers=['localhost:9093'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))



response = requests.request('GET', url)
#print(response.text)
my_file = open('response.csv','w')
writer = csv.writer(my_file)
for line in response.text.split():
	the_line = []
	for cell in line.split(','):
		the_line.append(cell)
	writer.writerow(the_line)
my_file.close()

df = pd.read_csv('response.csv', sep=',')

for i in range(30):
#data = "" + str(s['timestamp']) + " " + str(s['open']) + " " + str(s['high']) + " " + str(s['low']) + " " + str(s['close']) + " " + str(s['volume'])
	s = df.sample(n=1, replace=False).to_string().split()[6:]
	data = "" + s[1] + " " + s[2] + " " + s[3] + " " + s[4] + " " + s[5] + " " + s[6]
	producer.send('stocks', data)
	print(data)
