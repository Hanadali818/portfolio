from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
from utils import send_email, write_to_csv
from models import db, Contact

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Set up database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Save to database
    new_contact = Contact(name=name, email=email, message=message)
    db.session.add(new_contact)
    db.session.commit()
    
    # Write to CSV
    write_to_csv(name, email, message)

    # Send email
    send_email(name, email, message)

    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('thanks.html')

if __name__ == '__main__':
    create_tables()  # Create tables when starting the app
    app.run(debug=True)
