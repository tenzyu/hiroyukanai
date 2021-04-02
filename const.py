from os import getenv

from dotenv import load_dotenv

load_dotenv()

# get token from .env
DISCORD_BOT_TOKEN = getenv("DISCORD_BOT_TOKEN")

# setting
BOT_NAME = "Hiroyukanai"
BOT_PREFIX = "!"


VOICE_CHANNELS = {
    "714753888389169165": {
        "vc_text": 714757734192381972,
        "name": "vc1",
    },
    "821920031280857138": {
        "vc_text": 827484116026261514,
        "name": "vc2",
    },
}
CH_AFK = 718873424176349295
