import glob
import logging
import os
from pathlib import Path
from sys import argv
from ..core.session import catub
from userbot import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID
import sys
from asyncio.exceptions import CancelledError
from datetime import timedelta
from pathlib import Path

import requests
from telethon import Button, functions, types, utils

from userbot import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import catub
from ..helpers.utils import install_pip
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
import telethon.utils
from telethon import TelegramClient

from userbot import CMD_HNDLR, bot
from userbot.Config import Var
from userbot.thunderconfig import Config
from userbot.utils import load_assistant, load_module, start_assistant
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

TELE = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT
sed = logging.getLogger("Dark Fussion")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            Config.CATUBLOGO = await catub.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/4e3ba8e8f7e535d5a2abe.jpg",
                caption="**Your CatUserbot has been started successfully.**",
                buttons=[(Button.url("Support", "https://t.me/catuserbot"),)],
            )

async def startup_log_all_done():
    try:
        await bot.send_message(
            TELE,
            f"**Đ₳Ɽ₭ Ƒմʂʂìօղ has been deployed.\nSend** `{CMD_HNDLR}alive` **to see if the bot is working.\n\nAdd** @{BOTNAME} **to this group and make it admin for enabling all the features of userbot**",
        )
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished, no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            
         load_module(shortname.replace(".py", ""))
        except Exception:
            pass
print("Đ₳Ɽ₭ Ƒմʂʂìօղ has been deployed! ")

print("Setting up Đ₳Ɽ₭ Ƒմʂʂìօղ")


if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                
            
             load_assistant(shortname.replace(".py", ""))
            except Exception:
                pass
    sed.info("Đ₳Ɽ₭ Ƒմʂʂìօղ Has Been Deployed Successfully !")
    sed.info("╔════❰ Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ ❱═❍⊱❁۪۪")
    sed.info("║┣⪼ Ⲟⲱⲛⲉʀ - Ƒմʂʂìօղ ᴜꜱᴇʀ ")
    sed.info("║┣⪼ Ⲋⲧⲁⲧυⲋ - Ⲟⲛⳑⲓⲛⲉ")
    sed.info("║┣⪼ Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ - 1.2.0")   
    sed.info("║┣⪼ Ⳙⲣⲧⲓⲙⲉ - 00h:00m:4s ")
    sed.info("║┣⪼ Ⲃⲟⲧ Ⲣⲓⲛⳋ - 0.006")
    sed.info("║┣⪼ Ⲣⲩⲧⲏⲟⲛ - 3.9.2")
    sed.info("║┣⪼ Ⲧⲉⳑⲉⲧⲏⲟⲛ - 1.17.0 ")
    sed.info("║┣⪼ ✨Đ₳Ɽ₭ Ƒմʂʂìօղ✨")
    sed.info("║╰━━━━━━━━━━━━━━━➣ ")
    sed.info("╚══════════════════❍⊱❁۪۪")
else:
    sed.info("Đ₳Ɽ₭ Ƒմʂʂìօղ Has Been Installed Sucessfully !")
    sed.info("You Can Visit @Dark_Fussion_chat For Any Support Or Doubts")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()   
