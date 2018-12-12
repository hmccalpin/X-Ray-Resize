FROM python:3

COPY Users/hmccalpin/Kaggle_Xray_dataset/images/ /data/images/
COPY Users/hmccalpin/Kaggle_Xray_dataset/sample_labels.csv /data/sample_labels.csv

ADD resize.py /

RUN pip install Pillow

CMD ["python", "./resize.py"]
