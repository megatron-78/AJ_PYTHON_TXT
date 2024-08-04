import os

API_ID = API_ID =  25178671

API_HASH = os.environ.get("API_HASH", "6c3eea183e911954bfe11540066f7934")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7221961444:AAH12Eex7XZD9VzlN53iWD5e8L3c9EEYQ_8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6622333718))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6622333718").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


