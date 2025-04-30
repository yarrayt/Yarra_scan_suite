from fpdf import FPDF

def get_suggestions(score):
    if score < 30:
        return "Low risk. No immediate action needed."
    elif score < 70:
        return "Moderate risk. Please investigate further."
    else:
        return "High risk! Immediate attention required."

def generate_pdf(web_report, apk_report, score, suggestion):
    pdf = FPDF()
    pdf.add_page()

    # Header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "YarraScan Cybersecurity Report", ln=True, align='C')
    pdf.ln(5)

    # Summary Section
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Target: {web_report.get('target', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"Total Risk Score: {score}/100", ln=True)
    pdf.cell(0, 10, f"Suggestion: {suggestion}", ln=True)
    pdf.ln(8)

    # Web Scan Issues
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Web Scan Issues", ln=True)
    pdf.set_font("Arial", '', 12)

    web_issues = web_report.get('issues', [])
    if web_issues:
        for issue in web_issues:
            pdf.cell(0, 10, f"Issue: {issue['type']}", ln=True)
            pdf.cell(0, 10, f"Severity: {issue['severity']}", ln=True)
            pdf.multi_cell(0, 10, f"Suggestion: {issue['suggestion']}")
            pdf.ln(2)
    else:
        pdf.cell(0, 10, "No web vulnerabilities detected.", ln=True)

    # APK Scan Summary
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "APK Scan Summary", ln=True)
    pdf.set_font("Arial", '', 12)

    def write_list(title, items):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, title, ln=True)
        pdf.set_font("Arial", '', 12)
        if items:
            for item in items:
                pdf.multi_cell(0, 10, f"- {item}")
        else:
            pdf.cell(0, 10, "None found.", ln=True)
        pdf.ln(2)

    if apk_report:
        write_list("Dangerous Permissions", apk_report.get('permissions', []))
        write_list("Storage Issues", apk_report.get('storage_issues', []))
        write_list("Cryptographic Weaknesses", apk_report.get('crypto_warnings', []))
        write_list("Exposed Secrets", apk_report.get('secrets_found', []))
        write_list("Insecure URLs", apk_report.get('url_security', []))
        write_list("Malware Signatures", apk_report.get('malware_signs', []))
    else:
        pdf.cell(0, 10, "No APK scan data provided.", ln=True)

    path = "report.pdf"
    pdf.output(path)
    return path
