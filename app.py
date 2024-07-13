import streamlit as st
from PIL import Image
from keras.models import load_model
import numpy as np
from keras.preprocessing import image

st.set_page_config(page_title= "Cats and Dogs Classifer")

st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #333333;
        text-align: center;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stFileUploader label {
        color: #333333;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


st.write("## Welcome to Cats and Dogs Classifier")

file = st.file_uploader(label="Upload an image of a Dog or Cat to have it recognized",type=["jpg","jpeg","png","webp","jfif"])
model = load_model("model/catsvdogs_model.h5")

def preprocess_and_predict(img):
  img = image.load_img(img,target_size=(100,100))
  img = image.img_to_array(img)
  img = img/255.0
  img = np.expand_dims(img,axis=0)
  y_pred = model.predict(img)
  if y_pred>0:
    return "Dog"
  if y_pred<0:
    return "Cat"
columns = st.columns((2, 1, 2))
if file is not None:
    columns[1].image(Image.open(file))
    if columns[1].button("Submit"):
        y_pred = preprocess_and_predict(file)
        st.success(f"This is a {y_pred} image")
else:
   st.subheader("Upload the image first")


