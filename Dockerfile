FROM python:3

ADD resize.py /
COPY ./ images
COPY ./ sample_labels.csv

RUN pip install Pillow

CMD ["python", "./resize.py"]
