from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.functions import explode
from pyspark.sql.types import *
import json

def handle(rdd):
	if not rdd.isEmpty():
		global ss
		df = ss.read.json(rdd)
		df.show()		

sc = SparkContext(appName='Stocks')
sqlContext = SQLContext(sc)
ssc = StreamingContext(sc, 1)

ss = SparkSession.builder.appName('Spotify').getOrCreate()

ss.sparkContext.setLogLevel('WARN')

ks = KafkaUtils.createDirectStream(ssc, ['artists'], {'metadata.broker.list':'localhost:9093'})


data = ks.map(lambda x: x[1])


data.pprint()

data.foreachRDD(lambda rdd: handle(rdd))

ssc.start()
ssc.awaitTermination()
