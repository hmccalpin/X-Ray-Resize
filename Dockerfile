FROM python:3

COPY . /app
WORKDIR /app

RUN pip install Pillow

CMD ["python", "resize.py"]
