# llm-phishing-detection-benchmark

This repository contains a Python implementation for evaluating
large language models on phishing email detection using a
multi-source public dataset.

## Models Evaluated
- GPT-5 Nano
- Claude 3 Haiku
- Gemini 2.5 Flash-Lite

## Dataset
Public multi-source corpus (Enron, SpamAssassin, Nazario, etc.)
Stored as ham_spam.xlsx.

## How to Run
1. Create a virtual environment
2. Install dependencies
3. Set API keys as environment variables
4. Run evaluate_llms.py
