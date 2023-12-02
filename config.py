# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6467108615:AAGYr0xFmVej6je3TAylviAHKHoECfXD5vM")

    APP_ID = int(os.environ.get("APP_ID", 27240111))

    API_HASH = os.environ.get("API_HASH", "97ddeb5f8a91117c3e076b6fb3340b58")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("RemoveBG_API", "ESSsRj3CpbrRCGsqYFxUEyP1")
