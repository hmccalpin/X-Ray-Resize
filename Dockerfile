#Use Python 3 as parent image
FROM python:3.6

#Set the working directory to /resize
WORKDIR /resize

# Copy contents of current directory into container /resize  
COPY /Users/hmccalpin/Desktop/X-Ray-Resize/ /resize

RUN pip install Pillow

EXPOSE 5035

#run resize.py when container launches
CMD ["python", "resize.py"]
