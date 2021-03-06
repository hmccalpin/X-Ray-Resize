#Use Python 3 as parent image
FROM python:3

#Set the working directory to /resize
WORKDIR /resize-app

ADD resize.py /resize-app/
RUN pip install Pillow

#ARG image_ID="/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/images/00000013_005.png"
#ENV IMAGE_ID="/Users/hmccalpin/Desktop/Kaggle_Xray_Dataset/test/"
#ENTRYPOINT ["python", resize.py"]

#run resize.py when container launches
CMD ["python", "resize.py"]
