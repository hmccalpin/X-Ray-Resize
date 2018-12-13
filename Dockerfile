#Use Python 3 as parent image
FROM python:3

#Set the working directory to /app
WORKDIR /resize

# Copy contents of current directory into container /app  
COPY . /resize

RUN pip install Pillow

EXPOSE 5035

#run resize.py when container launches
CMD ["python", "resize.py"]
