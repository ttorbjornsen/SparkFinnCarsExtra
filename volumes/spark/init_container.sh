#!/bin/bash
service cron start
service mysql start
source /root/.virtualenvs/airflow/bin/activate

mysql -u root -e 'create database airflow'
airflow initdb
airflow webserver -p 8082 -D
airflow scheduler -D 
