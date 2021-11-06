#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import io
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest
from userbot.utils import assistant_cmd
from userbot import bot
from userbot.plugins.sql_helper.blacklist_assistant import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from userbot.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid
from userbot.plugins.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)

@assistant_cmd("start", is_args=False)
async def start(event):
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    bot_username = starkbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    starttext = f"Hᴇʟʟᴏ {firstname} ❤️\nHᴇy Myꜱᴇʟꜰ **{bot_id}** , Aꜱꜱɪꜱᴛᴀɴᴛ Bᴏᴛ Oꜰ My Mᴀꜱᴛᴇʀ\nU Cᴀɴ Cᴏɴᴛᴀᴄᴛ My Mᴀꜱᴛᴇʀ Tʜʀᴏᴜɢʜ Mᴇ ...🥰\nFᴇᴇʟ Fʀᴇᴇ Tᴏ Mᴇꜱꜱᴀɢᴇ.....\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nRᴇᴀᴅ Tʜᴇ Rᴜʟᴇꜱ Bᴇʟᴏᴡ......⚠️\n\n🔰 Wʜᴇɴ I Gᴇᴛ Fʀᴇᴇ Tɪᴍᴇ , I ʟʟ Rᴇᴩʟy U 💯✅"
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"Hi Master, It's Me {bot_id}, Your Assistant ! \nWhat You Want Do today ?",
            buttons=[
                [
                    Button.url(
                        "✘ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ✘", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
                [custom.Button.inline("✘ Usᴇʀs Lɪsᴛ ✘", data="users"),
                custom.Button.inline("✘ Cᴏᴍᴍᴀɴᴅs ✘", data="gibcmd")],
               # [Button.url("✘ Support ✘" , "https://t.me/Dark_Fussion_chat"),
                #  Button.url("✘ Updates ✘" , "https://t.me/DarkFussion")],
                [custom.Button.inline("✘ Sᴇᴛᴛɪɴɢs ✘" , data="settings")],
                [custom.Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫" , data="close")],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_message(
            event.chat_id,
            message=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("Rᴜʟᴇꜱ", data="rules")],
            ],
        )


# Data's

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rules")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="🔰Rᴇᴀᴅ Tʜᴇ Rᴜʟᴇꜱ Tᴏᴏ🔰\n\n🔹 Dᴏɴ'ᴛ Sᴩᴀᴍ\n🔹 ᴛᴀʟᴋ Fʀɪᴇɴᴅʟy\n🔹 Dᴏɴ'ᴛ Bᴇ Rᴜᴅᴇ\n🔹 Sᴇɴᴅ Uʀ Mᴇꜱꜱᴀɢᴇꜱ Hᴇʀᴇ\n🔹 Nᴏ Pᴏʀɴᴏɢʀᴀᴘʜʏ\n🔹 Dᴏɴ'ᴛ Wʀɪᴛᴇ Bᴀᴅ Wᴏʀᴅs.\n\n\nWʜᴇɴ I Gᴇᴛ Fʀᴇᴇ Tɪᴍᴇ , I'ʟʟ Rᴇᴩʟy U 💯✅",
            buttons=[
                [
                    custom.Button.inline(
                        "Cʟᴏsᴇ",
                        data="close_vcc",
                    )
                ],
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close_vcc")))
async def users(event):
    if event.query.user_id != bot.uid:
       await event.delete()


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def users(event):
    if event.query.user_id == bot.uid:
       await event.delete()

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "List Of Total Users In Bot. \n\n"
        for starked in total_users:
            users_list += ("==> {} \n").format(int(starked.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )
    else:
        pass

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Yᴏ Eᴅɪᴛ Iɴ Aʟɪᴠᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat)**",
            buttons=[
        [Button.inline("✘ Aʟɪᴠᴇ Nᴀᴍᴇ ✘", data="name"), 
         Button.inline("✘ Aʟɪᴠᴇ Pɪᴄ ✘", data="img")], 
        [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")], 
            ],
        )
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"img")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜɪᴄʜ Aʟɪᴠᴇ Pɪᴄ Dᴏ Yᴏᴜ Wᴀɴᴛ Tᴏ Cʜᴀɴɢᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat)**",
            buttons=[
        [Button.inline("✘ Dᴇғᴀᴜʟᴛ Aʟɪᴠᴇ ✘", data="aimg"), 
         Button.inline("✘ Fʀɪᴅᴀʏ's Aʟɪᴠᴇ ✘", data="fimg")], 
        [Button.inline("✘ Hᴇʟʟ Bᴏᴛ's Aʟɪᴠᴇ ✘", data="halive"), 
         Button.inline("✘ Dᴄ's Aʟɪᴠᴇ ✘", data="dalive")], 
        [Button.inline("✘ Bᴀᴄᴋ ✘", data="alive")], 
        [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")], 
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"name")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**Yᴏᴜ Cᴀɴ Cʜᴀɴɢᴇ Aʟɪᴠᴇ Nᴀᴍᴇ..!!\nJᴜsᴛ Fᴏʟʟᴏᴡ Tʜᴇ Sᴛᴇᴘs.! \n\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Pʀᴏʙʟᴇᴍ Oʀ Dᴏᴜʙᴛ Dᴏ Jᴏɪɴ [Đ₳Ɽ₭ Ƒմʂʂìօղ](http://t.me/Dark_Fussion_chat)\n\nJᴜsᴛ Tʏᴘᴇ\n\n`.set var ALIVE_NAME <Name>`\n\nRᴇᴍᴏᴠᴇ `<>` Tʜɪs.**",
            buttons=[
       [Button.inline("✘ Bᴀᴄᴋ ✘", data="alive")],
       [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aimg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.alive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var ALIVE_PIC <Telegraph Link>`\n\nRemove `<>` this**",
            buttons=[
       [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
       [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fimg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.falive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var FRI_IMAGE <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
       [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
       [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dalive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.dalive` \nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var ALIVE_PHOTTO <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
       [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
       [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"halive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.halive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var HELL_IMG <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
       [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
       [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"permit")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**What do you want to edit in Pm Permit?\nFor Any kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)**",
            buttons=[
       [Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Tᴇxᴛ ✘", data="text"),
       Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Mᴇᴅɪᴀ ✘", data="media")],
       [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"media")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit Pic..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var LIGHTNING_BOT_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
       [Button.inline("✘ Bᴀᴄᴋ ✘", data="permit")],
       [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"text")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit message..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var LIGHTNING_WARN <Text>`\n\nRemove `<>` this.**",
            buttons=[
       [Button.inline("✘ Bᴀᴄᴋ ✘", data="permit")],
       [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="settings")],  
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"settings")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**Which type of setting do you want to edit?\nYou can change anything from these..!!\nAny kind for help do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat)**",
            buttons=[
        [Button.inline("✘ Aʟɪᴠᴇ ✘", data="alive"), 
         Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ ✘", data="permit")], 
       # [Button.inline("✘ Chat Bot ✘", data="chat"), 
       #  Button.inline("✘ Vc Bot ✘", data="Vc_Bot")], 
        [Button.inline("✘ Bᴀᴄᴋ ✘", data="redwarp")], 
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"redwarp")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
               message=f"Hi Master, It's Me {bot_id}, Your Assistant ! \nWhat You Wanna Do today ?",
               buttons=[
                [custom.Button.inline("✘ Usᴇʀs Lɪsᴛ ✘", data="users"),
                custom.Button.inline("✘ Cᴏᴍᴍᴀɴᴅs ✘", data="gibcmd")],
               # [Button.url("✘ Support ✘" , "https://t.me/Dark_Fussion_chat"),
               #   Button.url("✘ Updates ✘" , "https://t.me/DarkFussion")],
                [custom.Button.inline("✘ Sᴇᴛᴛɪɴɢs ✘" , data="settings")],
                [custom.Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫" , data="close")],
            ],
        )



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    grabon = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /ban - Works In Group , Bans A User. \n➤ /unban - Unbans A User in Group \n➤ /promote - Promotes A User \n➤ /demote - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
    await tgbot.send_message(event.chat_id, grabon)


# Bot Permit.
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.raw_text.startswith("/"):
        pass
    elif event.sender_id == bot.uid:
        return
    else:
        await event.get_sender()
        event.chat_id
        sed = await event.forward_to(bot.uid)
        # Add User To Database ,Later For Broadcast Purpose
        # (C) @SpecHide
        add_me_in_db(sed.id, event.sender_id, event.id)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    msg.id
    msg_s = event.raw_text
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id == bot.uid:
        if event.raw_text.startswith("/"):
            pass
        else:
            await tgbot.send_message(user_id, msg_s)


# broadcast
@tgbot.on(
    events.NewMessage(
        pattern="^/broadcast ?(.*)", func=lambda e: e.sender_id == bot.uid
    )
)
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            sent_count += 1
            await tgbot.send_message(int(starkcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            try:
                logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}")
            except:
                pass
    await tgbot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


@tgbot.on(
    events.NewMessage(pattern="^/stats ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    starkisnoob = get_all_users()
    await event.reply(
        f"**Stats Of Your Bot** \nTotal Users In Bot => {len(starkisnoob)}"
    )


@tgbot.on(events.NewMessage(pattern="^/help", func=lambda e: e.sender_id == bot.uid))
async def starkislub(event):
    grabonx = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot"
    await event.reply(grabonx)


@tgbot.on(
    events.NewMessage(pattern="^/block ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        user_id, reply_message_id = his_userid(msg.id)
        await event.reply("Already Blacklisted")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )


@tgbot.on(
    events.NewMessage(pattern="^/unblock ?(.*)", func=lambda e: e.sender_id == bot.uid)
)
async def starkisnoob(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even. Blacklisted 🤦🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("DisBlacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "Congo! You Have Been Unblacklisted By My Master."
        )
