from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import os
import re
from nltk.stem.porter import PorterStemmer

# Load NLTK stemmer
ps = PorterStemmer()

# Load custom stopwords
stopwords_path = os.path.join(os.path.dirname(__file__), 'combined_stopwords.txt')
custom_stopwords = set()
if os.path.exists(stopwords_path):
    with open(stopwords_path, "r", encoding="utf-8") as f:
        custom_stopwords = set(line.strip() for line in f if line.strip())

def transform_text(text):
    text = text.lower()
    # Tokenize alphanumeric
    text = re.findall(r'\w+', text)
    
    # alphanumeric filter & stopword filter
    text = [i for i in text if i.isalnum() and i not in custom_stopwords]
    
    # stemming
    text = [ps.stem(i) for i in text]
    
    return " ".join(text)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Load model and vectorizer
base_dir = os.path.dirname(__file__)
tfidf_path = os.path.join(base_dir, 'vectorizer.pkl')
model_path = os.path.join(base_dir, 'model.pkl')

try:
    tfidf = pickle.load(open(tfidf_path, 'rb'))
    model = pickle.load(open(model_path, 'rb'))
except Exception as e:
    tfidf = None
    model = None

class PredictRequest(BaseModel):
    message: str

class PredictResponse(BaseModel):
    is_spam: bool
    response_text: str

@app.post("/api/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
        
    if model is None or tfidf is None:
        raise HTTPException(status_code=500, detail="Model files not found")

    # 1. preprocess
    transformed_sms = transform_text(req.message)
    
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    
    # 3. predict
    result = model.predict(vector_input)[0]
    
    is_spam = bool(result == 1)
    response_text = "Hey hey 😊 I think this is spam" if is_spam else "Oh thanks for that, you seem genuine."
    
    return PredictResponse(is_spam=is_spam, response_text=response_text)
