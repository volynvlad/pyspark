from pyspark import SparkContext
from pyspark import SparkFiles
finddistance = "/home/vlad/books/pyspark.pdf"
finddistancename = "pyspark.pdf"
sc = SparkContext("local", "SparkFile App")
sc.addFile(finddistance)
print("Absolute Path -> {}".format(SparkFiles.get(finddistancename)))
