import os

import re
import json
from math import ceil
from userbot.thunderconfig import Config

from telethon import Button, custom, events, functions

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST, DETAIL_CMD_HELP, bot

from var import Var


LIGHT_LOGS = Config.PM_LOGGR_BOT_API_ID 
lightning_bot = Var.TG_BOT_USER_NAME_BF_HER
import asyncio

from datetime import datetime
from pathlib import Path


from userbot.utils import lightning_cmd, load_module, remove_plugin

DELETE_TIMEOUT = 5


thumb_image_path = "./resources/541200.png"

LIGHTNINGUSER = str(ALIVE_NAME) if ALIVE_NAME else "Ƒմʂʂìօղ мαѕтєя"
LIGHTNINGBOT = Var.TG_BOT_TOKEN_BF_HER






@borg.on(lightning_cmd(pattern=r"unload (?P<krish_blac>\w+)$"))
async def unload(lightning):
    if lightning.fwd_from:
        return
    krish_blac = lightning.pattern_match["krish_blac"]
    try:
        remove_plugin(krish_blac)
        await lightning.edit(f"Successfully unloaded {krish_blac}")
    except Exception as e:
        await lightning.edit(
            "Successfully unloaded {krish_blac}\n{}".format(krish_blac, str(e))
        )


@borg.on(lightning_cmd(pattern=r"load (?P<krish_blac>\w+)$"))
async def load(lightning):
    if lightning.fwd_from:
        return
    krish_blac = lightning.pattern_match["krish_blac"]
    try:
        try:
            remove_plugin(krish_blac)
        except BaseException:
            pass
        load_module(krish_blac)
        await lightning.edit(f"Successfully loaded {krish_blac}")
    except Exception as e:
        await lightning.edit(
            f"Sorry,{krish_blac} can not be loaded\nbecause of the following error.\n{str(e)}"
        )

 # created by @cyper666
"""xoxbot: Avaible commands: .xnxx picx les<link>
"""


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError




