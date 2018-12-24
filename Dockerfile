#Use Python 3 as parent image
FROM python:3

#Set the working directory to /resize
#WORKDIR /resize-app

# Copy contents of current directory into container /resize  
#COPY  resize.py .
ADD resize.py /
RUN pip install Pillow

#ARG image_ID="/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/00000013_005.png"
ENV IMAGE_ID="/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/00000013_005.png"
#ENTRYPOINT ["python", resize.py"]

#run resize.py when container launches
CMD ["python", "resize.py"]
