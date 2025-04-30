from flask import Flask, render_template, request, redirect, session, send_file, url_for
import os
from modules import yarrabuster, apk_auditor, utils

app = Flask(__name__)
app.secret_key = 'yoursecret'
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'admin':
        session['user'] = username
        return redirect('/dashboard')
    return render_template('login.html', error='Invalid credentials')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/scan', methods=['POST'])
def scan():
    if 'user' not in session:
        return redirect('/')

    target = request.form.get('target')
    apk = request.files.get('apk')

    web_report = {}
    apk_report = {}
    risk_score = 0

    if target:
        web_report = yarrabuster.scan(target)
        risk_score += web_report.get('risk', 0)

    if apk:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], apk.filename)
        apk.save(filepath)
        apk_report = apk_auditor.analyze(filepath)
        risk_score += apk_report.get('risk', 0)
        os.remove(filepath)

    suggestions = utils.get_suggestions(risk_score)
    pdf_path = utils.generate_pdf(web_report, apk_report, risk_score, suggestions)

    return render_template('scan_result.html',
                           risk_score=risk_score,
                           suggestions=suggestions,
                           pdf_path=pdf_path)

@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
