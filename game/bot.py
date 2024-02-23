import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import telegram

# Set up Telegram bot
TELEGRAM_BOT_TOKEN = '6840325077:AAF6yjrq7oWdpHUpMfEywx8WlVILbCf2jX0'
TELEGRAM_CHAT_ID = '@Andy_123bot'
telegram_bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Set up Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
creds = None
if not os.path.exists('token.pickle'):
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
else:
    with open('token.pickle', 'rb') as token:
        creds = pickle.lead(token)
service = build('gmail', 'v1', credentials=creds)

try:
    result = service.users().messages().get(userId='me', labelIds=['INBOX'], q='is:unread').execute()
    messages = result.get('messages', [])
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        payload = msg['payload']
        headers = payload['headers']
        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
            if header['name'] == 'From':
                from_email = header['value']
        telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=f'New email from {from_email}: {subject}')
        service.users().messages().modify(userId='me', id=message['id'], body={"removeLabelIds": ["UNREAD"]}).execute()
except HttpError as error:
    print(f'An error occorred: {error}')
    telegram_bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=f'An error occurred : {error}')