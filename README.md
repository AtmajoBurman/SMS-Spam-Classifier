<div align="center">
  <h1>🛡️ Spambuster</h1>
  <p><strong>A Premium, ML-Powered Spam Classification Chatbot</strong></p>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
</div>

<br />

## 🌟 Overview

**Spambuster** is an interactive, beautifully designed chatbot that utilizes Machine Learning to classify whether your SMS/email text is *Spam* or *Genuine*. Moving away from standard, rigid machine learning interfaces, Spambuster delivers predictions through a modern **Glassmorphism UI**, engaging micro-animations, and dynamic conversational feedback.

## 🚀 Key Features

- **Beautiful UI/UX:** Powered by Vanilla CSS, featuring frosted glass effects, gradient backgrounds, and the sleek Outfit typeface.
- **Conversational Interface:** Submit your messages like a chat, and receive natural language responses.
- **Robust ML Backend:** Utilizes a pre-trained `scikit-learn` classifier and TF-IDF Vectorizer to accurately flag spam.
- **Serverless Ready:** The entire architecture (React Frontend + FastAPI Backend) is fully configured to be deployed as a single application on **Vercel**.

## 🛠️ Tech Stack

- **Frontend:** React, Vite, Vanilla CSS
- **Backend:** Python, FastAPI, Uvicorn, Pydantic
- **Machine Learning:** `scikit-learn`, `nltk` (PorterStemmer)
- **Deployment:** Vercel (Static Frontend + Serverless Functions)

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

The Vite frontend is pre-configured to proxy `/api` requests to your local FastAPI server. Open the local link provided by Vite to interact with Spambuster!

## 🌍 Deployment (Render + Vercel)

Due to Vercel's strict 250MB size limit for serverless functions, the heavy ML dependencies (`scikit-learn`, `scipy`) require us to decouple the application. 

### 1. Deploy Backend on Render
1. Create an account on [Render](https://render.com).
2. Create a new **Web Service** and connect this repository.
3. Set the Build Command to: `pip install -r requirements.txt`
4. Set the Start Command to: `uvicorn backend.index:app --host 0.0.0.0 --port $PORT`
5. Click **Deploy**. Once deployed, copy the Render URL (e.g., `https://spambuster-api.onrender.com`).

### 2. Deploy Frontend on Vercel
1. Log into [Vercel](https://vercel.com) and click **Add New Project**.
2. Import your GitHub repository.
3. In the **Environment Variables** section, add:
   - Key: `VITE_API_URL`
   - Value: `<Your Render Backend URL>`
4. Click **Deploy**. Vercel will statically host your React app, and it will communicate perfectly with your Render backend!
