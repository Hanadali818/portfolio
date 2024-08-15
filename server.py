from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Get the API key and email from environment variables
RESEND_API_KEY = os.getenv('RESEND_API_KEY')
EMAIL_TO = os.getenv('EMAIL_TO')

def send_email(name, email, message):
    url = "https://api.resend.com/emails"  # Example endpoint, adjust as needed
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "from": "onboarding@resend.dev",
        "to": EMAIL_TO,
        "subject": "Contact Form Submission",
        "text": f"Name: {name}\nEmail: {email}\nMessage: {message}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return True
        else:
            print(f"API error: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    if send_email(name, email, message):
        return redirect(url_for('thank_you'))
    else:
        return "There was an error sending your message."

@app.route('/thanks')
def thank_you():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)

