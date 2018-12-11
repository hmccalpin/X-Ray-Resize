FROM python:3

ADD resize.py /

RUN pip install Pillow

CMD ["python", "./resize.py"]
