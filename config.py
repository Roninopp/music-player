from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7217645")) 
API_HASH = getenv("API_HASH", "78ba6352dd5cdc166fdef5aa84ba7c67")
BOT_TOKEN = getenv("BOT_TOKEN", "2100096282:AAHFgMRR_kkW_Mj05OyunSrjMrnhIk3VnEc")
SESSION_NAME = getenv("SESSION_NAME", "BQC7YeVY_dfntSCNJaDQl0IZiep5IbEIaiQZ3SOxFDQw3tv-doVV8d89qzQn7oo1kM0n7C_CEC_H1UAko02i3w5vHqQtxDgctu70rczR7-WYoyjy7RiGayatWHpyDcTUmVDV94K1-CL3jnuNGKcNjtGcPibOgqf4C166SJ_UsDCNz69T9WfmTpNZc1GUiQS1TFzIAe3PkDZL-S48FJOWvDR8KfvtPqzE8X9FVXXmVNynEVRiu9NmiX9gy5tQ8_-IYhifCw_1fQdYhlwjeoogAejwmYf0P5fI6QwFeSIbyvnLoTXfVOqBrOxnKQFzAE7MgGjOHLbMd5sKJchjEnAMO2J7AAAAAS3VP2UA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Dushmanxronin")
ALIVE_NAME = getenv("ALIVE_NAME", "Fantastic")
BOT_USERNAME = getenv("BOT_USERNAME", "fantasticfighterbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Roninopp/music-player")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "imperial_arena")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "imperial_arena")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://DARKAMAN:DARKAMAN@cluster0.snqhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1793699293").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
