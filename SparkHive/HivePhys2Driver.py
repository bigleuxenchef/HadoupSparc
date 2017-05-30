

import pyhs2  # using phys2 instead of hive
 
with pyhs2.connect(host='localhost',
                   port=10000,
                   authMechanism="PLAIN",
                   user='hadoop',
                   database='default') as conn:
    with conn.cursor() as cur:
        # Show databases
        print cur.getDatabases()

        cur.execute("Create Database if not exists rumi")            
        cur.execute("Create Table if not exists rumi.droolsset (nameSet string,contentSet string)") 
        # Execute query
        cur.execute("select * from rumi.droolsset")
 
        # Return column info from query
        print cur.getSchema()
        # load database with Drools File
        
        with open('Example1.drl') as f:
            lines = f.readlines()
            print lines
        
        myrulesrting = open('Example1.drl').read()
         
        cur.execute("insert into rumi.droolsset values (\"Example1\",\"example2\")")
        # not very practical to insert a file in a column, it may create more than one line as there are \n or "
        query = "insert into rumi.droolsset values ('Example1.drl','" + myrulesrting + "')"
        cur.execute(query)
        
        print "QUERY : ", query

         
        # Fetch table results
        
