import email
from email import parser, policy
import json
from email.parser import BytesParser

from email.message import EmailMessage
import os
import re
import pandas as pd
from pandas import DataFrame as df


def parseEmail(path, eFile):
    with open(os.path.join(path, eFile), "rb") as f:
    # Create a text/plain message
        msg = BytesParser(policy=policy.compat32).parse(f)
        #msg = EmailMessage()
        #msg.set_content(f.read())
    
    eSubject = msg["Subject"] if msg["Subject"] else ""
    eFrom = msg["From"] if msg["From"] else ""
    eTo = msg["To"] if msg["To"] else ""
    eReplyTo = msg["Reply-To"] if msg["Reply-To"] else ""
    eMessageID = msg["Message-Id"] if msg["Message-Id"] else ""
    eDate = msg["Date"] if msg["Date"] else ""
    eContentType = msg["Content-Type"] if msg["Content-Type"] else ""
    eContentLang = msg["Content-Language"] if msg["Content-Language"] else ""
    eBody = getEmailBody(msg)
    eURLs = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', eBody)
    eAttachments = getEmailAttachments(msg)
    email_features = {"File Name": str(eFile),
                        "From": str(eFrom) ,
                        "To": str(eTo),
                        "Reply To": str(eReplyTo),
                        "Subject": str(eSubject),
                        "Date": str(eDate),
                        "Message ID": str(eMessageID),
                        "Body": eBody,
                        "URLs": "".join(map(str, eURLs)),
                        "URL Count": len(eURLs),
                        "Attachments": "".join(map(str, eAttachments)),
                        "Attachment Count": len(eAttachments),
                        "Content Type" : str(eContentType),
                        "Content Language" : str(eContentLang),
                        }
    return email_features

def getEmailBody(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ("text/plain", "text/html"):
                charset = part.get_content_charset() if part.get_content_charset() else ""
                try:
                    return part.get_payload(decode=True).decode(charset, errors="replace")
                except (LookupError, UnicodeDecodeError):
                    return part.get_payload(decode=True).decode("utf-8", errors="replace")
    else:
        charset = msg.get_content_charset() if msg.get_content_charset() else ""
        try:
            return msg.get_payload(decode=True).decode(charset, errors="replace")
        except (LookupError, UnicodeDecodeError):
            return msg.get_payload(decode=True).decode("utf-8", errors="replace")

def getEmailAttachments(msg):
    attachments = []

    
    for part in msg.walk():
        if part.get_content_maintype() == "multipart":
            continue

        disposition = part.get("Content-Disposition", "")
        filename = part.get_filename()

        if disposition == "attachment" or (disposition == "inline" and filename) or filename:
            
            content_type = part.get_content_type()
            payload = part.get_payload(decode=True) or b""

            attachments.append({
                "filename": filename or "",
                "content_type": content_type,
                "size": len(payload) if payload else 0,

            })
    return attachments

path = "/Users/VyasSrinivasan/AI-Social-Engineering-Scam-Detector/data/data_llm/PhishingPot/"
#print (os.listdir(phishingPotPath))

allEmails = []
for file in os.listdir(path):
    #print(file)
    emlFile = parseEmail(path, str(file))
    allEmails.append(emlFile)

df = pd.DataFrame(allEmails[:60])
outputFile = "/Users/VyasSrinivasan/AI-Social-Engineering-Scam-Detector/data/data_llm/PhishingPot/phishing_pot_emails.csv"
df.to_csv(outputFile)
'''
with open(outputFile, "w") as f:
    json.dump(allEmails[:60], f)
'''
print ("Extracted ", len(df), " emails into ", outputFile)