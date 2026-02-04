# Sentiment Analysis of Flipkart Product Reviews 📊📝

## 📌 Project Overview
This project performs **sentiment analysis on real-time Flipkart product reviews** using
Natural Language Processing (NLP) techniques.  
The goal is to classify customer reviews as **positive or negative** and extract meaningful
insights from negative feedback to understand customer pain points.

---

## 🎯 Objectives
- Classify customer reviews into **positive** and **negative**
- Analyze negative reviews to identify common issues
- Build an end-to-end NLP pipeline from raw text to predictions
- (Optional) Provide a simple UI using **Streamlit**

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries:**  
  - Pandas, NumPy  
  - NLTK  
  - Scikit-learn  
  - Matplotlib / Seaborn  
- **NLP Techniques:**  
  - Tokenization  
  - Stopword Removal  
  - Lemmatization  
  - TF-IDF Vectorization  
- **Model(s):** Logistic Regression / Naive Bayes (as used)  
- **Deployment:** Streamlit (optional)

---

## ⚙️ Project Workflow
1. **Data Collection**  
   - Real-time scraped Flipkart review dataset (provided)

2. **Data Cleaning**
   - Handling missing values
   - Removing duplicates
   - Cleaning text data

3. **Text Preprocessing**
   - Lowercasing
   - Tokenization
   - Stopword removal
   - Lemmatization

4. **Feature Extraction**
   - TF-IDF Vectorization

5. **Model Training**
   - Train-test split
   - Model fitting

6. **Model Evaluation**
   - Accuracy score
   - Classification report
   - Confusion matrix

7. **Insights**
   - Identification of common issues from negative reviews

---

## 📊 Results
- Model Accuracy: **XX%**
- Successfully classified customer sentiment
- Extracted meaningful insights from negative reviews to highlight customer pain points

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the notebook
jupyter notebook

(Optional) Run Streamlit App
streamlit run app/app.py

📁 Project Structure
Sentiment-Analysis-Flipkart/
│── data/
│── notebooks/
│── app/
│── requirements.txt
│── README.md
│── .gitignore