@borg.on(lightning_cmd(pattern="xnxx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "💋2016 Videolar🔞{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(lightning_cmd(pattern="picx?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "♨️Old photo👙{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@borg.on(lightning_cmd(pattern="les?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "🔞Uz_sex♨️{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


BOT_MSG = os.environ.get("BOT_MSG", None)
if BOT_MSG is None:
    BOT_LIT = f"**Hᴇʟʟᴏ\nI'ᴍ Aꜱꜱɪꜱᴛᴀɴᴛ..!!**\n\n"
else:
    BOT_LIT = BOT_MSG   


LIGHTNING_WARN = os.environ.get("LIGHTNING_WARN", None)
LIGHTNING_BOT_PIC = os.environ.get("LIGHTNING_BOT_PIC", None)

if LIGHTNING_WARN is None:
    WARNING = (
    f"{BOT_LIT}"
    f"**Dᴏɴ'ᴛ ᴛʀʏ ᴛᴏ sᴘᴀᴍ.**\n"
    f"**Oᴛʜᴇʀᴡɪsᴇ Yᴏᴜ'ʟʟ Bᴇ Bʟᴏᴄᴋᴇᴅ Aɴᴅ Rᴇᴘᴏʀᴛᴇᴅ. **\n"
    f"**I'ʟʟ Rᴇᴘʟʏ Yᴏᴜ Aғᴛᴇʀ, Cᴏᴍᴇ Bᴀᴄᴋ Oɴʟɪɴᴇ.!**\n\n"
    f"**Cʜᴏᴏꜱᴇ Yᴏᴜʀ Oʀɪɢɪɴᴀʟ Rᴇᴀꜱᴏɴ Wʜʏ Yᴏᴜ Cᴏᴇ Hᴇʀᴇ..!!**"
   )
else:
    WARNING = LIGHTNING_WARN

LIGHTNING_BOT_PIC = (
    LIGHTNING_BOT_PIC
    if LIGHTNING_BOT_PIC
    else "https://te.legra.ph/file/1b87bff0d89a0ba1f71f4.jpg"
)









@tgbot.on(events.InlineQuery)
async def inline_handler(lightning):
    builder = lightning.builder
    result = None
    query = lightning.text
    if lightning.query.user_id == bot.uid and query.startswith("**sed") or query.startswith("soosed"):
        rev_text = query[::-1]
        buttons = lightnings_menu_for_help(0, CMD_LIST, "helpme")
        result = builder.article(
            f"Help Menu",
            text="\n{}\n`Plugins`: {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await lightning.answer([result] if result else None)
    elif lightning.query.user_id == bot.uid and query.startswith("**Black") or query.startswith("Black"):
        result = builder.photo(
            file="https://te.legra.ph/file/de1eb7e29a6553d8e3670.jpg",
            text=f"** Bᴏᴛ Oғ {LIGHTNINGUSER}\n\n Mᴀɪɴ Mᴇɴᴜ\n Pʟᴜɢɪɴs ~ {len(CMD_LIST)}\n\n Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ\n╭━━━━━━━━━━━━━━━➣\n┣⪼ Ⲟⲱⲛⲉʀ - {LIGHTNINGUSER}\n┣⪼ Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ - 1.2.7\n┣⪼ Ⳙⲣⲧⲓⲙⲉ - 2m.42s\n┣⪼ Ⲣⲩⲧⲏⲟⲛ - 3.9.96\n┣⪼ Ⲧⲉⳑⲉⲧⲏⲟⲛ - 1.23.0\n╰━━━━━━━━━━━━━━━➣** ",
            buttons=[
                [custom.Button.inline("🔌 Pʟᴜɢɪɴs 🔌", data="what?"),
                custom.Button.inline("📍 Pɪɴɢ 📍", data="bitch")],
                [Button.url("🧑‍💻 Uᴘᴅᴀᴛᴇs 🧑‍💻", "https://t.me/DarkFussion"),
                Button.url("💓 Sᴜᴘᴘᴏʀᴛ 💓", "https://t.me/Dark_Fussion_chat")],
                [Button.url("⚙ Sᴇᴛᴛɪɴɢs ⚙" , "https://t.me/Red_warp")],
                [custom.Button.inline("🚫 Cʟᴏsᴇ 🚫", data="close?")],
  
           ],
        )
        await lightning.answer([result])

    elif lightning.query.user_id == bot.uid and query.startswith("**Hello Sir"):
        result = builder.photo(
            file=LIGHTNING_BOT_PIC,
            text=WARNING,
            buttons=[

                [custom.Button.inline("🚫 Sᴘᴀᴍ 🚫", data="fussion_bc_fucker"),
              
                custom.Button.inline("📝 Rᴇǫᴜᴇsᴛ 📝", data="fck_ask")],
   
                    [custom.Button.inline(
                        "💬 Cʜᴀᴛ 💬", 
                        data="fck_niigaaaaa_noob",
                        
                    )
                        
                ,

                    custom.Button.inline(
                        "⭐ Fʀɪᴇɴᴅ ⭐",
                        data="he_sucks",
                    )
                ],
[
                    custom.Button.inline(
                        "❌ Lᴇᴛ Mᴇ Iɴ ❌", 
                        data="lol_u_think_so",
                        
                    )
                        
                ],
            ],
            )
        await lightning.answer([result] if result else None)
    else:
        return
    


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    )
)
async def lightning_pugins_query_hndlr(lightning):
    if lightning.query.user_id == bot.uid:  # pylint:disable=E0602
        lightning_page = int(lightning.data_match.group(1).decode("UTF-8"))
        buttons = lightnings_menu_for_help(
            lightning_page + 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await lightning.edit(buttons=buttons)
    else:
        lightning_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
        await lightning.answer(lightning_is_best, cache_time=0, alert=True)


@tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"_lightning_plugins_(.*)")
   )
) # Thanks To Friday Userbot
async def lightning_pugins_query_hndlr(lightning):
    if not lightning.query.user_id == bot.uid:
        how = "Do you Really Think This is for you? \nThen Make your own Fussion Bot and don't poke your nose in mine.!"
        await lightning.answer(how, cache_time=0, alert=True)
        return
    light_pulu_name = lightning.data_match.group(1).decode("UTF-8")
   
    if light_pulu_name in CMD_HELP.keys():
       
       lightning_help_strin  = f"**✘ Commands Available ✘**\n" 
       lightning_help_strin  += f"**✘ Name ✘ :** `{light_pulu_name}` \n{CMD_HELP[light_pulu_name]}"
       lightning_is_best = lightning_help_strin 
    
    else:
       lightning_help_strin  = f"**✘ Commands Available ✘\n✘ Name ✘ : ** `{light_pulu_name}` \n`{CMD_LIST[light_pulu_name]}`"
       lightning_is_best = lightning_help_strin 
    if len(lightning_is_best) >= 4096:
          keinshin = "`Wait.( ͡🔥 ͜ʖ ͡🔥)`"
          await lightning.answer(keinshin, cache_time=0, alert=True)
          out_file = lightning_is_best
          lig_url = "https://del.dog/documents"
          r = requests.post(lig_url, data=out_file.encode("UTF-8")).json()
          lig_url = f"https://del.dog/{r['key']}"
          await lightning.edit(
               f"Pasted {light_pulu_name} to {lig_url}",
               link_preview=False,
               buttons=[ 
                [custom.Button.inline("✘ Status ✘", data="stta")],
                [custom.Button.inline("✘ Ⴆαƈƙ ✘", data="lghtback")]],
         )
    else:
           await lightning.edit(
            message=lightning_is_best,
            buttons=[
                [custom.Button.inline("✘ Check Status ✘", data="stta")],
                [custom.Button.inline("✘ Ⴆαƈƙ ✘", data="lghtback")],
            ],
        )


@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(rb"helpme_prev\((.+?)\)")
    )
)
async def lightning_pugins_query_hndlr(lightning):
    if lightning.query.user_id == bot.uid:  # pylint:disable=E0602
        lightning_page = int(lightning.data_match.group(1).decode("UTF-8"))
        buttons = lightnings_menu_for_help(
            lightning_page - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await lightning.edit(buttons=buttons)
    else:
        lightning_is_best = "Oh C'mon You Think You Can Touch This? ಠ╭╮ಠ!"
        await lightning.answer(lightning_is_best, cache_time=0, alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"what?")))
async def what(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = "**Đ₳Ɽ₭ Ƒմʂʂìօղ Heres With The Detailed Help For CMDs** 🙂! "
        buttons = lightnings_menu_for_help(0, CMD_LIST, "helpme")
        await lightning.edit(fck_bit, buttons=buttons)
    else:
        txt = f"Ohh C'mon You Think That This Is For You?\n Ok I Will Complain To {LIGHTNINGUSER}👀👀"
        await lightning.answer(txt, alert=True)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lol_u_think_so")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    text1 = f"LOL You Think So You Can😂😂\nGo and wait😂😂"
    await lightning.edit("Off Course Go To Hell Dude😛")
    await bot.send_message(lightning.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))
    await bot.send_message(
        LIGHT_LOGS,
        f"Hey Master Sorry Disturb You, [Noob](tg://user?id={lightning_id}) Tryin To Enter With Out approval😂 \n.",
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"bitch")))

async def lightning_is_better(lightning):
        start = datetime.now()

        end = datetime.now()

        ping = (end - start).microseconds / 1000
        wews = bot.me.first_name
        weds = bot.me.username
        if lightning.query.user_id == bot.uid:
          fck_bit = f"꧁ Pong! ꧂\n\n⚘ Ping Time:- {ping}\n\n⚘ My Fussion Master [{wews}](t.me/{weds})"
          await lightning.edit(fck_bit, link_preview=False, buttons=[Button.inline("✧Back✧", data="wtshit")])
        else: 
           await lightning.answer(f"I am {LIGHTNINGUSER}'s Assistant not your", alert=True)
    

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"he_sucks")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    await lightning.edit("Oh You Wanna Talk With My Master\n\nPls Wait Dear \n\n**Btw** **You Can Wait For My Master**")
    await asyncio.sleep(2)
    await lightning.edit(
        "Name Which Type Of Friend?", buttons= [
        [Button.inline("✘ Sᴄʜᴏᴏʟ ᴏʀ Cʟᴏsᴇ Fʀɪᴇɴᴅ ✘", data="school")], 
        [Button.inline("✘ Cᴀᴜsᴀʟ Fʀɪᴇɴᴅ ✘" , data="tg_okay")],],
    )
    light_text = "`Warning`- ❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"
    await bot.send_message(lightning.query.user_id, light_text)
    
    
    
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"school")))
async def yeahbaba(lightning):
        if lightning.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} "
            await lightning.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**So You  Are School Friend** Okay wait"
        lightning_id = lightning.query.user_id
        await asyncio.sleep(2)
        await lightning.edit(f"`Informing To Master {LIGHTNINGUSER}`")
        await asyncio.sleep(2)
        await lightning.edit("`Done Informed`")
        await bot.send_message(lightning.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"Hii {LIGHTNINGUSER}..!!\nYour School friend is waiting..!!\nPlease talk to him if necessary..!!\nYour friend - [Here](tg://user?id={lightning_id})",
    
    )    
    
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"tg_okay")))
async def yeahbaba(lightning):
        if lightning.query.user_id == bot.uid:
            fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} "
            await lightning.answer(fck_bit, cache_time=0, alert=True)
            return
        light_text = "**So You  Are Causal Friend** Okay wait"
        lightning_id = lightning.query.user_id
        await asyncio.sleep(2)
        await lightning.edit(f"`Informing To My Master {LIGHTNINGUSER}`")
        await asyncio.sleep(2)
        await lightning.edit("`Done Informed`")
        await bot.send_message(lightning.query.user_id, light_text)
        await bot.send_message(
        LIGHT_LOGS,
        message=f"Hii {LIGHTNINGUSER}..!!\nYour Causal friend is waiting..!!\nPlease talk to him if necessary..!!\nYour friend - [Here](tg://user?id={lightning_id})",
    
    )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_ask")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    await lightning.edit("Okay let Me Think")
    await asyncio.sleep(2)
    await lightning.edit("Okay Giving You A Chance")
    await asyncio.sleep(2)
    await lightning.edit(
        "You Will Spam?", buttons= [
        [Button.inline("✘ Yᴇs ✘", data="lemme_ban"),
         Button.inline("✘ Nᴏ ✘", data="hmm")],
        ],
    )

    
    reqws = "`Warning`- ❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"


    await bot.send_message(lightning.query.user_id, reqws)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"Hello, Master  [Nibba](tg://user?id={lightning_id}). Wants To Request Something.",
        buttons=[Button.url("Contact Him", f"tg://user?id={lightning_id}")],
    )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fck_niigaaaaa_noob")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch 😁✌️"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    await lightning.edit("Okay Giving You A Chance")
    await asyncio.sleep(2)
    await lightning.edit(
        "Will You Spam?", buttons= [
        [Button.inline("✘ Yᴇs ✘", data="lemme_ban"),
         Button.inline("✘ Nᴏ ✘", data="hmm")],
        ],
    )

    
    reqws = f"You can chat with {LIGHTNINGUSER} when he'll online\n`Warning`- ❗️⚠️Don't send any message now wait kindly!!!❗️⚠️"


    await bot.send_message(lightning.query.user_id, reqws)
    await bot.send_message(
        LIGHT_LOGS,
        message=f"#Chatter\n\nʜᴇʟʟᴏ {LIGHTNINGUSER},\nɴɪʙʙᴀ ᴡᴀɴᴛs ᴛᴏ ᴄʜᴀᴛ ᴡɪᴛʜ ʏᴏᴜ..!! 😁😂\n\nɪғ ʜᴇ ɪs ᴀ ɢᴏᴏᴅ ᴍᴀɴ ᴛʜᴇɴ ᴛᴀʟᴋ ᴡɪᴛʜ ʜɪᴍ..\nɪғ ʏᴏᴜ ᴛʜɪɴᴋ ʜᴇ ɪs sᴘᴀᴀᴍᴇʀ ᴛʜᴇɴ  ʙʟᴏᴄᴋ ᴛʜɪs ɴɪʙʙᴀ.!\n\nsᴏʀʀʏ ғᴏʀ ᴅɪsᴛᴜʀʙɪɴɢ ʏᴏᴜ..! 😁,\nʜᴀᴠᴇ ᴀ ɴɪᴄᴇ ᴅᴀʏ 🙂" , buttons=[[Button.url("✘ ᴄʜᴀᴛᴛᴇʀ ✘", "tg://user?id={lightning_id}")],],)
    
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hmm")))
async def yes_ucan(lightning):
    if lightning.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol."
           await lightning.answer(lmaoo, cache_time=0, alert=True)
           return 
    await lightning.get_chat()
    await asyncio.sleep(2)
    await lightning.edit("Okay You Can Wait Till Wait")
    hmmmmm = "Okay Kindly wait  i will inform you"
    await bot.send_message(
              lightning.query.user_id, hmmmmm)
          
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lemme_ban")))
async def yes_ucan(lightning):
    if lightning.query.user_id == bot.uid:
           lmaoo = "You Are Not Requesting , Lol.."
           await lightning.answer(lmaoo, cache_time=0, alert=True)
           return    
    await lightning.get_chat()
    await asyncio.sleep(2)
    await lightning.edit("Get Lost Reward")
    ban = "Get Lost Going To Block You" 
    await bot.send_message(
         lightning.query.user_id, ban)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stta")))
