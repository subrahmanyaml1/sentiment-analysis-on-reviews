import numpy as np
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

import streamlit as st
import joblib
import os

st.title("Sentiment Analysis on FlipKart Reviews")
text = st.text_input("Enter the Review")

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "sentiment_flipkart.pkl")

model = joblib.load(model_path)   # ✅ CORRECT

if st.button("Submit"):
    result = model.predict([text])[0]

    if result == 'Positive':
        st.text('Its Positive ( ˶ˆᗜˆ˵ ) ')

    elif result == 'Negative':
        st.text('Its Negative (˚ ˃̣̣̥⌓˂̣̣̥ ) ')

