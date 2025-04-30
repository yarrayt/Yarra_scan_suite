def analyze(filepath):
    report = {
        'filename': filepath,
        'permissions': [],
        'storage_issues': [],
        'crypto_warnings': [],
        'url_security': [],
        'secrets_found': [],
        'malware_signs': [],
        'risk': 0
    }

    # Simulate permissions
    dangerous_perms = ['READ_SMS', 'RECORD_AUDIO', 'ACCESS_FINE_LOCATION', 'READ_CONTACTS']
    report['permissions'] = dangerous_perms
    report['risk'] += len(dangerous_perms) * 5

    # Simulate insecure storage (e.g., storing sensitive data in plaintext)
    report['storage_issues'].append("Plaintext passwords found in internal storage")
    report['risk'] += 10

    # Simulate crypto issues
    report['crypto_warnings'].append("Uses outdated cipher: DES")
    report['crypto_warnings'].append("Hardcoded encryption key detected")
    report['risk'] += 10

    # Simulate hardcoded secrets
    report['secrets_found'].append("API key exposed: ABC123XYZ")
    report['risk'] += 10

    # Simulate insecure network communication
    report['url_security'].append("Uses HTTP instead of HTTPS")
    report['risk'] += 5

    # Simulate malware patterns
    report['malware_signs'].append("Background service auto-starts on boot")
    report['malware_signs'].append("Communicates with known blacklisted IP")
    report['risk'] += 15

    return report
