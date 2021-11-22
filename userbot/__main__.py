from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, JARVISversion
from pathlib import Path
import asyncio
import glob
import telethon.utils

JARVIS_PIC ="https://te.legra.ph/file/7aa60202b95b798a2a4bb.jpg"

async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"JARVIS_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN_BF_HER",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()
print("Loading Modules / Plugins")

async def main_pl():
  import glob
  path = 'userbot/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))
"""
async def assistant():
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))
        extra_repo = "https://github.com/JARVIS-USERBOT/JARVIS-BOT"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("Loading Addons")
        path = "JARVIS-DATA-BASE/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[JARVIS-1.0] - Addons -  Installed - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[JARVIS-1.0] - Addons - ERROR - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
"""
bot.loop.run_until_complete(main_pl())
print(f"""
 ________________
|                    |
|JARVIS-BOT TURNED ON|
|____________________|""")



async def jarvis_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                JARVIS_PIC,
                caption=f"DEPLOYED JARVIS BOT",
            )
    except Exception as e:
        print(str(e))

    try:
        await bot(JoinChannelRequest("@Jarvis_Support_Official"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Jarvis_Support_Official"))
    except BaseException:
         pass


bot.loop.create_task(jarvis_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
