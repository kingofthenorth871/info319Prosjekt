
##første del av testingen

from pyspark import SparkConf, SparkContext

sc = SparkContext(master="local", appName= "Spark Demo")
print(sc.textFile("C:\\deckofcards.txt").first())

##andre del av testingen

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('find_hacker').getOrCreate()

from pyspark.ml.clustering import KMeans

dataset = spark.read.json("C:\\Users\\ASUS g751jt\\PycharmProjects\\info319Prosjekt\\tweets.json")