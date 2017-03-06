FROM gettyimages/spark
RUN apt-get update && apt-get -y install cron && apt-get -y install vim && apt-get -y install python2.7 && apt-get -y install gcc && apt-get -y install python-dev && apt-get -y install virtualenv && apt-get -y install build-essential && mkdir /root/.virtualenvs && cd /root/.virtualenvs && virtualenv -p /usr/bin/python2.7 airflow 
RUN export DEBIAN_FRONTEND=noninteractive && apt-get -q -y install mysql-server
RUN apt-get -y install libmysqlclient-dev
#RUN service mysql start
#RUN /bin/bash -c "mysql -u root -e 'create database airflow'"
RUN "echo"
RUN /bin/bash -c "source /root/.virtualenvs/airflow/bin/activate; pip install airflow[hive,mysql]"
RUN /bin/bash -c "source /root/.virtualenvs/airflow/bin/activate; airflow initdb; airflow webserver -p 8082 -D"
RUN /bin/bash -c "service mysql start;mysql -e 'create database airflow'"

RUN (crontab -l ; echo "JAVA_HOME=/usr/jdk1.8.0_112") | crontab - && (crontab -l ; echo "SPARK_DIST_CLASSPATH=/usr/hadoop-2.7.3/etc/hadoop/*:/usr/hadoop-2.7.3/share/hadoop/common/lib/*:/usr/hadoop-2.7.3/share/hadoop/common/*:/usr/hadoop-2.7.3/share/hadoop/hdfs/*:/usr/hadoop-2.7.3/share/hadoop/hdfs/lib/*:/usr/hadoop-2.7.3/share/hadoop/hdfs/*:/usr/hadoop-2.7.3/share/hadoop/yarn/lib/*:/usr/hadoop-2.7.3/share/hadoop/yarn/*:/usr/hadoop-2.7.3/share/hadoop/mapreduce/lib/*:/usr/hadoop-2.7.3/share/hadoop/mapreduce/*:/usr/hadoop-2.7.3/share/hadoop/tools/lib/*") | crontab - && (crontab -l ; echo "#00 18 * * * PATH=$PATH:/usr/spark-2.0.2/bin /usr/jobs/SparkStreamingFinnCars.sh") | crontab - && (crontab -l ; echo "#01 18 * * * PATH=$PATH:/usr/jdk1.8.0_112/bin /usr/jobs/ExtractFinnCars.sh") | crontab - && (crontab -l ; echo "#00 18 * * * PATH=$PATH:/usr/spark-2.0.2/bin /usr/jobs/SparkBatchFinnCars.sh") | crontab -