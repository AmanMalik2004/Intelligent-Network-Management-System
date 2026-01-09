import streamlit as stl
import pandas as pd
import re
from log_parser import parse_logs
from chatops import chat
from summarizer import summarize_logs
from alert_classifier import classify_alert
from generate_logs import generate_logs

def is_valid_log_message(text):

    if not text or len(text.strip()) < 3:
        return False

    t = text.strip().lower()

    if re.fullmatch(r"(.)\1{3,}", t):
        return False

    if not re.search(r"[aeiou]", t):
        return False

    single_word = t.replace("-", "")
    if " " not in t and len(single_word) > 5:
        known = [
            "error","warning","info","router","switch","firewall","cpu","memory",
            "packet","loss","down","fail","alert","system","server","reboot",
            "backup","login","unauthorized","dhcp","interface","eth0","eth1"
        ]
        if single_word not in known:
            return False

    if re.search(r"\d", t):
        return True

    keywords = [
        "error","warning","down","up","cpu","memory","packet","loss","router",
        "switch","firewall","login","logged","interface","disk","usage","fail",
        "failure","reboot","unauthorized","dhcp","connection","timeout"
    ]
    if any(k in t for k in keywords):
        return True

    if " " in t:
        return True

    return False



stl.title("Intelligent Network Management System")

uploaded_file = stl.file_uploader("Upload your log file(optional)", type=["txt"])
use_auto = stl.checkbox("Generate sample logs")

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")

    with open("uploaded_file_backup.txt", "w") as f:
        f.write(content)

    df = parse_logs("uploaded_file_backup.txt")

elif use_auto:
    df = generate_logs()

else:
    df = parse_logs("sample_logs.txt")

stl.subheader("View Logs")
choice = stl.radio("Choose which logs to display:", ["Recent 20 Logs", "Old 20 Logs"])

if choice == "Recent 20 Logs":
    stl.dataframe(df.tail(20))
else:
    stl.dataframe(df.head(20))

df = parse_logs("sample_logs.txt")
stl.subheader("Parsed Logs")
stl.dataframe(df)

stl.subheader("Log Summary")
if stl.button("Generate Summary"):
    summary = summarize_logs(df)
    stl.write(summary)

stl.subheader("Network Assitant")
userInput = stl.text_input("Ask something (e.g. 'summary', 'recent alerts', 'classify latest')")
if userInput:
    response = chatbot(df, userInput)
    stl.write(response)

stl.subheader("Test Alert Classification")
testMsg = stl.text_input("Enter a custom log message to classify:")
if stl.button("Classify Message"):
    if not is_valid_log_message(testMsg):
        stl.error("Incorrect input. Please enter a valid log message.")
    else:
        rslt = classify_alert(testMsg)
        stl.success(f"Classification: **{rslt}**")