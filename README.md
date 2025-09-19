# Social Engineering Scam Detection using LLMs

## Objective
There is a social engineering tactic that cybercriminals use called phishing, where they use manipulation tactics to gather personal information. 
The goal of this this scam detection tool is to leverage LLMs paired with machine learning models to accurately identify phishing emails and texts by classifying it as either "spam" or "ham".

## Datasets
- Phishing Email Dataset
- Spam SMS Classification Using NLP
- Spam Email Classification
- UCI SMS Spam Collection

## Methodology
* Load & Combine Datasets
* Data cleaning
* Feature extraction
* Baseline Model (Logistic Regression)
* LLM Model
* Model Evaluation
Logistic Regression: 

|     |precision | recall | f1-score | support  |
|:---:|:--------:|:------:|:--------:|:--------:|
|Spam | 0.98     | 0.97   | 0.97     |  458     |
|Ham  | 0.96     | 0.98   | 0.97     |  439     |
|Ham  | 0.96     | 0.98   | 0.97     |  439     |
|:---:|:--------:|:------:|:--------:|:--------:|
|accuracy        |      |      | 0.97 | 897     |
|macro avg       | 0.97 | 0.97 | 0.97 | 897     |
|weighted avg    | 0.97 | 0.97 | 0.97 | 897     |

LLMs: 
              precision    recall  f1-score   support

        Spam       0.90      0.95      0.93       458
         Ham       0.95      0.89      0.92       439

    accuracy                           0.92       897
   macro avg       0.93      0.92      0.92       897
weighted avg       0.93      0.92      0.92       897

## References
Zafko. (2025, June 11). PHISHING EMAIL AND SPAM SMS AI DETECTION TOOL. Kaggle. https://www.kaggle.com/code/zafko8/phishing-email-and-spam-sms-ai-detection-tool/notebook

Spam SMS classification using NLP. (2024, September 20). Kaggle. https://www.kaggle.com/datasets/mariumfaheem666/spam-sms-classification-using-nlp

Al-Subaiey, A., Al-Thani, M., Alam, N. A., Antora, K. F., Khandakar, A., & Zaman, S. A. U. (2024, May 19). Novel Interpretable and Robust Web-based AI Platform for Phishing Email Detection. ArXiv.org. https://arxiv.org/abs/2405.11619

Spam email classification. (2023, December 22). Kaggle. https://www.kaggle.com/datasets/ashfakyeafi/spam-email-classification

UCI SMS Spam collection data set. (2021, June 8). Kaggle. https://www.kaggle.com/datasets/adityakaranth/uci-sms-spam-collection-data-set