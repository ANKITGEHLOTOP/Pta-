#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29905645"))
API_HASH = environ.get("API_HASH", "e5a701f6e0b5fb659cb57a230b9a3feb")
BOT_TOKEN = environ.get("BOT_TOKEN", "8134512573:AAGHqVcKIcr6Cw9u5uoYdjxKNu-KPeuClaY")
OWNER = int(environ.get("OWNER", "8102112566"))
CREDIT = environ.get("CREDIT", "PAPA HI KEHDE")
AUTH_USER = os.environ.get('AUTH_USERS', '8102112566').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
