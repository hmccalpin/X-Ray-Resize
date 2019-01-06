import datetime as dt
from airflow import DAG
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes import secret

path =  path = "/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/"
dirs = os.listdir(path)

resized_counter = 0

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 12, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
    'wait_for_downstream': True
}


with DAG('xray_project_airflow_k8s_v02',
         default_args=default_args,
         schedule_interval='0 * * * *',         
         max_active_runs = 1
         ) as dag:
    
    for item in dirs:
        
        resizeimg=KubernetesPodOperator(namespace='default', 
                                        task_id="resize-k8s-" + item,
                                        name="resize-k8s",
                                        image="localhost:5000/resize:0.1",
                                        cmds=["python","resize.py"],
                                        env_vars={'IMAGE_ID': '{{/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/{}}}'.format(item)},
                                        #secrets=[secret_env, secret_file],
                                        get_logs=True,
                                        dag=dag
                                        )
