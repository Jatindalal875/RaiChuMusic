## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA-cOfpFvDJpq5wUtxrKkIgU8yViN7YxCaW7y0gP6S5V90R7YPlE-AMfIuGhe8Uj4A2c8Dr0puBOd7h-aXQrSzjXdJQdr0uorVFkoLdFJ87uctVlWjjlQQVIGX0Bf5FytWIOOR1txQMl6U64xuMrr73O5IMHScv9fW6p6jkT5Oo5KJ-fSfFSNa5PqggZnJ7Sw0Li6OOkkfjQRXBF9pX4Ha-al0vX4MinZ-U5NroNeQqkAYgtRoGV0USjd43DUhzo1WiuRzeI40WvcjEnB4atGBXa7lg9DoE0woKslgAlgJnw-BS8pTQCGanH57vJ0A4RJIuGI-IOgc7jIAy75bsXZVOAAAAAS_xwkcA")
BOT_TOKEN = getenv("BOT_TOKEN", "5757428871:AAEwjnNC7o_XPTOfy1IkKIVQCPDHrXaZvOw")
BOT_NAME = getenv("BOT_NAME", "KITTY ✘ ᗰＵＳＩＣ")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", " KITTY")
ALIVE_NAME = getenv("ALIVE_NAME", "KITTY ON FIRE❤️‍🔥")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "ll_KITTY_MUSIC_ll_ASSISTANT")
BOT_USERNAME = getenv("BOT_USERNAME", "KITTY_X_MUSIC_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "🦋【𝕂𝕚𝕥𝕥𝕪】muຮic͢͢bøτ🦋")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "EAGLE_MAFIA_CLUB")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "INDIA_UNITED")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1761766352").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . *").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
