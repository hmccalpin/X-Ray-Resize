FROM python:3

WORKDIR /hmccalpin/src/data/
COPY images/ ./
COPY sample_labels.csv ./
COPY resize.py ./

RUN pip install Pillow

CMD ["python", "resize.py"]
