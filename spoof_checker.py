import re

def check_spoofing(header_text):
    issues = []

    if "SPF=fail" in header_text or "spf=fail" in header_text:
        issues.append("SPF check failed")

    if "dkim=fail" in header_text.lower():
        issues.append("DKIM check failed")

    if "dmarc=fail" in header_text.lower():
        issues.append("DMARC check failed")

    if "Return-Path" in header_text and "From" in header_text:
        from_field = re.findall(r"From:\s.*", header_text)
        return_path = re.findall(r"Return-Path:\s.*", header_text)
        if from_field and return_path and from_field[0] != return_path[0]:
            issues.append("Return-Path and From mismatch")

    return issues

if __name__ == "__main__":
    with open("sample_email_headers.txt", "r") as file:
        headers = file.read()
    
    issues_found = check_spoofing(headers)
    if issues_found:
        print("⚠️ Possible Spoofing Detected:")
        for issue in issues_found:
            print(f"- {issue}")
    else:
        print("✅ Email appears safe.")
