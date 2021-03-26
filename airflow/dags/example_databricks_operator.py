import airflow
import time
from airflow import DAG
from airflow.contrib.operators.databricks_operator import DatabricksSubmitRunOperator

args = {
    'owner': '',
    'email': ['mark.lee@databricks.com'],
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(2)
}
new_cluster = {
    'spark_version': '6.0.x-scala2.11',
    'node_type_id': 'i3.xlarge',
    'aws_attributes': {
        'availability': 'ON_DEMAND'
    },
    'num_workers': 2
}

dag = DAG(
	dag_id = 'example_databricks_operator',
	default_args=args,
	schedule_interval='@daily')

notebook_task_params = {
   'new_cluster': new_cluster,
   'notebook_task':{
	'notebook_path':'/Repos/mark.lee@databricks.com/airflow_demo/src/example_job.py'
    }
}

notebook_task = DatabricksSubmitRunOperator(
    task_id='Airflow_',
    databricks_conn_id='databricks_default',
    dag=dag,
    json=notebook_task_params)

