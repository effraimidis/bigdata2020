from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def lines_rdd(line):
	print(line)

sc = SparkContext(appName='Shakespeare')
ssc = StreamingContext(sc, 5)

with open('shakespeare.txt') as f:
	the_lines = f.readlines()

lines = sc.parallelize(the_lines)

fore = lines.foreach(lines_rdd)

ssc.start()
ssc.awaitTermination()
