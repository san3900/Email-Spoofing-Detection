 Email Spoofing Detection and Alert System

A Python-based tool to detect spoofed email headers using SPF, DKIM, and DMARC validation. This tool flags forged emails and alerts users, helping to prevent phishing attacks.

## 🔍 Features
- Analyzes email headers from .txt files
- Validates SPF, DKIM, and DMARC records
- Highlights anomalies in header structure
- Optional Flask UI for visual alerts
- Useful for cybersecurity awareness and filtering

## 📦 Tech Stack
- Python
- Regex, SMTP
- Flask (optional)
- Sample headers and screenshot provided

## 🚀 Usage
```bash
python spoof_checker.py sample_email_headers.txt
