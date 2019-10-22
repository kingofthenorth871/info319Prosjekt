from pyspark import SparkConf, SparkContext

sc = SparkContext(master="local", appName="SvmTest")
print(sc.textFile("C:\\test.txt").first())

