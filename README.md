# Overview

We have created this project to help users send emails without even opening their gmail. Wondering how to do so ? We have used python for this purpose

## What this project does

* Uses python's smtplib module to create a connection with the server
* Logs in to our google account
* Sends an email message with as well as without attachments using gmail


# Setup required

* smtplib module is a built in module in python for sending emails using the simple mail transfer protocol(SMTP). **No installation required for  this module**

## Clone the repository

```bash
git clone https://github.com/arnabmitra471/python_email_sender.git
```
## Configuring the environment variables
You will need to create a `.env` file in your current working directory and put in the username and password there.

**Important note** - If you have 2 step verification turned on, you will need to enter an app password instead of your actual password. Create one if you don't have setup one already.

# Features
* Handles file attachments with MIME modules
* Supports different MIME types
* Can also send text email messages
* Rich formatting of emails with html tags supported
* Secure authentication with TLS encryption
* Handles missing files and authentication errors gracefully
* Doesn't hard code the username and password for an account while logging in to send emails


```properties
USER_NAME = "your_user_name"
PASSWORD = "your app_password"
```

**Please be sure to use an app password instead of your normal password**

Run the script
```shell
python emails_with_python.py
```




