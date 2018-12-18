import datetime as dt
from airflow import DAG
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

path =  path = "/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/"
dirs = os.listdir(path)

resized_counter = 0

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 12, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
    'wait_for_downstream': True,
    'depends_on_past': True
}


with DAG('xray_project_airflow_k8s',
         default_args=default_args,
         schedule_interval='0 * * * *',         
         max_active_runs = 1
         ) as dag:
    
    for item in dirs:
        
        resize_image=KubernetesPodOperator(namespace='default', 
            image="localhost:5000/my-resize",
            cmds=["Python","resize.py"],
            arguments=["resize(item)"],
            labels={"foo": "bar"},
            name="resize_k8s",
            task_id="resize" + item,
            get_logs=True,
            dag=dag
            )
            #resized_counter += 1                                
