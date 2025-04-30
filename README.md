🛡️ YarraScan Suite

"YarraScan" is an AI-inspired, simulated "cybersecurity toolkit" designed to scan websites and APK files for vulnerabilities based on the "OWASP Top 10" and mobile security best practices.

> Built by [Raghav](https://github.com/yarrayt) as a BTech 3rd year cybersecurity practical project.

🚀 Features

🔍 Web Scanner (OWASP Top 10 based)
- SQL Injection detection
- XSS (Cross Site Scripting)
- Security misconfiguration
- Sensitive data exposure
- Broken authentication & access control

📱 APK Analyzer
- Detects dangerous permissions
- Insecure file storage practices
- Exposed secrets (e.g., hardcoded keys)
- Malware-like behavior
- Insecure communication (HTTP)

📊 Risk Scoring System
- Combines web and mobile issues
- Final risk score: 0–100
- Suggests action based on severity

📄 PDF Report Generation
- Summarized findings with formatting
- Downloadable for sharing/submission

🌙 Dark Mode UI
- Technical aesthetic with stylish design
- Mobile responsive layout

💻 Setup Instructions

```bash
git clone https://github.com/yarrayt/Yarra_scan_suite.git
cd Yarra_scan_suite
pip install -r requirements.txt
python app.py

Visit http://127.0.0.1:5000/ in your browser

Login with:
username: admin
password: admin
