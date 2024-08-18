# Contact Management System

## Overview

The Contact Management System is a Flask-based web application that allows users to submit contact information through a web form. The application processes submissions by storing them in a SQLite database, logging them in a CSV file, and sending email notifications using the Resend API. All timestamps are recorded in Central Time.

## Project Structure

- `server.py`: The main application file that initializes the Flask app, defines routes, and handles form submissions.
- `models.py`: Contains the SQLAlchemy model for storing contact information in the database.
- `utils.py`: Includes utility functions for sending emails and writing data to a CSV file.
- `.env`: Stores environment variables such as the Resend API key and email recipient.

## How It Works

### 1. Initialization

- **Flask App Initialization**: The Flask application is initialized in `server.py`. It loads environment variables using `python-dotenv` and configures the SQLite database with SQLAlchemy.
- **Database Setup**: The `db` object is initialized with the Flask app, and the `create_tables` function is used to create the database tables before the first request.

### 2. Form Submission

- **Contact Route**: When a user submits the contact form, the data is sent to the `/contact` route via a POST request.
- **Data Handling**: The form data (name, email, message) is captured, and a new `Contact` record is created and added to the SQLite database.
- **CSV Logging**: The form data is also appended to a CSV file for record-keeping.
- **Email Notification**: An email notification is sent to the specified recipient using the Resend API. This here is the link to their documentation: https://resend.com/docs/introduction.

### 3. Timestamps

- **Timezone Handling**: Timestamps are recorded in Central Time (`America/Chicago`) using the `pytz` library. This ensures that all time-related information is consistent with the Central Time Zone.

## Dependencies

- Flask
- Flask-SQLAlchemy
- python-dotenv
- pytz
- Resend API

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
