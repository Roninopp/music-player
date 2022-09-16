from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("7217645")) 
API_HASH = getenv("78ba6352dd5cdc166fdef5aa84ba7c67")
BOT_TOKEN = getenv("2100096282:AAHFgMRR_kkW_Mj05OyunSrjMrnhIk3VnEc")
SESSION_NAME = getenv("SESSION_NAME", "BQDBd2sYonPAV2YF2P8z9sMW-ekFcP37K_BemckMz-V_SRsVMZgC0wMw7sWbJsF9iAVaTO2_E8Tn7jqbgbcWZSgCNjO-vWzfJJFP5xA2sKSN5OysVrw3u3LFzArVpCEl9B6ihpXcbmXDwSvan46PfSShTIE5aoj4d_dbAjNjxi9hnDNLXWoCOfGL-ldBj5nL47XchebwE4LU91MlsgMJ1I2yftvoC5GVFzpWrmVQch_4lU1peCsbP81L5RHYCJMPhvyqdmr9ADOh0U6UYBLY2V4S8_qcik8RI13JlS5-NA3F_kQur_Urjb2lATGJ9DVmEeaLUDgLIJfGgPohHhDBOUWkAAAAAS3VP2UA")

# mandatory vars
OWNER_USERNAME = getenv("Dushmanxronin")
ALIVE_NAME = getenv("Fantastic")
BOT_USERNAME = getenv("fantasticfighterbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Roninopp/music-player")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "imperial_arena")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "imperial_arena")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("mongodb+srv://DARKAMAN:DARKAMAN@cluster0.snqhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("1793699293").split()))
SUDO_USERS = list(map(int, getenv("1793699293").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
