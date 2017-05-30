# remote connection from spark to hiveserver 2


```bash

<host>:libexec <user>$ ./bin/spark-beeline 
Beeline version 1.2.1.spark2 by Apache Hive
beeline> !connect jdbc:hive2://localhost:10000
Connecting to jdbc:hive2://localhost:10000
Enter username for jdbc:hive2://localhost:10000: root
Enter password for jdbc:hive2://localhost:10000: *******
log4j:ERROR Could not connect to remote log4j server at [localhost]. We will try again later.
Connected to: Apache Hive (version 2.1.0)
Driver: Hive JDBC (version 1.2.1.spark2)
Transaction isolation: TRANSACTION_REPEATABLE_READ
0: jdbc:hive2://localhost:10000> show databases;
+----------------+--+
| database_name  |
+----------------+--+
| default        |
| rumi           |
+----------------+--+
2 rows selected (0.182 seconds)
0: jdbc:hive2://localhost:10000> use default;
No rows affected (0.025 seconds)
0: jdbc:hive2://localhost:10000> show tables;
+------------+--+
|  tab_name  |
+------------+--+
| customers  |
| sample_07  |
| sample_08  |
| web_logs   |
+------------+--+
4 rows selected (0.057 seconds)
0: jdbc:hive2://localhost:10000> 


```


