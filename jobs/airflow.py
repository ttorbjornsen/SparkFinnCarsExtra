from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from datetime import datetime, timedelta

import os
import sys

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
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

dag = DAG('spark_test_dag', default_args=default_args, schedule_interval=timedelta(1))

#os.environ['SPARK_HOME'] = '/path/to/spark/root'
sys.path.append(os.path.join(os.environ['SPARK_HOME'], 'bin'))

spark_task = BashOperator(
    task_id='spark_task1',
    bash_command='spark-submit --class {{ params.class }} {{ params.jar }}',
    params={'class': 'Batch', 'jar': '/usr/jobs/SparkFinnCars-1.0-SNAPSHOT.jar'},
    dag=dag
)