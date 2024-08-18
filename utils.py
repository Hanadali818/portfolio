import csv
from datetime import datetime
import os
import resend
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

RESEND_API_KEY = os.getenv('RESEND_API_KEY')
EMAIL_TO = os.getenv('EMAIL_TO')

# Resend API setup
resend.api_key = RESEND_API_KEY

def send_email(name, user_email, message):
    data = {
        "from": "onboarding@resend.dev",
        "to": [EMAIL_TO],
        "subject": "Contact Form Submission",
        "text": f"Name: {name}\nEmail: {user_email}\nMessage: {message}"
    }
    try:
        response = resend.Emails.send(data)
        return response
    except Exception as e:
        print(f"Error sending email: {e}")

def write_to_csv(name, email, message):
    filename = 'contact_submissions.csv'
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['name', 'email', 'message', 'datetime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'name': name, 'email': email, 'message': message, 'datetime': datetime.now()})

