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
### Load & Combine Datasets
Loaded and merged all four datasets into one unified dataset with consistent labels (Spam, Ham)
### Data cleaning
- Lowercased, trimmed whitespace, and eliminated missing values
Mapped *spam* and *ham* labels into binary (Spam = 0, Ham = 1)
- Balanced the dataset using undersampling to lower bias toward non-spam messages
### Train/test split
Split the dataset into 80% training & 20% testing to evaluate generalization performance.
### Feature extraction
Applied TF-IDF vectorization to transform raw text messages into numerical feature vectors. 
Dropped English stopwords to improve model focus on meaningful tokens.
### Baseline Model (Logistic Regression)
Trained a Logistic Regression classifier on TF-IDF features.
Measured accuracy, precision, recall, F1 score, and visualized the confusion matrix.
This was a benchmark model. 
### LLM Model (Ollama 'mistral')
Improved the pipeline by integrating an LLM (Mistral) through Ollama for semantic classification. 
Used a carefully crafted prompt: 

"Classify the message as exactly one word: \"Spam\" or \"Ham\". Reply with only that word, no punctuation. If unsure, pick the most likely label."
Tested the LLM's interpretability and compared predictions to the baseline model.

### Model Evaluation
Generated classification reports for both Logistic Regression and LLM models.
Metrics used:
- <u>Accuracy</u>: true predictions out of all predictions made
- <u>Precision</u>: the number of predicted *spam* messages that were actually *spam*
- <u>Recall</u>: the number of *spam* messages that were successfully identified
- <u>F1-score</u>: harmonic mean of precision and recall

## Results    

<span style="font-size: 3em; font-weight: normal;">Logistic Regression: </span>

|                   |precision | recall | f1-score | support  |
|:-----------------:|:--------:|:------:|:--------:|:--------:|
|**Spam**           | 0.98     | 0.97   | 0.97     | 458      |
|**Ham**            | 0.96     | 0.98   | 0.97     | 439      |
|                   |          |        |          |          |
|**accuracy**       |          |        | 0.97     | 897      |
|**macro avg**      | 0.97     | 0.97   | 0.97     | 897      |
|**weighted avg**   | 0.97     | 0.97   | 0.97     | 897      |

<span style="font-size: 3em; font-weight: normal;">LLMs: </span>

|                   |precision | recall | f1-score | support  |
|:-----------------:|:--------:|:------:|:--------:|:--------:|
|**Spam**           | 0.90     | 0.95   | 0.93     | 458      |
|**Ham**            | 0.95     | 0.89   | 0.92     | 439      |
|                   |          |        |          |          |
|**accuracy**       |          |        | 0.92     | 897      |
|**macro avg**      | 0.93     | 0.92   | 0.92     | 897      |
|**weighted avg**   | 0.93     | 0.92   | 0.92     | 897      |


## Findings
1. Logistic Regression achieved a strong performance using TF-IDF features
2. LLM ('Mistral') slightly underperformed on overall accuracy but the recall for *Spam* was higher, meaning more scam messages were overlooked.
3. Results suggest that adopting a hybrid approach in which both models — Logistic Regression and LLMs — are combined to further enhance reliability. 

## References
*Zafko. (2025, June 11). PHISHING EMAIL AND SPAM SMS AI DETECTION TOOL. Kaggle. https://www.kaggle.com/code/zafko8/phishing-email-and-spam-sms-ai-detection-tool/notebook*

*Spam SMS classification using NLP. (2024, September 20). Kaggle. https://www.kaggle.com/datasets/mariumfaheem666/spam-sms-classification-using-nlp*

*Al-Subaiey, A., Al-Thani, M., Alam, N. A., Antora, K. F., Khandakar, A., & Zaman, S. A. U. (2024, May 19). Novel Interpretable and Robust Web-based AI Platform for Phishing Email Detection. ArXiv.org. https://arxiv.org/abs/2405.11619*

*Spam email classification. (2023, December 22). Kaggle. https://www.kaggle.com/datasets/ashfakyeafi/spam-email-classification*

*UCI SMS Spam collection data set. (2021, June 8). Kaggle. https://www.kaggle.com/datasets/adityakaranth/uci-sms-spam-collection-data-set*