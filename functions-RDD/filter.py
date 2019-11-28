from pyspark import SparkContext
sc = SparkContext("local", "Filter app")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"]
)
word_filter = words.filter(lambda x: 'spark' in x)
filtered = word_filter.collect()
print("Filtered RDD -> {}".format(filtered))
