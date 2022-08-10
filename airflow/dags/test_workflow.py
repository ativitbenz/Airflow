from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
import io


default_args = {"owner" : "airflow"}

def test_function():
    with io.open("/opt/ariflow/output_files/test.txt","w", encodeing="utf-8") as f1:
        f1.write("hello from airflow dag")
        f1.close()

with DAG(dag_id="test_workflow", start_date=datatime(2022,7,19),schedule_interval="@daily", default_args=default_args) as dag :
    test_function =PythonOperator(
        task_id="test_function",
        python_callable = test_function
    )