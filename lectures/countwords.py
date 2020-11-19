from pyspark import SparkContext


sc = SparkContext()

lines = sc.parallelize(["It is sunny toady", "Friday will be a bit cloudy", "Yesterday was sunny"])

tokens = lines.flatMap(lambda x: x.split())

tokens = tokens.map(lambda x: (x , 1))

counts = tokens.reduceByKey(lambda x, y: x + y)

counts.saveAsTextFile("s3://habahram-bucket1/word-counts-result")

sc.stop()



