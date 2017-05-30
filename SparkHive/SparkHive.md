


!connect jdbc:hive2://localhost:10000
grant all to user hadoop;
hadoop security disable that way no need to enter password :-)

```
./bin/beeline
ls: /usr/local/Cellar/apache-spark/2.1.1/libexec/lib/spark-assembly-*.jar: No such file or directory
Beeline version 1.2.1 by Apache Hive
beeline> !connect jdbc:hive2://localhost:10000
Connecting to jdbc:hive2://localhost:10000
Enter username for jdbc:hive2://localhost:10000: root
Enter password for jdbc:hive2://localhost:10000: 
Connected to: Apache Hive (version 1.2.1)
Driver: Hive JDBC (version 1.2.1)
Transaction isolation: TRANSACTION_REPEATABLE_READ
0: jdbc:hive2://localhost:10000> show databases;

+----------------+--+
| database_name  |
+----------------+--+
| default        |
| rumi           |
+----------------+--+
2 rows selected (0.284 seconds)
0: jdbc:hive2://localhost:10000> 

```