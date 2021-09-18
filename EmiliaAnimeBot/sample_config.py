# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/EmiliaAnimeBot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 123456  # integer value, dont use ""
    API_HASH = "awoo"
    # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    TOKEN = "BOT_TOKEN"
    # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_ID = 792109647
    OWNER_USERNAME = "Izumi"
    SUPPORT_CHAT = 'TangentChat'  # Your own group for support, do not add the @
    # Prints any new group the bot is added to, prints just the name and ID.
    JOIN_LOGGER = -1234567789
    # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    EVENT_LOGS = -123456789

    # RECOMMENDED
    # needed for any database modules
    SQLALCHEMY_DATABASE_URI = 'something://somewhat:user@hosturl:port/databasename'
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', ]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "HW6WJSFETVW"  # Example; go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    # List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    # List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    BAN_STICKER = ''
    # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    ALLOW_EXCL = True
    # Get your API key from https://www.alphavantage.co/support/#api-key
    CASH_API_KEY = 'awoo'
    TIME_API_KEY = 'awoo'  # Get your API key from https://timezonedb.com/api
    WALL_API = 'awoo'  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    AI_API_KEY = 'awoo'
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
