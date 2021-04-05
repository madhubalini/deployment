

import pandas as pd
import streamlit as st 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle 
from pickle import dump
from pickle import load

st.title('Model Deployment:Book Recommendation')


def user_input_features():
    Name = st.text_input("Title")
   
    return Name
    
df = user_input_features()
st.subheader('recommended books')
st.write(df)

# load the model from disk
pickle_out = open("bookrec.pkl", mode = "wb") 
pickle.dump(genre_recommendation, bookrec.pkl)
prediction = pickle_out(df)


st.subheader('Predicted Result')
st.write(prediction)

