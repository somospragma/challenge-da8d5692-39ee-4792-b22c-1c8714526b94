from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from src.extract.extract_transacciones import extract_transacciones
from src.transform.transform_transacciones import transform_transacciones
from src.load.load_transacciones import load_transacciones

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'transacciones_etl_dag',
    default_args=default_args,
    description='ETL para consolidar transacciones diarias',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
)

extract_task = PythonOperator(
    task_id='extract_transacciones',
    python_callable=extract_transacciones,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_transacciones',
    python_callable=transform_transacciones,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_transacciones',
    python_callable=load_transacciones,
    dag=dag,
)

extract_task >> transform_task >> load_task