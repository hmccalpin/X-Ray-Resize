#Use Python 3 as parent image
FROM python:3.6

#Set the working directory to /resize
WORKDIR /resize-app

# Copy contents of current directory into container /resize  
COPY  resize.py .

RUN pip install Pillow

ENTRYPOINT ["python", resize.py"]

#run resize.py when container launches
#CMD ["python", "resize.py"]
