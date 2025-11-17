# Movie Review Sentiment Analyzer (BERT + Flask)

After exploring Attention and Self-Attention, I wanted to push further — by building an **end-to-end Transformer project** for movie review sentiment analysis.

This project fine-tunes **BERT** on the **IMDB Movie Review dataset** and deploys it using **Flask** as a real-time web app that predicts whether a review is **Positive** or **Negative**.

---

## • Steps Followed

1. **Model Fine-Tuning**
   - Used `BertForSequenceClassification` from Hugging Face.
   - Tokenized input using `BertTokenizer` with max length 128.
   - Trained using AdamW optimizer on IMDB dataset.
   - Saved fine-tuned model and tokenizer for deployment.

2. **Evaluation Phase**
   - Used **Expected Calibrated Error (ECE)** to understand the real calibration of the model.
   - Used **Brier Score** to understand how close the predicted probabilities are to actual labels.

3. **Backend with Flask**
   - Built Flask API with routes:
     - `/` → homepage  
     - `/predict` → handles user input and inference  
     - `/health` → quick status check  
   - Loaded model with PyTorch for on-demand predictions.

4. **Frontend Interface**
   - Created using **HTML, CSS, Jinja2**.  
   - Dark-themed UI with a clean “About” sidebar.  
   - Takes a review as input and displays prediction instantly.

---

## • Learnings
- Fine-tuning **BERT** improves contextual understanding for text sentiment.  
- Flask bridges research and production efficiently.  
- A simple UI makes NLP models intuitive and easy to demonstrate.  

---

## • Tech Stack
- Python, Flask  
- PyTorch, Transformers  
- HTML, CSS, Jinja2  

---

**#NLP #BERT #Transformers #Flask #MachineLearning #DeepLearning #AI #DataScience #WebApp #SentimentAnalysis**


<video src="demo.mp4

https://github.com/user-attachments/assets/b1b2e2a2-8ad1-4952-ba1f-64dc98bfa0e8


