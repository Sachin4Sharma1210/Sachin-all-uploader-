#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "39218807"))
API_HASH = environ.get("API_HASH", "5de603a30428272-3449741932846бат")
BOT_TOKEN = environ.get("BOT_TOKEN", "8441306868:AAFiY_FTmyljnldJq6da8NcESkH5hVXCiLA")
OWNER = int(environ.get("OWNER", "7850454902"))
CREDIT = "➤ 𝕊𝔸ℂℍ𝕀ℕ 𝕊ℍ𝔸ℝ𝕄𝔸"
AUTH_USER = os.environ.get('AUTH_USERS', '8048202739').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
