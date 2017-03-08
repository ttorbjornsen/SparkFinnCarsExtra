from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from datetime import datetime, timedelta

import os
import sys

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 3, 7),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('SparkBatch_v5', default_args=default_args, schedule_interval="00 12 * * *")

cmd = "sh /usr/jobs/SparkBatchFinnCars.sh "
t1 = BashOperator(task_id='spark_batch',bash_command=cmd,dag=dag)
