AUTO-GEAR

Local email automation and scheduling written in Python.

AUTO-GEAR is a lightweight email automation tool that runs locally and uses SMTP to send emails immediately, at a scheduled time, or on a recurring interval.

The project originally started as a network-alert bot and was later expanded into a general-purpose email automation tool.

Some portions of the code were developed with AI assistance. The project structure, concept, and core implementation are my own.

Features
Send emails through SMTP
Schedule emails for a specific date and time
Send recurring emails
Run scheduled jobs in background threads
Attach files to emails
Add BCC recipients
Use a custom bot name
Load App Passwords from a local file
Google SMTP support
Outlook SMTP support
Custom SMTP server support
Network alert functionality
How It Works

AUTO-GEAR creates a background thread for each scheduled email job.

Create Email
     │
     ▼
Configure Schedule
     │
     ▼
Background Worker
     │
     ├── Wait for scheduled time
     ├── Connect to SMTP
     ├── Authenticate
     ├── Send email
     └── Repeat if recurring


The main program remains available while scheduled jobs run in the background.

Scheduling
Delayed Emails

You can specify an exact date and time for the first delivery.

YYYY-MM-DD HH:MM

Example:
2026-10-25 14:30

Recurring Emails

Recurring messages can run at an interval of:

Minutes
Hours
Days

For example:

Every 10 minutes
Every 2 hours
Every 3 days

SMTP Support

AUTO-GEAR currently supports:

Provider	SMTP Server	Port
Google	smtp.gmail.com	587
Outlook	smtp-mail.outlook.com	587
Custom	User-defined	User-defined

TLS is enabled when connecting to the supported SMTP servers.

Authentication

AUTO-GEAR supports App Password authentication.

You can either enter the App Password manually or load it from a local file.

/path/to/app_password.txt


Do not commit credentials to the repository.

Recommended .gitignore entries:

.env
secrets/
__pycache__/
*.pyc

Installation
Requirements
Python 3.x
An SMTP-enabled email account
App Password or compatible SMTP credentials

AUTO-GEAR currently uses Python's standard library, so no external packages are required.

Clone
git clone https://github.com/YOUR-USERNAME/AUTO-GEAR.git
cd AUTO-GEAR

Run
python auto_gear.py


On some systems:

python3 auto_gear.py

Usage

After starting AUTO-GEAR, select your SMTP provider and authenticate your account.

The main menu provides:

1. Send / Schedule an email
2. Send a system log/alert
3. Exit Program


From there, you can configure:

Bot Name
Recipient
Subject
Message
Attachment
BCC
Recurring Schedule
Delayed Start Time

Project Structure
AUTO-GEAR/
├── auto_gear.py
├── README.md
├── LICENSE
└── .gitignore

Current Limitations

AUTO-GEAR is currently a command-line application.

Scheduled jobs are stored in memory.
Jobs are lost when the program exits.
Recurring jobs are not persistent.
There is currently no GUI.
There is no job cancellation system.
Timezone handling is basic.
Roadmap
 Persistent scheduled jobs
 Job IDs and management
 Job cancellation
 Pause and resume
 Improved logging
 Configuration files
 Secure credential storage
 Timezone support
 HTML email support
 Email templates
 GUI
AI-Assisted Development

Some portions of AUTO-GEAR were developed or refined with AI assistance.

The overall project concept, structure, architecture, and development direction were created by the author.

License

This project is licensed under the MIT License.

See LICENSE for details.

Disclaimer

AUTO-GEAR is intended for legitimate email automation, monitoring, notification, and alerting purposes.

Users are responsible for complying with the policies of their SMTP provider and all applicable laws.
