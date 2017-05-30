# running spark on mesos

## installing mesos

### install zookeeper

brew install zookeeper
brew install mesos


launching mesos

```
# starting zookeeper
zkServer start

# starting mesos master node

/usr/local/sbin/mesos-master --registry=in_memory --ip=192.168.0.17 --zk=zk://192.168.0.17:2181/jpoint-mesos

# starting one slave

/usr/local/sbin/mesos-slave --master=zk://192.168.0.17:2181/jpoint-mesos --port=5052 --work_dir=/tmp/mesos2

# starting second slave

/usr/local/sbin/mesos-slave --master=zk://192.168.0.17:2181/jpoint-mesos --port=5053 --work_dir=/tmp/mesos3


# starting spark-shell

./bin/spark-shell --master mesos://192.168.0.17:5050

```

```

# put spark library on hadoop

hadoop fs -put spark-2.1.0-bin-hadoop2.7.tgz /tmp/spark-2.1.0-bin-hadoop2.7.tgz

```

[interesting link ](https://vanwilgenburg.wordpress.com/2015/05/10/how-to-run-a-spark-cluster-on-mesos-on-your-mac/)