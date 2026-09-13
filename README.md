AUTO-GEAR
Local Email Automation for Python

AUTO-GEAR is a lightweight Python email automation tool that lets you send, schedule, delay, and repeat emails locally through an SMTP server.

It started as a simple network-alert bot. The project grew from there into a general-purpose local email automation service.

Some of the code was developed with AI assistance. The project concept, structure, frame, and overall implementation are mine.

Overview

AUTO-GEAR runs entirely from your local machine.

Configure an SMTP account, create an email, choose when it should be sent, and let AUTO-GEAR handle the rest.

┌──────────────────────────────────────────┐
│                 AUTO-GEAR                │
├──────────────────────────────────────────┤
│                                          │
│  SMTP Configuration                      │
│          │                               │
│          ▼                               │
│  Create Email                            │
│          │                               │
│          ▼                               │
│  Configure Schedule                      │
│          │                               │
│          ▼                               │
│  Background Worker                       │
│          │                               │
│          ▼                               │
│      SMTP Server                         │
│          │                               │
│          ▼                               │
│       Email Sent                         │
│                                          │
└──────────────────────────────────────────┘

Features
Feature	Supported
SMTP email delivery	Yes
Google SMTP	Yes
Outlook SMTP	Yes
Custom SMTP	Yes
Delayed delivery	Yes
Recurring delivery	Yes
Attachments	Yes
BCC	Yes
Custom bot names	Yes
App-password files	Yes
Background execution	Yes
Network alerts	Yes
GUI	Not currently
Scheduling

AUTO-GEAR supports three recurring intervals:

Minutes
Hours
Days


You can also specify an exact date and time for the first delivery:

YYYY-MM-DD HH:MM

Example:
2026-10-25 14:30

Example

Starting AUTO-GEAR presents the main configuration:

##---Auto-Gears---##

What is your SMTP service?

1. Google
2. Outlook
3. Type custom SMTP

Input your choice (1, 2, or 3):


After authentication:

What would you like to do:

1. Send / Schedule an email
2. Send a system log/alert
3. Exit Program


A job can then be configured with:

Bot Name
Recipient
Subject
Content
Attachment
BCC
Recurring Schedule
Delayed Start Time


Once configured, the email is handed to a background worker.

Main Program
     │
     ├── Create Job
     │
     └── Background Thread
              │
              ├── Wait
              ├── Connect
              ├── Authenticate
              ├── Send
              └── Repeat / Exit


The main program remains available while the scheduled job waits.

SMTP Support
Google
Server: smtp.gmail.com
Port:   587
TLS:    Enabled

Outlook
Server: smtp-mail.outlook.com
Port:   587
TLS:    Enabled

Custom

AUTO-GEAR also allows you to provide your own SMTP server.

Authentication

AUTO-GEAR supports application-specific passwords.

You can either load an app password from a local file:

/path/to/app_password.txt


or enter it manually when prompted.

Important

Do not commit credentials to GitHub.

For example, add sensitive files to .gitignore:

.env
secrets/
__pycache__/
*.pyc


If you store credentials in a text file, make sure that file is excluded from version control.

Installation
Requirements
Python 3.x
SMTP-enabled email account
App password or compatible SMTP credentials

AUTO-GEAR currently uses Python's standard library, so there are no required third-party packages.

Clone
git clone https://github.com/USERNAME/AUTO-GEAR.git
cd AUTO-GEAR

Run
python auto_gear.py


Or:

python3 auto_gear.py

Project Structure
AUTO-GEAR/
│
├── auto_gear.py
├── README.md
├── LICENSE
├── .gitignore
│
└── secrets/          # Local only


The current implementation intentionally keeps the project small.

How It Works

AUTO-GEAR uses Python's threading module to run scheduled jobs independently from the main program.

The worker:

Waits for the scheduled start time.
Creates an SMTP connection.
Starts TLS.
Authenticates.
Sends the message.
Closes the connection.
Calculates the next execution time.
Repeats if the job is recurring.

For one-time messages, the worker exits after delivery and removes the temporary content file.

Current Limitations

AUTO-GEAR is still an early-stage project.

Currently:

Jobs exist only while the program is running.
Closing AUTO-GEAR stops active background jobs.
Recurring schedules are not persisted.
There is no GUI.
There is no database.
Timezone handling is basic.
Job cancellation is not currently implemented.
Credentials are not stored in an encrypted credential manager.
Roadmap
Scheduling
 Persistent scheduled jobs
 Job IDs
 Cancel jobs
 Pause/resume jobs
 More scheduling options
 Timezone support
Email
 HTML email support
 Email templates
 Multiple attachments
 Improved recipient management
 Additional SMTP providers
Application
 Configuration file
 Better logging
 Persistent job database
 Improved CLI
 GUI
AI-Assisted Development

Parts of AUTO-GEAR were written or refined with AI assistance.

The AI-assisted portions are part of the development process, but the project concept, architecture, structure, and core direction were developed by the author.

License

This project is licensed under the MIT License.

See LICENSE for details.

Final

AUTO-GEAR is built around a simple idea:

Create an email.
Choose when it runs.
Let the local machine handle it.


It started as a network-alert script and is being developed into a broader local email automation tool.
