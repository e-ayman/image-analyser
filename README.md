# Image Component Analyzer

## Description

this is a Streamlit based application that allows users to upload an image and, upon clicking a button, displays a list of names of each component present in the image.

## Features

### User Interface

#### Image Upload
- A widget is provided for the user to upload an image file.
- Supported formats include common image types such as JPEG, PNG, etc.

#### Analyse Image Button
- A button labelled "Analyse" is included.
- When clicked, this button triggers the image analysis process.

### Results Display
- A list of the names of each component detected in the uploaded image is displayed.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Streamlit
- Torch
- PIL (Python Imaging Library)
- OpenCV
- Matplotlib

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/image-component-analyzer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd image-component-analyzer
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Streamlit application:
    ```bash
    streamlit run app.py
    ```
2. Open a web browser and go to the displayed URL (usually `http://localhost:8501`).


## YOLOv5 Model Usage

The application utilizes the YOLOv5 model for object detection.



