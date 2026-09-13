Got it — **no roadmap section**. Keep it simple and focused on what AUTO-GEAR currently does.

# AUTO-GEAR

Local email automation and scheduling tool written in Python.

AUTO-GEAR uses SMTP to send emails immediately, at a scheduled time, or on a recurring interval.

It started as a network alert script and was later expanded into a general email automation tool.

Some parts of the code were written with AI assistance.

## Features

* Send emails through SMTP
* Schedule emails
* Recurring emails
* Background threads for scheduled jobs
* File attachments
* BCC recipients
* Custom bot name
* Load App Password from a file
* Google SMTP
* Outlook SMTP
* Custom SMTP servers
* Network alerts

## How It Works

Scheduled emails run in background threads while the main program continues running.

```text
Create Email
     |
     v
Set Schedule
     |
     v
Background Thread
     |
     +-- Wait for scheduled time
     +-- Connect to SMTP
     +-- Send email
     +-- Repeat if recurring
```

## Scheduling

### Delayed Emails

Format:

```text
YYYY-MM-DD HH:MM
```

Example:

```text
2026-10-25 14:30
```

### Recurring Emails

Emails can repeat every:

* Minutes
* Hours
* Days

Examples:

```text
Every 10 minutes
Every 2 hours
Every 3 days
```

## SMTP Support

| Provider | SMTP Server             |         Port |
| -------- | ----------------------- | -----------: |
| Google   | `smtp.gmail.com`        |          587 |
| Outlook  | `smtp-mail.outlook.com` |          587 |
| Custom   | User-defined            | User-defined |

TLS is used for SMTP connections.

## Authentication

AUTO-GEAR supports App Passwords.

The password can be entered when the program starts or loaded from a local file.

Example:

```text
/path/to/app_password.txt
```

Do not store passwords in the repository.

Recommended `.gitignore`:

```gitignore
.env
secrets/
__pycache__/
*.pyc
```

## Installation

### Requirements

* Python 3.x
* SMTP-enabled email account
* App Password or compatible SMTP credentials

No external packages are required.

### Clone

```bash
git clone https://github.com/YOUR-USERNAME/AUTO-GEAR.git
cd AUTO-GEAR
```

### Run

```bash
python auto_gear.py
```

Or:

```bash
python3 auto_gear.py
```

## Usage

Run the program and select an option from the main menu:

```text
1. Send / Schedule an email
2. Send a system log / alert
3. Exit Program
```

When sending an email, you can set:

* Bot Name
* Recipient
* Subject
* Message
* Attachment
* BCC
* Schedule
* Recurring interval

## Network Alerts

AUTO-GEAR was originally made for network alerts.

It can send an email when a system or network event occurs.

## Project Structure

```text
AUTO-GEAR/
├── auto_gear.py
├── README.md
├── LICENSE
└── .gitignore
```

## Limitations

* Scheduled jobs are stored in memory
* Jobs are lost when the program exits
* Recurring jobs are not persistent
* Command-line only
* No job cancellation
* No pause/resume
* Basic timezone handling
* Limited logging

## License

MIT License. See [LICENSE](LICENSE) for details.

## Disclaimer

AUTO-GEAR is intended for legitimate email automation, monitoring, notifications, and alerts.

Users are responsible for following their SMTP provider's policies and applicable laws.
