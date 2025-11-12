from flask import Flask, render_template, request, url_for
from transformers import BertTokenizer, BertForSequenceClassification
import torch


# ----------------------------------
# Load Model
# ----------------------------------
model_path = r"C:\New folder\bert_sentiment_model\bert_sentiment_model"

tokenizer = BertTokenizer.from_pretrained(model_path)
model = BertForSequenceClassification.from_pretrained(model_path)
model.eval()


app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return "Health is okay", 200


@app.route("/predict", methods = ["POST"])
def predict():
    data = request.form
    text = data["review"]
    input = tokenizer(text, return_tensors = "pt", max_length = 128, truncation = True)
    output = model(**input)
    prediction = torch.argmax(output.logits, dim = 1)
    prediction = prediction.cpu().numpy()[0]
    text_output= f"Positive Review" if prediction == 1 else "Negative Review"
    return render_template("results.html",  prediction = text_output )

if __name__ == "__main__":
    app.run(debug = True)
