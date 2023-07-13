

# Email del

**email del** is a Python script that helps you delete those annoying emails that crowd your inbox. This script is specifically designed for Gmail and may not work with other email providers.

## Prerequisites

To use **email del**, you need to have the following prerequisites:

- Docker installed on your machine. You can download and install Docker from the official Docker website: **(https://www.docker.com/get-started)**

## Installation

Follow these steps to install and set up **email del**:

1. Clone the repository to your local machine:

 **git clone https://github.com/your-username/email-del.git**
   
2. Navigate to the project directory:

   **cd email-del**

3. Build the Docker image:

   **docker build -t email-del .**



# Usage

To use email del and delete unread emails, follow these steps:

Generate an app password from Google to use with email del. App passwords provide an extra layer of security for accessing your Gmail account. Follow the steps below to generate an app password:

Go to your Google Account settings: **https://myaccount.google.com/**
Navigate to the "Security" tab.
Under "Signing in to Google," click on "App Passwords" (you may need to enable two-factor authentication if not already enabled).
Select "Mail" and "Other (Custom name)" in the dropdown menus.
Enter a custom name for the app password, such as "email-del."
Click on the "Generate" button.
Google will generate an app password for you. Make note of this password as it will be used in the next step.

Run the Docker container:

 **docker run -it -e EMAIL_ADDRESS="your-email@gmail.com" -e PASSWORD="your-app-password" email-del**

Replace your-email@gmail.com with your Gmail address and your-app-password with the app password you generated in the previous step.

Follow the prompts in the terminal to confirm the email address and password.

email del will log in to your Gmail account and delete unread messages older than 30 days.

Fork the repository.

Create your feature branch: **git checkout -b feature-name.**

Commit your changes: **git commit -m 'Add some feature'.**

Push to the branch: **git push origin feature-name.**

Open a pull request.


**License**

This project is licensed under the **MIT License**.

