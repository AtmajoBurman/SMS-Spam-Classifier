import streamlit as st
import pickle
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


tokenizer = RegexpTokenizer(r'\w+')

with open("combined_stopwords.txt", "r", encoding="utf-8") as f:
    custom_stopwords = set(line.strip() for line in f if line.strip())

def transform_text(text):
    text = text.lower()
    text = tokenizer.tokenize(text)

    # alphanumeric filter
    text = [i for i in text if i.isalnum()]

    # stopword filter
    text = [i for i in text if i not in custom_stopwords]

    # stemming
    text = [ps.stem(i) for i in text]

    return " ".join(text)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")