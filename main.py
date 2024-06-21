import streamlit as st
from PIL import Image
import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def analyse(image):
    # Perform inference
    results = model(image)

    # Get detected objects
    detections = results.pandas().xyxy[0]  # Extract results as a pandas DataFrame

    # Prepare list of objects detected
    object_list = []
    for idx, detection in detections.iterrows():
        label = detection['name']
        confidence = detection['confidence']
        box = detection[['xmin', 'ymin', 'xmax', 'ymax']].values.astype(int)
        object_list.append(label)
       # object_list.append(f'{label} (Confidence: {confidence:.2f}) at {box}')

    return object_list

st.title("Image Upload and Analysis")

# Upload image section
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # To read image file bytes
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    

    if st.button('Analyse'):
        st.write("Image is being analyzed..")
        object_list = analyse(image)
        st.write("Detected Objects: ")
        for obj in object_list:
            st.write(f"- {obj}")