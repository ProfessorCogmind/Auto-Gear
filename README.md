#AUTO-GEAR

AUTO-GEAR is a lightweight, locally hosted email automation service written in Python.

It was originally developed as a network-alert email bot, but was expanded into a general-purpose tool for sending emails immediately, scheduling delayed messages, and running recurring email jobs in the background.

The project is designed to run locally from the command line without requiring a web server or external automation platform.

Features
Send emails through SMTP
Support for Google/Gmail SMTP
Support for Outlook SMTP
Custom SMTP server support
App-password file loading
Manual app-password entry
Delayed email delivery
Recurring email delivery
Recurring schedules based on:
Minutes
Hours
Days
Email attachments
BCC recipients
Custom sender/bot names
Temporary email-content files
Background email execution using Python threads
SMTP connection verification before starting
Automatic cleanup of temporary files after one-time deliveries
How It Works

AUTO-GEAR runs as a local command-line application.

The general workflow is:

Start AUTO-GEAR
      |
      v
Select SMTP Provider
      |
      v
Authenticate SMTP Account
      |
      v
Verify SMTP Connection
      |
      v
Main Menu
  /       \
 /         \
Send      System
Email      Alert
  |
  v
Configure Message
  |
  +--> Recipient
  +--> Subject
  +--> Content
  +--> Attachment
  +--> BCC
  |
  v
Configure Schedule
  |
  +--> Immediate
  +--> Delayed
  +--> Recurring
  |
  v
Background Worker
  |
  v
SMTP Transmission


The main process remains available while scheduled or recurring jobs are handled by background threads.

Requirements
Python 3.x
An SMTP-enabled email account
An app password or equivalent SMTP authentication method

The project currently uses Python's standard library, so no external Python packages are required.

Installation

Clone the repository:

git clone https://github.com/yourusername/auto-gear.git
cd auto-gear


Run the program:

python auto_gear.py


Depending on your system, you may need:

python3 auto_gear.py

SMTP Configuration

AUTO-GEAR currently provides three SMTP options:

1. Google
2. Outlook
3. Custom SMTP


Google uses:

smtp.gmail.com:587


Outlook uses:

smtp-mail.outlook.com:587


Custom SMTP servers can be entered manually.

AUTO-GEAR establishes a TLS connection and authenticates before sending mail.

Authentication

AUTO-GEAR supports loading an app password from a local file.

Example:

/path/to/app_password.txt


The file should contain the password without additional formatting.

It can also be entered manually when starting the application.

Do not commit password files, credentials, or other authentication secrets to the repository.

A .gitignore entry such as the following is recommended:

*.txt
.env
__pycache__/
*.pyc


If your project stores temporary files using a specific directory, it is better to ignore that directory instead of every .txt file.

Sending an Email

From the main menu:

What would you like to do:

1. Send / Schedule an email
2. Send a system log/alert
3. Exit Program


Selecting option 1 allows you to configure an email.

You can specify:

Bot name
Recipient
Subject
Email content
Attachment
BCC recipient
Recurring schedule
Delayed start time
Delayed Emails

AUTO-GEAR can delay the initial transmission of an email.

Example:

Enter Date & Time: 2026-10-25 14:30


The background worker calculates the delay and waits until the specified time before transmitting the message.

The expected format is:

YYYY-MM-DD HH:MM

Recurring Emails

Emails can also be configured to repeat indefinitely.

Available intervals include:

Minutes
Hours
Days


For example:

Every 30 minutes
Every 4 hours
Every 2 days


After each successful transmission, the worker calculates the next execution time and waits until the next cycle.

Attachments

AUTO-GEAR supports standard email attachments.

During message configuration:

Do you have an attachment? (y/n):


If enabled, the program asks for the attachment's filename and adds it to the MIME message before transmission.

BCC

Additional recipients can be added through BCC.

The primary recipient is stored separately while the BCC recipient is added to the SMTP recipient list.

This allows the BCC recipient to receive the email without being displayed in the visible To header.

Background Execution

AUTO-GEAR uses Python's threading module to move scheduled email jobs into background threads.

The worker is responsible for:

Waiting for the scheduled start time.
Establishing an SMTP connection.
Authenticating with the SMTP server.
Sending the email.
Closing the SMTP connection.
Calculating the next execution time for recurring jobs.
Repeating until the job is stopped or the process exits.

The main program can therefore return to its menu while a scheduled job is waiting.

Project Structure

A simple repository layout can look like:

AUTO-GEAR/
│
├── auto_gear.py
├── README.md
├── .gitignore
└── LICENSE


Temporary email-content files and credential files should not be committed to the repository.

Technical Notes

The project currently relies entirely on Python's standard library.

Primary modules include:

import os
import smtplib
import threading
import time
from datetime import datetime, timedelta


Email construction is handled using Python's MIME modules:

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


Attachments are encoded using:

from email import encoders


The original project was developed around network-alert functionality. The current implementation keeps that use case available through the system-log/alert workflow while allowing the same underlying engine to be used for general email automation.

Security Considerations

AUTO-GEAR handles SMTP credentials, so credential management is important.

Do not:

Hard-code passwords into the source code.
Commit app-password files.
Commit .env files containing credentials.
Upload credentials through GitHub.
Share SMTP credentials in issues or pull requests.

For production use, credential handling should be improved beyond plain-text local files and terminal input.

Current Limitations

AUTO-GEAR is currently a command-line application.

It does not currently provide:

A graphical interface
A web interface
Persistent job storage
A job-management database
Job cancellation from the main menu
Persistent schedules after the program exits
Advanced cron-style scheduling
Robust timezone handling
Encrypted credential storage

Scheduled and recurring jobs depend on the Python process remaining active.

If AUTO-GEAR is terminated, its active background threads will also terminate.

Future Development

Potential future improvements include:

GUI interface
Persistent scheduled jobs
Job IDs and job management
Cancel/pause/resume functionality
Better logging
Configuration files
Secure credential storage
Timezone support
More advanced scheduling rules
Multiple simultaneous SMTP accounts
HTML email support
Richer system-alert integrations
AI-Assisted Development

Some portions of AUTO-GEAR were developed or refined with AI assistance.

The overall project structure, concept, implementation direction, and core framework were developed by the author. AI assistance was used for portions of the code and experimentation.

The repository is intended to document the project as it develops rather than represent every line as entirely manually written.

License

This project is licensed under the MIT License.

See LICENSE for details.

Disclaimer

AUTO-GEAR is intended for legitimate email automation, notification, and system-alert use.

Users are responsible for complying with the terms of service of their SMTP provider and all applicable laws and regulations.

Author

Developed as a local email automation project originally built for network monitoring and alerting.
