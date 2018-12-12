#Use Python 3 as parent image
FROM python:3

#Set the working directory to /app
WORKDIR /app

# Copy contents of current directory into container /app  
COPY . /app

RUN pip install Pillow

#run resize.py when container launches
CMD ["python", "resize.py"]
