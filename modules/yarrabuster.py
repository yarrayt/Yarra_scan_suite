def scan(target):
    # Simulate checks for OWASP Top 10 vulnerabilities
    issues = [
        {"type": "SQL Injection", "severity": "High", "suggestion": "Use parameterized queries", "risk": 20},
        {"type": "Cross Site Scripting (XSS)", "severity": "Medium", "suggestion": "Sanitize user input", "risk": 15},
        {"type": "Security Misconfiguration", "severity": "Medium", "suggestion": "Disable default accounts and ports", "risk": 10},
        {"type": "Sensitive Data Exposure", "severity": "High", "suggestion": "Use HTTPS and encryption", "risk": 15},
        {"type": "Broken Authentication", "severity": "High", "suggestion": "Implement MFA", "risk": 10},
        {"type": "XXE Injection", "severity": "Low", "suggestion": "Disable external entity parsing", "risk": 5},
        {"type": "Insecure Deserialization", "severity": "Medium", "suggestion": "Avoid accepting serialized objects", "risk": 10},
        {"type": "Broken Access Control", "severity": "High", "suggestion": "Enforce proper access control checks", "risk": 15},
        {"type": "Vulnerable Components", "severity": "Medium", "suggestion": "Keep dependencies updated", "risk": 5},
        {"type": "Insufficient Logging & Monitoring", "severity": "Low", "suggestion": "Log security events properly", "risk": 5}
    ]

    total_risk = sum(item["risk"] for item in issues)

    return {
        'target': target,
        'issues': issues,
        'risk': total_risk
    }
