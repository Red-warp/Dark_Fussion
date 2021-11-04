# Created by Red warp and Akshat7678..!!

import os
from telethon import events, Button, custom
from userbot.thunderconfig import Config

from userbot import ALIVE_NAME, bot 

currentversion = "1.0"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Đ₳Ɽ₭ Ƒմʂʂìօղ"
ASSIS_PIC = os.environ.get("ASSIS_PIC", None)
if ASSIS_PIC is None:
     PM_IMG = "https://telegra.ph/file/62fa5d70a65f9ce0d0170.jpg"
else:
     PM_IMG = ASSIS_PIC


pm_caption = "**Đ₳Ɽ₭ Ƒմʂʂìօղ IS ONLINE**\n\n"
pm_caption += "┏┓━┏┓━━━━┏┓━┏┓━━━━━\n"
pm_caption += "┃┃━┃┃━━━━┃┃━┃┃━━━━━\n"
pm_caption += "┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n"
pm_caption += "┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃\n"
pm_caption += "┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃\n"
pm_caption += "┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛\n"
pm_caption += "╭━━━━━━━━━━━━━━━➣\n"
pm_caption += "┣► **SYSTEMS STATS**\n"
pm_caption += "┣► **Telethon Version:** `1.15.0` \n"
pm_caption += f"┣► **Assistant Version** : `{currentversion}`\n"
pm_caption += f"┣► **My Master** : {DEFAULTUSER} \n"
pm_caption += "┣► **License** : [GNU License](https://github.com/TeamFussion/Dark_Fussion/blob/master/LICENSE)\n"
pm_caption += "┣► **Copyright** : [Đ₳Ɽ₭ Ƒմʂʂìօղ](GitHub.com/TeamFussion/Dark_Fussion)\n"
pm_caption += "╰━━━━━━━━━━━━━━━➣\n\n"
light = [[Button.url("✧Repo✧", "https://github.com/TeamFussion/Dark_Fussion"), Button.url("✧Deploy✧", "https://heroku.com/deploy?template=https://github.com/TeamFussion/Dark_Fussion")]]
light +=[[Button.url("✧Channel✧", "https://t.me/DarkFussion") , Button.url("✧Group✧", "https://t.me/Dark_Fussion_chat")]]
light +=[[Button.url("✧Devoloper✧" , "https://github.com/TeamFussion")]]
@tgbot.on(events.NewMessage(pattern="^/alive" , func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption, buttons=light)
