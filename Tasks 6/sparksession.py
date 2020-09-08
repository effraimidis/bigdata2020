from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

def handle(rdd):
	if not rdd.isEmpty():
		global ss
		list = rdd.collect()
		for l in list:
			print(l)

sc = SparkContext(appName='Stocks')
ssc = StreamingContext(sc, 1)

ss = SparkSession.builder.appName('Stocks').getOrCreate()

ss.sparkContext.setLogLevel('WARN')

ks = KafkaUtils.createDirectStream(ssc, ['stocks'], {'metadata.broker.list':'localhost:9093'})

lines = ks.map(lambda x: x[1])

transform = lines.map(lambda st: st)

transform.pprint()
#transform.foreachRDD(handle)
ssc.start()
ssc.awaitTermination()
