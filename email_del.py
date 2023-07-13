import getpass
import imaplib
from datetime import datetime, timedelta

# Prompt the user to enter their email address and password
email_address = input("Enter your email address: ")
password = input("Enter your password: ")

# IMAP server details
IMAP_SERVER = 'imap.gmail.com'

# Connect to the IMAP server
imap_server = imaplib.IMAP4_SSL(IMAP_SERVER)

# Login to the user's email account
imap_server.login(email_address, password)

# Select the INBOX folder
imap_server.select('INBOX')

# Calculate the date threshold (30 days ago)
threshold_date = datetime.now() - timedelta(days=30)
threshold_date_str = threshold_date.strftime('%d-%b-%Y')

# Search for messages older than the threshold date and unread
status, response = imap_server.search(None, 'UNSEEN', 'BEFORE', threshold_date_str)

# Get the list of message IDs
message_ids = response[0].split()

# Iterate over the message IDs and delete them
for message_id in message_ids:
    # Delete the message
    imap_server.store(message_id, '+FLAGS', '\\Deleted')

# Permanently remove the deleted messages
imap_server.expunge()

# Logout and close the connection
imap_server.close()
imap_server.logout()
