FROM python:3

WORKDIR hmccalpin/src/data/
COPY images/ /data/
COPY sample_labels.csv /data/
COPY resize.py /data/

RUN pip install Pillow

CMD ["python", "./resize.py"]