async def hmm(lightning):
    if lightning.query.user_id == bot.uid:
        text = "✘ My Stats ✘\n\nPʟᴜɢɪɴ-- All Good ✔\nHᴇʀᴏᴋᴜ - Connected ✔\nLᴏɢs -- Looks Good ✔"
        await lightning.answer(text, alert=True)
    else:
        txt = f"Stats For {LIGHTNINGUSER} Not For You Nigga\nDon't Poke your Nose Please"
        await lightning.answer(txt, alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"wtshit"))) 
async def lmaao(lightning):
    if lightning.query.user_id == bot.uid:
        await lightning.edit(
            f"** Bᴏᴛ Oғ {LIGHTNINGUSER}\n\n Mᴀɪɴ Mᴇɴᴜ\n Pʟᴜɢɪɴs ~ {len(CMD_LIST)}\n\n Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ\n╭━━━━━━━━━━━━━━━➣\n┣⪼ Ⲟⲱⲛⲉʀ - {LIGHTNINGUSER}\n┣⪼ Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ - 1.2.7\n┣⪼ Ⳙⲣⲧⲓⲙⲉ - 2m.42s\n┣⪼ Ⲣⲩⲧⲏⲟⲛ - 3.9.96\n┣⪼ Ⲧⲉⳑⲉⲧⲏⲟⲛ - 1.23.0\n╰━━━━━━━━━━━━━━━➣**",
            buttons=[
                [custom.Button.inline("🔌 Pʟᴜɢɪɴs 🔌", data="what?"),
                custom.Button.inline("📍 Pɪɴɢ 📍", data="bitch")],
                [Button.url("🧑‍💻 Uᴘᴅᴀᴛᴇs 🧑‍💻", "https://t.me/DarkFussion"),
                Button.url("💓 Sᴜᴘᴘᴏʀᴛ 💓", "https://t.me/Dark_Fussion_chat")],
                [Button.url("⚙ Sᴇᴛᴛɪɴɢs ⚙" , "https://t.me/Red_warp")],
                [custom.Button.inline("🚫 Cʟᴏsᴇ 🚫", data="close?")],
            ],
        )
    else:
        fukoff = "You Don't belong to my master's category. So, why should i follow your orders\nHence, Fuck off Noob" 
        await lightning.answer(fukoff, alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close?"))) 
async def lmaao(lightning):
    if lightning.query.user_id == bot.uid:
        await lightning.delete()

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fussion_bc_fucker")))
async def lightning_is_better(lightning):
    if lightning.query.user_id == bot.uid:
        fck_bit = f"Oh! C'mon Master {LIGHTNINGUSER} Im Try To Get Rid Of This Nigga Pls Dont Touch"
        await lightning.answer(fck_bit, cache_time=0, alert=True)
        return
    await lightning.get_chat()
    lightning_id = lightning.query.user_id
    text1 = f"LOL **You Think So You Can**😂😂\n\n**[Idiot](tg://user?id={lightning_id}) Bye I'm going to block you.**😂😂"
    await lightning.edit("Off Course Go To Hell Dude")
    await bot.send_message(lightning.query.user_id, text1)
    await bot(functions.contacts.BlockRequest(lightning.query.user_id))
    await lightning.edit("😛 Bye idiot")
    await bot.send_message(
        LIGHT_LOGS,
        f"#Spammer\n\nHᴇʟʟᴏ {LIGHTNINGUSER},\nNɪʙʙᴀ Tʀʏɪɴɢ Tᴏ Sᴘᴀᴍ..😁😏\n\n**Sᴏ Bʟᴏᴄᴋᴇᴅ** 😏\n\nSᴏʀʀʏ Fᴏʀ Dɪsᴛᴜʀʙɪɴɢ Yᴏᴜ..! 😁,\nHᴀᴠᴇ ᴀ Nɪᴄᴇ Dᴀʏ 🙂" , 
        buttons=[[Button.url("Spammer", "tg://user?id={lightning_id}")],],
    )


import requests




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lghtback")))
async def ho(event):
    if event.query.user_id != bot.uid:
        how = "Not For You Idiot ( ͡❛ ͜ʖ ͡❛)."
        await event.answer(how, cache_time=0, alert=True)
        return
    await event.answer("( ͡🔥 ͜ʖ ͡🔥)", cache_time=0, alert=False)
    # This Is Copy of Above Code. (C) link_preview=False
    buttons = lightnings_menu_for_help(0, CMD_LIST, "helpme")
    ho = f"""Đ₳Ɽ₭ Ƒմʂʂìօղ Is Here With Stunning Help ! In Case Any Problem [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat) \nTottal Plugs : {len(CMD_LIST)}"""
    await event.edit(message=ho, buttons=buttons)



        


    
def lightnings_menu_for_help(b_lac_krish, lightning_plugs, lightning_lol):
    lightning_no_rows = 5
    lightning_no_coulmns = 5
    lightning_plugins = []
    for p in lightning_plugs:
        if not p.startswith("_"):
            lightning_plugins.append(p)
    lightning_plugins = sorted(lightning_plugins)
    plugins = [
        custom.Button.inline(
            "{} {} {}".format("🌟", x, "🌟"), data="_lightning_plugins_{}".format(x)
        )
        for x in lightning_plugins
    ]
    pairs = list(zip(plugins[::lightning_no_coulmns], plugins[1::lightning_no_coulmns]))
    if len(plugins) % lightning_no_coulmns == 1:
        pairs.append((plugins[-1],))
    max_fix = ceil(len(pairs) / lightning_no_rows)
    lightning_plugins_pages = b_lac_krish % max_fix
    if len(pairs) > lightning_no_rows:
        pairs = pairs[
            lightning_plugins_pages * lightning_no_rows : lightning_no_rows * (lightning_plugins_pages + 1)
        ] + [
            (
                custom.Button.inline(
                    "✨ яιgнт ✨", data="{}_prev({})".format(lightning_lol, lightning_plugins_pages)
                ),
               # Thanks To Friday For This Idea
               custom.Button.inline("🚫 Back 🚫", data="wtshit"
               ),
               custom.Button.inline(
                    "✨ ℓєfт ✨", data="{}_next({})".format(lightning_lol, lightning_plugins_pages)
                ),
                
            )
        ]
    return pairs
