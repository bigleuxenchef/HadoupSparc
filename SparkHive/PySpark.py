'''
Created on Apr 18, 2017

@author: rumi
'''
import sys, os
from random import random
from operator import add

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
import pyspark


if __name__ == "__main__":
    """
        Usage: pi [partitions]
    """
    

    conf =  pyspark.SparkConf()\
        .set("spark.executor.memory", '4g')\
        .set('spark.executor.cores', '4')\
        .set('spark.driver.cores', '4')\
        .set('spark.num.executors', '4')\
        .set('spark.total.executor.cores', '4')\
        .set('spark.cores.max', '4')\
        .set("spark.driver.memory",'12g')
        
    sc = pyspark.SparkContext(conf=conf)

    spark = SparkSession\
        .builder\
        .master(os.getenv("SPARK_HOME"))\
        .appName("PythonPi")\
        .getOrCreate()
        
   

   
    
    partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    n = 1000000 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0
    
    def f2(index):
        print("index %d" % index)
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0
    
    myrdd = spark.sparkContext.parallelize(range(1, n + 1), partitions).cache()
    count = myrdd.map(f).reduce(add)
    
    result = myrdd.map(f2).reduce(add)
    

    print("Pi is roughly %f" % (4.0 * count / n))

    print ("result 2 %f" % result)

    spark.stop()