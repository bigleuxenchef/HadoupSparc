 # Imports
# Take care about unused imports (and also unused variables),
# please comment them all, otherwise you will get any errors at the execution.
# Note that neither the directives "@PydevCodeAnalysisIgnore" nor "@UnusedImport"
# will be able to solve that issue.
#from pyspark.mllib.clustering import KMeans
from pyspark import SparkConf, SparkContext
import os
from StdSuites.Text_Suite import word
from __builtin__ import sum

# Configure the Spark environment
sparkConf = SparkConf().setAppName("WordCounts")
#.setMaster("local")
sc = SparkContext(conf = sparkConf)

# The WordCounts Spark program
textFile = sc.textFile(os.environ["SPARK_HOME"] + "/../README.md")

wordCounts = textFile.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)

for wc in wordCounts.collect(): print wc

list=wordCounts.mapValues((lambda a,b: a + b))

#print reduce((lambda a,b: b), wordCounts.collect())

#print reduce((lambda a,b : a+b), 

print list

