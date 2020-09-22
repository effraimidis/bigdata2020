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
		df = ss.createDataFrame(rdd, schema=['timest','open','high','low','close','volume'])
		df.show()
		df.write.saveAsTable(name='default.stocks',format='hive', mode='append')


sc = SparkContext(appName='Stocks')
sqlContext = SQLContext(sc)
ssc = StreamingContext(sc, 1)

#ss = SparkSession.builder.appName('Stocks').getOrCreate()
ss = SparkSession.builder.appName('Stocks').config('spark.sql.warehouse.dir','user/hive/warehouse').config('hive.metastore.uris', 'thrift://localhost:9083').enableHiveSupport().getOrCreate()

ss.sparkContext.setLogLevel('WARN')

ks = KafkaUtils.createDirectStream(ssc, ['stocks'], {'metadata.broker.list':'localhost:9093'})
#ks = KafkaUtils.createRDD(ssc, {'metadata.broker.list':'localhost:9093'})

data = ks.map(lambda x: tuple(x[1].split()))

#lines = data.map(lambda x: x.split('\r\n'))
data.pprint()

data.foreachRDD(lambda rdd: handle(rdd))

ssc.start()
ssc.awaitTermination()
