# 📊 Poll Results Visualizer (AI-Powered Real-Time Analytics System)

![Python](https://img.shields.io/badge/Python-3.9-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Status-Live-success)

---

## 🚀 Live Demo

🌐 Dashboard: https://poll-results-visualizer-ai-gurhsyx6wjqdechyafyshv.streamlit. 

---

## 📌 Project Overview

The Poll Results Visualizer is a full-stack, AI-powered data analytics platform designed to collect, process, and visualize poll/survey data in real time.

This system simulates how modern organizations convert raw user feedback into actionable insights using backend APIs, databases, NLP techniques, and interactive dashboards.

---

## 🎯 Objectives

- Build a real-time data pipeline from user input to visualization  
- Perform sentiment analysis on textual feedback  
- Present insights using interactive dashboards  
- Deploy a full-stack application accessible via public URLs  

---

## 🔥 Key Features

### 🗳 Data Collection
- Real-time poll submission via REST API (FastAPI)
- Inputs include:
  - Name
  - Tool preference
  - Region
  - Rating
  - Feedback text

### 🧠 AI-Based Sentiment Analysis
- Uses TextBlob (NLP)
- Classifies feedback into:
  - Positive
  - Neutral
  - Negative

### 📊 Data Visualization
- Built using Streamlit + Plotly
- Includes:
  - Bar charts (tool popularity)
  - Pie charts (vote share)
  - Heatmaps (region-wise analysis)
  - Histograms (rating distribution)
  - Sentiment charts

### 🔄 Real-Time Updates
- Dashboard auto-refreshes
- API-driven architecture

### 📝 Insights Blog
- Markdown-based reporting system
- Displays key findings and recommendations

### ☁️ Deployment
- Backend: Render
- Dashboard: Streamlit Cloud

---

## 🧠 Tech Stack

Backend:
- FastAPI
- SQLite

Frontend:
- Streamlit

Data Processing:
- Pandas
- NumPy

Visualization:
- Plotly

AI / NLP:
- TextBlob

Deployment:
- Render
- Streamlit Cloud

---

## 🏗 Architecture

User → FastAPI API → SQLite Database → Sentiment Analysis → Streamlit Dashboard

---

## ⚙️ Installation & Setup

1. Clone Repository
git clone https://github.com/your-username/Poll-Results-Visualizer-AI.git  
cd Poll-Results-Visualizer-AI  

2. Create Virtual Environment
python -m venv venv  
venv\Scripts\activate  

3. Install Dependencies
pip install -r requirements.txt  
python -m textblob.download_corpora  

4. Run Backend
uvicorn api.app:app --reload  

5. Run Dashboard
streamlit run dashboard/app.py  

---

## 📊 API Endpoints

GET / → Check API  
POST /submit → Submit poll  
GET /results → Tool vote counts  
GET /all-data → Full dataset  
GET /export → Export for BI tools  

---

## 📊 Key Insights

- Tool popularity trends  
- Sentiment classification  
- Region-wise analysis  
- Rating distribution  
- Trending tool detection  

---

## 🚀 Future Improvements

- Authentication system  
- Advanced ML sentiment models  
- Mobile app  
- Power BI integration  
- Public polling system  
- Real-time streaming  

---

## 💼 Use Cases

- Customer feedback analysis  
- Product surveys  
- Polling systems  
- Employee feedback analytics  

---

## 👩‍💻 Author

Arpita Bhendigeri  

---

