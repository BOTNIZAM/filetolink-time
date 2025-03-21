from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(env.get("API_ID", "25336929"))
    API_HASH = str(env.get("API_HASH", "308f4c34a6c3b90a74546d7e7e3087c2"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "8152045363:AAEbdljzOSjjyrSv-bHnwTGmCeSpHhsdF3Q"))
    OWNER_ID = int(env.get('OWNER_ID', '7978482443'))
    WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', "mongodb+srv://Filterbot:wywgsgwwwuww2iqiw@cluster0.s7cys.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Telegram"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "0"))
    FILE_PIC = env.get('FILE_PIC', "https://envs.sh/nlW.jpg/IMG21032025.jpg")
    START_PIC = env.get('START_PIC', "https://envs.sh/nlW.jpg/IMG21032025.jpg")
    VERIFY_PIC = env.get('VERIFY_PIC', "https://envs.sh/nlW.jpg/IMG21032025.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1002366692007"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1002491191746"))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "filetolink-time-22717399c4f5.herokuapp.com"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "120"))
    HAS_SSL = str(env.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "1").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



