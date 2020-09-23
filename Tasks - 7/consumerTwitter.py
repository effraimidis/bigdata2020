from pyspark.streaming import StreamingContext
from pyspark import SparkContext
from pyspark.sql import SparkSession
import json
import sys

#reload(sys)
#sys.setdefaultencoding('UTF-8')

ss = SparkSession.builder.appName("twitter").config('spark.sql.warehouse.dir','user/hive/warehouse').config('hive.metastore.uris', 'thrift://localhost:9083').enableHiveSupport().getOrCreate()
sc = SparkContext.getOrCreate()

ssc = StreamingContext(sc, 5)


def transform(rdd):
	print(rdd.isEmpty())
	if not rdd.isEmpty():
		global ss
		df = ss.read.json(rdd)
		#df.printSchema()	
		df = df.select('id','created_at','text')
		df.show()
		df.write.saveAsTable(name='default.tweets',format='hive', mode='append')

lines = ssc.textFileStream("hdfs://localhost:9000/user/hadoop/twitter_data/")


data = lines.foreachRDD(lambda rdd:transform(rdd))


ssc.start()
ssc.awaitTermination()
