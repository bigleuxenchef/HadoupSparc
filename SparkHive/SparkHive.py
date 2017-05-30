'''
Created on May 7, 2017

@author: rumi
'''
from os.path import expanduser, join
from pyspark.sql import SparkSession
from pyspark.sql import Row
import pyspark

    
if __name__ == '__main__':
    """
        Usage: 
    """
    
    conf =  pyspark.SparkConf()\
        .set("spark.executor.memory", '8g')\
        .set('spark.executor.cores', '4')\
        .set('spark.driver.cores', '1')\
        .set('spark.num.executors', '1')\
        .set('spark.total.executor.cores', '6')\
        .set('spark.cores.max', '8')\
        .set("spark.driver.memory",'12g')\
        .set("hive.execution.engine","spark")
     
        
        #.set('spark.sql.hive.metastore.version','2.1.0')

        
        

    sc = pyspark.SparkContext(conf=conf).setLogLevel("ERROR")

   


    warehouse_location = '/Users/hive/warehouse'

    spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .getOrCreate()


    jdbcDF = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:hive2://mbp15.local:10000/") \
        .option("dbtable", "rumi.droolsset") \
        .option("user", "hadoop") \
        .load()
        
    jdbcDF.printSchema()
    jdbcDF.show()
    
    jdbcDF2 = spark.write \
        .format("jdbc") \
        .option("url", "jdbc:hive2://mbp15.local:10000/") \
        .option("dbtable", "rumi.droolsset") \
        .option("user", "hadoop") \
        .save()
        
        
    print jdbcDF2.show()
        
    #jdbcDF.createOrReplaceTempView("table1")
    
    #jdbcDF.filter(jdbcDF["droolsset.setcontenttext"] != None).show()
    
    #jdbcDF.show()
    #df2 = spark.sql("select * from table1")
    #df2.show()
    spark.sql("SHOW DATABASES").show()
    spark.sql("show tables").show()
    spark.sql("CREATE TABLE IF NOT EXISTS droolsset2  (nameset string, contentset STRING)")
    
    #spark.sql("select * from droolsset").show()
    spark.sql("show tables").show()
        


    #spark.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING)")    
    #spark.sql("select * from droolsset").show()