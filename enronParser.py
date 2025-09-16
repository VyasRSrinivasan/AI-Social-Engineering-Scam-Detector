import numpy
import glob
import os
import email
from email import parser, policy
import json
from email.parser import BytesParser

from email.message import EmailMessage
import re
import pandas as pd
from pandas import DataFrame as df


def load_text_file(path, filename):
    with open(os.path.join(path, filename), "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
   
    eSubject = ""
    eFrom = ""
    eBody = ""
    eTo = ""

    for i, line in enumerate(text.splitlines()):
        l = line.strip()
        if not eSubject and l.lower().startswith("subject:"):
            eSubject = l.split(":", 1)[1]
            bodyL = l[i+1:]
            break

    eBody = "".join(bodyL).strip()
    eURLs = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', eBody)
    eLabel = ""
    if "spam" in filename:
        eLabel = "spam"

    elif "ham" in filename:
        eLabel = "ham"
    #print("Body: ", eBody)
    return {
        "File Name": filename,
        "From": eFrom,
        "To": eTo,
        "Reply To": "",
        "Subject": eSubject,
        "Date": "",
        "Message ID": "",
        "Body": eBody,
        "URLs": eURLs,
        "URL Count": len(eURLs),
        "Attachments": "",
        "Attachment Count": 0,
        "Content Type": "text/plain",
        "Content Language": "",
        "Label": eLabel
    }




resultSpam = []
resultHam = []

for i in range(1,2):
    basePath = "/Users/VyasSrinivasan/AI-Social-Engineering-Scam-Detector/data/data_llm/EnronSpam/enron"+ str(i)
    for spamFile in os.listdir(basePath+"/spam/"):
        #print (basePath+"/spam/")
        #print(spamFile)
        spam_list = load_text_file(basePath+"/spam/", spamFile)
        resultSpam.append(spam_list)
    for hamFile in os.listdir(basePath+"/ham/"):
        #print (basePath+"/ham/")
        #print(hamFile)
        ham_list = load_text_file(basePath+"/ham/", hamFile)
        resultHam.append(ham_list)






#print (resultSpam)

df_spam = df(resultSpam)
df_spam.to_csv("/Users/VyasSrinivasan/AI-Social-Engineering-Scam-Detector/data/data_llm/EnronSpam/enron_spam.csv")

df_ham = df(resultHam)
df_ham.to_csv("/Users/VyasSrinivasan/AI-Social-Engineering-Scam-Detector/data/data_llm/EnronSpam/enron_ham.csv")
#print (resultHam[0][0])

