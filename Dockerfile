FROM python:3

WORKDIR hmccalpin/src/data
COPY images/ /data/
COPY sample_labels.csv /data/

ADD resize.py /

RUN pip install Pillow

CMD ["python", "./resize.py"]
