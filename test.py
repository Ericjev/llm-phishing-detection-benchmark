import certifi
import os
import time
import pandas as pd
from collections import Counter

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from openai import OpenAI
from anthropic import Anthropic
from google import genai


df = pd.read_csv("spam_ham_dataset.csv")
#df["label"] = df["label"].str.lower()

emails = df["email"].tolist()
true_labels = df["label"].tolist()


def build_prompt(email):
    return f"""
You are a cybersecurity email classifier.
Classify the following email as phishing or legitimate or uncertain.
Respond with exactly one word: phishing, legitimate, or uncertain.

Email:
{email}
"""

#Gemini LLM AI
# client = genai.Client(api_key="[GEMINI_API_KEY]")

# def gemini_classify(email):
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=build_prompt(email)
#     )
#     return response.text.strip().lower()


#ChatGPT LLM AI
# openai_client = OpenAI(api_key="[OPENAI_API_KEY]")

# def openai_classify(email):
#     r = openai_client.chat.completions.create(
#         model="gpt-5-nano",
#         messages=[{"role": "user", "content": build_prompt(email)}],
#         temperature=0
#     )
#     return r.choices[0].message.content.strip().lower()


#Anthropic Claude LLM AI
# anthropic_client = Anthropic(api_key="[ANTHROPIC_API_KEY]")

# def anthropic_classify(email):
#     r = anthropic_client.messages.create(
#         model="claude-3-haiku",
#         max_tokens=5,
#         temperature=0,
#         messages=[{"role": "user", "content": build_prompt(email)}]
#     )
#     return r.content[0].text.strip().lower()



def evaluate(LLModel_function):
    raw_pred = []
    for e in emails:
        raw_pred.append(LLModel_function(e))
        time.sleep(12)

    counts = Counter(raw_pred)

    processed_pred = [
        "legitimate" if p == "uncertain" else p
        for p in raw_pred
    ]

    return {
        "counts": counts,
        "accuracy": accuracy_score(true_labels, processed_pred),
        "precision": precision_score(true_labels, processed_pred, pos_label="phishing"),
        "recall": recall_score(true_labels, processed_pred, pos_label="phishing"),
        "f1": f1_score(true_labels, processed_pred, pos_label="phishing"),
        "preds": processed_pred
    }

results = {
    #"OpenAI": evaluate(openai_classify),
    #"Anthropic": evaluate(anthropic_classify),
    #"Gemini": evaluate(gemini_classify)
}

for name, r in results.items():
    print(f"\n{name}")
    print("Label counts:", r["counts"])
    print(f"Accuracy:  {r['accuracy']:.4f}")
    print(f"Precision: {r['precision']:.4f}")
    print(f"Recall:    {r['recall']:.4f}")
    print(f"F1-score:  {r['f1']:.4f}")
