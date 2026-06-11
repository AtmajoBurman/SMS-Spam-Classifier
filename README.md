<div align="center">
  <h1>🛡️ Spambuster</h1>
  <p><strong>A Premium, ML-Powered Spam Classification Chatbot</strong></p>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" />
</div>

<br />

<video width="100%" autoplay loop muted playsinline>
  <source src="SMS%20SPAM%20CLASSIFIER_NEW_.mp4" type="video/mp4">
</video>

## 🌟 Overview

**Spambuster** is an interactive, beautifully designed chatbot that utilizes Machine Learning to classify whether your SMS/email text is *Spam* or *Genuine*. We trained multiple models on the popular **Kaggle SMS Spam Collection Dataset**, performed detailed exploratory data analysis (EDA), optimized text vectorization approaches, and deployed the best-performing classifier into a modern, decoupled web application.

Moving away from standard, rigid machine learning interfaces, Spambuster delivers predictions through a modern **Glassmorphism UI**, engaging micro-animations, and dynamic conversational feedback.

## 🚀 Key Features

- **Beautiful UI/UX:** Powered by Vanilla CSS, featuring frosted glass effects, gradient backgrounds, and the sleek Outfit typeface.
- **Conversational Interface:** Submit your messages like a chat, and receive natural language responses.
- **Robust ML Backend:** Utilizes a pre-trained `scikit-learn` classifier (Multinomial Naive Bayes) and TF-IDF Vectorizer to accurately flag spam.
- **Serverless Ready:** The frontend is statically hosted on Vercel while the ML pipeline is securely hosted as a Web Service on Render.

## 🛠️ Tech Stack

- **Frontend:** React, Vite, Vanilla CSS
- **Backend:** Python, FastAPI, Uvicorn, Pydantic
- **Machine Learning:** `scikit-learn`, `nltk` (PorterStemmer)
- **Deployment:** Vercel (Frontend) + Render (Backend API)

---

## 🧠 Machine Learning Pipeline

### 📂 Dataset
We used the **SMS Spam Collection Dataset** from Kaggle, which contains:
- **5,572 SMS messages**
- Labels:
  - **ham** → legitimate message
  - **spam** → unsolicited / promotional message

### 🧹 Data Cleaning & Preprocessing
Before model training, the dataset was thoroughly cleaned using standard NLP preprocessing steps:
- Lowercasing text
- Removing punctuation and custom stopwords
- Tokenization
- Stemming using Porter Stemmer
- Creating additional engineered features: `char_count`, `word_count`, `sentence_count`

This preprocessing ensured the text was standardized and noise-free, allowing models to learn meaningful patterns.

### 📊 Exploratory Data Analysis (EDA)
We analyzed the dataset to understand structural differences between ham and spam messages. Key insights:
- **Spam messages are generally longer** in terms of characters, words, and sentences.
- Word count and character count show a strong positive correlation.
- Spam messages tend to have more structured, paragraph-like content.
- Ham messages exhibit higher variance—some are extremely short, while others are unusually long.
- Length-based features provide useful separability but are not sufficient alone; textual patterns are essential.

### 🔡 Feature Extraction
We experimented with CountVectorizer, default TF-IDF Vectorizer, and TF-IDF with `max_features = 3000`. After comparative evaluation, **TF-IDF with 3000 features consistently provided the best performance**, balancing vocabulary richness with model generalization.

### 🤖 Model Training & Evaluation
Multiple Machine Learning algorithms were trained and compared:

| Algorithm | Observations |
|-----------|--------------|
| **Multinomial Naive Bayes (MNB)** | Consistently top-performing, excellent precision, ideal for sparse TF-IDF matrices. |
| **Bernoulli Naive Bayes (BNB)** | Performed well but inferior to MNB on text data. |
| **Complement Naive Bayes (CNB)** | Strong performance but slightly below MNB. |
| **Random Forest / Extra Trees** | High accuracy/precision, but overfitting signs and slower inference. |
| **Support Vector Classifier (SVC)** | High accuracy, but more computationally heavy. |
| **Logistic Regression** | Solid baseline, stable and reliable across folds. |
| **Boosting (XGBoost/AdaBoost)** | Good accuracy but weaker spam precision relative to Naive Bayes. |

**🏆 Final Model Selection:** **Multinomial Naive Bayes (MNB)** was selected as the final model due to having the highest precision (minimizing false positives), best performance on TF-IDF features, and fast training/inference times.

---

## 💻 Running Locally

To run the application locally, you will need to start both the Python API and the React frontend in two separate terminal windows.

### 1. Start the FastAPI Backend

```bash
# Navigate to the root directory
cd SpamDetector

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server (runs on http://localhost:8000)
uvicorn backend.index:app --reload
```

### 2. Start the React Frontend

```bash
# In a new terminal, navigate to the root directory
cd SpamDetector

# Install Node dependencies
npm install

# Start the Vite development server (runs on http://localhost:5173)
npm run dev
```

The Vite frontend uses an environment variable to locate the API. Create a `.env.local` file in the root directory:
```
VITE_API_URL=http://127.0.0.1:8000
```
Open the local link provided by Vite to interact with Spambuster!

## 🌍 Deployment (Render + Vercel)

Due to Vercel's strict 250MB size limit for serverless functions, the heavy ML dependencies (`scikit-learn`, `scipy`) require us to decouple the application. 

### 1. Deploy Backend on Render
1. Create an account on [Render](https://render.com).
2. Create a new **Web Service** and connect this repository.
3. Leave Root Directory blank.
4. Set the Build Command to: `pip install -r requirements.txt`
5. Set the Start Command to: `uvicorn backend.index:app --host 0.0.0.0 --port $PORT`
6. Click **Deploy**. Once deployed, copy the Render URL (e.g., `https://spambuster-api.onrender.com`).

### 2. Deploy Frontend on Vercel
1. Log into [Vercel](https://vercel.com) and click **Add New Project**.
2. Import your GitHub repository.
3. In the **Environment Variables** section, add:
   - Key: `VITE_API_URL`
   - Value: `<Your Render Backend URL>`
4. Click **Deploy**. Vercel will statically host your React app, and it will communicate perfectly with your Render backend!
