# (c) @KGN_OFFICIAL

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 7588344))
    API_HASH = os.environ.get("API_HASH", "6ade175bcf8ea4981e3153ef48fe07f5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL"),( None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/BlackSovereignMDBot'>Black Sovereign</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 USED IN: <a href='https://t.me/BlackHArbour'>Group</a></b>
"""

    ABOUT_HELP_TEXT = """<b> You Can Try Searching Any Movies Series Shows In Our Group.

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! Dear {}😉,

I'm Mdisk Search Robo🤠</a>

I Can Search Anything!🔍 Just Drop A Movie Name With Correct Spelling 💁

<a>If You Didn't Found Ur Query Then Please Request It On @BlackHarbour ❤ </a></b>
"""


    START_MSG = """
<b>Hey! Dear {}😉,

I'm Black Sovereign a M-Disk Search Robo🤠</a>

I Can Search Anything!🔍 Just Drop A Movie Name With Correct Spelling 💁

<a>If You Didn't Found Ur Query Then Please Request It On @BlackHarbour ❤ </a></b>

"""
