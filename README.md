
---

# Cat and Dog Image Classification using Deep Learning with SVM

## Project Description

In this project, I developed a deep learning model using SVM with L2 regularization and hinge loss to classify cat and dog images, achieving robust and efficient image classification. A Streamlit app is included for easy interaction with the model.

## Introduction

This project aims to classify images of cats and dogs using a hybrid approach that integrates deep learning with Support Vector Machine (SVM) techniques. The model is designed to leverage the strengths of deep learning for feature extraction and the robustness of SVM with L2 regularization and hinge loss for classification. A Streamlit app provides a user-friendly interface to interact with the model.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Raghavan-B/PRODIGY_ML_03.git
   cd PRODIGY_ML_03
   ```

2. Create a virtual environment and activate it:
   ```bash
   conda create -p venv
   conda activate venv 
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Streamlit App

The project includes a Streamlit app for easy interaction with the model. To run the Streamlit app, follow these steps:

1. Ensure your virtual environment is activated.

2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

3. Open your web browser and go to `http://localhost:8501` to interact with the app.

## Model Training

The model training process involves the following steps:

1. **Data Loading:** Load and preprocess the dataset of cat and dog images.
2. **Feature Extraction:** Use a deep learning model (e.g., CNN) to extract features from the images.
3. **SVM Classification:** Train an SVM with L2 regularization and hinge loss on the extracted features.
4. **Model Evaluation:** Evaluate the model's performance on a test set using accuracy and other relevant metrics.

## Evaluation

The model's performance is evaluated using accuracy as a metric. This model gives an accuracy of **96%**
