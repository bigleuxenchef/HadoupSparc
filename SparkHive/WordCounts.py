
from pyspark import SparkConf, SparkContext


import os
from StdSuites.Text_Suite import word
from __builtin__ import sum




# Configure the Spark environment
sparkConf = SparkConf()\
        .setAppName("WordCountSamples")\
        .set("spark.executor.memory", '1g')\
        .set('spark.executor.cores', '8')\
        .set('spark.driver.cores', '1')\
        .set('spark.num.executors', '1')\
        .set('spark.total.executor.cores', '8')\
        .set('spark.cores.max', '8')\
        .set("spark.driver.memory",'1g')
#.setMaster("local")




sc = SparkContext(conf = sparkConf)



filelist = {"test.md","hdfs://MBP15.local:9000/tmp/test.md",os.environ["SPARK_HOME"] + "/../README.md"}
# The WordCounts Spark program
#textFile=sc.textFile("hdfs://MBP15.local:9000/tmp/application_1492290106735_0014_1",8) # 4 meqns the number of partitions



for f in filelist:
    
    print "****** FILE : {} ******".format(f)
    textFile = sc.textFile(f)
    wordCounts = textFile.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
    wordCounts.cache()

    #print the first 10 tuple of the unsorted collection
    for wc in wordCounts.collect()[1:10]: print wc

    list=wordCounts.mapValues((lambda a,b: a + b))

    print "total words :", wordCounts.map(lambda a: a[1]).reduce(lambda a, b: a + b)
    print "Concat words and show firt 50 char : ",wordCounts.map(lambda a: a[0]).reduce(lambda a, b: a + '*' +  b)[0:50]
    print "top 5 most frequent word :", wordCounts.sortBy(lambda x: x[1],ascending=False).take(5)
    print "****** *     * *****         "
    print "*      **    * *     * "
    print "*      * *   * *      *"
    print "****   *  *  * *      *"
    print "*      *   * * *      *"
    print "*      *    ** *     * "
    print "****** *     * *****"


