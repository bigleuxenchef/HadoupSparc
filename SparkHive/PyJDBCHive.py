from pyhive import hive # using hive package


conn = hive.Connection(host="localhost", port=10000, username="hadoop")
cursor = conn.cursor()

cursor.execute("Show Databases")

for row in cursor.fetchall():
    print "Row:", row
cursor.close()

cursor.execute("Show tables")

for row in cursor.fetchall():
    print "Row:", row
cursor.close()

cursor.execute("select * from rumi.droolsset")


for row in cursor.fetchall():
    print "Row:", row
cursor.close()

conn.close()

