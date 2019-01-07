import datetime as dt
from airflow import DAG
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume import Volume
from airflow.contrib.kubernetes.volume_mount import VolumeMount

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
  
    volume_mount = VolumeMount('test-volume',
                               mount_path='/images/',
                               sub_path=None,
                               read_only=False)

    volume_config = {
        'hostPath':
            {
                'path': '/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/'
            }
    }
    volume = Volume(name='test-volume', configs=volume_config)

    for item in dirs:

        resizeimg=KubernetesPodOperator(namespace='default', 
                                        task_id="resize-k8s-" + item,
                                        name="resize-k8s",
                                        image="localhost:5000/resize:0.1",
                                        cmds=["python","resize.py"],
                                        env_vars={'IMAGE_ID': '/images/{}'.format(item)},
                                        #secrets=[secret_env, secret_file],
                                        volumes=[volume],
                                        volume_mounts=[volume_mount],
                                        get_logs=True,
                                        dag=dag
                                        )
