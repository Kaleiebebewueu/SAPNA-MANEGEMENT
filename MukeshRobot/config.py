
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "28795512" # integer value, dont use ""
    API_HASH = "c17e4eb6d994c9892b8a8b6bfea4042a"
    TOKEN = "6827959192:AAF2IvJce014rPQ8Y6JNSo5tRD82EnX3UUQ"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 7115307617 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "ALL_SANATANI_BOT"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph//file/00c5804219a122d0c959b.jpg"
    EVENT_LOGS = (-1001970127211)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://SachinSanatani:SACHINxSANATANI@sanatani.bnmsfbd.mongodb.net/?retryWrites=true&w=majority&appName=Sanatani"
    # RECOMMENDED
    BOT_USERNAME = getenv("BOT_USERNAME" , "SANATANI_TECH_BOT")
    DATABASE_URL = getenv("DATABASE_URL", " postgres://iarfggbc:Vxzh_kG7cxa1kHR5faxcd1kuA4R-UT9E@rosie.db.elephantsql.com/iarfggbc")
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "HD7RYGCTES1V"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
