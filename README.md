# Intelligent Network Management System (INMS)

## 📌 Project Overview

The **Intelligent Network Management System (INMS)** is a Python-based application designed to help network administrators monitor, analyze, and understand network events efficiently. The system processes raw network log files, classifies alerts by severity, generates meaningful summaries, and enables interaction through an AI-powered ChatOps assistant.

The project focuses on automating log analysis and improving network observability using structured data and intelligent rules.

---

## How to Run

* pip install -r requirements.txt
* streamlit run app.py

---

## 🚀 Features

### 1. Log Parsing

* Reads log files line by line
* Uses **Regular Expressions (Regex)** to extract:

  * Timestamp
  * Log level
  * Log message
* Converts logs into a **Pandas DataFrame**
* Enables structured, searchable, and filterable log data

---

### 2. Automated & User-Uploaded Logs

The system supports two log sources:

1. **User-uploaded log files**
2. **System-generated sample logs** (up to 1000 entries)

Users can choose to view:

* Last 10 or 20 log entries
* Oldest 10 or 20 log entries

---

### 3. Alert Classification

A custom alert classifier assigns severity levels based on:

* Keyword detection
* Protocol-specific rules
* Detection of:

  * Errors
  * Packet loss
  * Failures
  * Unauthorized access attempts

---

### 4. Log Summary Generator

The summarization module generates:

* **Log level summary**
* **Most frequent log messages**
* **Latest critical events**

---

### 5. ChatOps AI Assistant

The system includes a ChatOps assistant that understands natural-language queries such as:

* `"summary"`
* `"recent alerts"`
* `"classify latest"`

This enables quick interaction and insight retrieval from logs.

---

### 6. Log Message Validation

The system validates log messages to prevent meaningless or invalid inputs. It checks for:

* Empty or very short messages
* Repeated characters (gibberish)
* Presence of network-related keywords
* Digits and multi-word structure
* Reasonable English words

---

### 7. Streamlit User Interface

The **Streamlit-based UI** provides:

* Parsed log display
* Log summaries
* ChatOps assistant interface
* Alert classification tester
* Options to upload or generate logs

---

## 🧩 Project Architecture

```
├── log_parser.py        # Log parsing and structuring
├── alert_classifier.py # Alert severity classification
├── summarizer.py       # Log summary generation
├── chatops.py          # ChatOps AI assistant
├── app.py              # Streamlit application
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Streamlit**
* **Regular Expressions (Regex)**

---

## 📊 Results

The system successfully:

* Parses raw log files accurately
* Classifies alerts based on severity
* Generates meaningful summaries
* Validates log messages
* Provides an interactive and user-friendly interface

---

## 🔮 Future Enhancements

* Machine Learning–based alert classification
* Real-time log stream processing
* Database integration for log storage
* Advanced visualization dashboards

---

## 📄 Conclusion

The **Intelligent Network Management System (INMS)** is a modular and intelligent solution for network monitoring and log analysis. It demonstrates practical applications of networking concepts, data processing, and intelligent automation, making it well-suited for academic and real-world use.
