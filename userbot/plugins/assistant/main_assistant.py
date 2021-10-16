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
    starttext = f"Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Assistant Bot. \n\nMy [➤ Master](tg://user?id={bot.uid}) \nYou Can Talk/Contact My Master Using This Bot. \n\nIf You Want Your Own Assistant You Can Deploy From Button Below. \n\nPowered By [вℓα¢к ℓιgнтηιηg](https://t.me/lightning_support_group)"
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"Hi Master, It's Me {bot_id}, Your Assistant ! \nWhat You Wanna Do today ?",
            buttons=[
                [
                    Button.url(
                        "✘ Add Me to Group ✘", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
                [custom.Button.inline("✘ Users List ✘", data="users"),
                custom.Button.inline("✘ Commands ✘", data="gibcmd")],
                [Button.url("✘ Support ✘" , "https://t.me/Dark_Fussion_chat"),
                  Button.url("✘ Updates ✘" , "https://t.me/DarkFussion")],
                [custom.Button.inline("✘ Settings ✘" , data="settings")],
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
                [custom.Button.inline("Deploy your BL ", data="deploy")],
                [Button.url("Help Me ❓", "https://t.me/lightning_support_group")],
                [Button.url("Lightning Web💫", "https://lightninguserbot.blogspot.com")],
            ],
        )


# Data's

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="You Can Deploy Black Lightning In Heroku By Following Steps Bellow, You Can See Some Quick Guides On Support Channel Or On Your Own Assistant Bot. \nThank You For Contacting Me.",
            buttons=[
                [
                    Button.url(
                        "Deploy Tutorial 📺",
                        "https://www.youtube.com/watch?v=GfZMqrCAqxI",
                    )
                ],
                [Button.url("Need Help ❓", "https://t.me/lightning_support_group")],
                [Button.url("Lightning Web💫", "https://lightninguserbot.blogspot.com")],
            ],
        )


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


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"red")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"Hi Master, It's Me {bot_id}, Your Assistant ! \nWhat You Wanna Do today ?",
            buttons=[
                [Button.url("✘ Add Me to Group ✘", f"t.me/{bot_username}?startgroup=true")],
                [Button.inline("✘ Users List ✘", data="users"),
                 Button.inline("✘ Commands ✘", data="gibcmd")],
                [Button.url("✘ Support ✘" , "https://t.me/Dark_Fussion_chat"),  
                Button.url("✘ Updates ✘" , "https://t.me/DarkFussion")],
                [Button.inline("✘ Settings ✘" , data="settings")],
              ],
          )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**What do you want to edit in Alive?\nYou can anything from these..!!\nAny kind for help do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat)**",
            buttons=[
        [Button.inline("✘ Alive Name ✘", data="name"), 
         Button.inline("✘ Alive Pic ✘", data="img")], 
        [Button.inline("🚫 Cancel 🚫", data="settings")], 
            ],
        )
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"img")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**Which Alive pic do you want to change?\nFor Any kind for help do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat)**",
            buttons=[
        [Button.inline("✘ Fussion Alive ✘", data="aimg"), 
         Button.inline("✘ Friday Alive ✘", data="fimg")], 
        [Button.inline("✘ Hell_bot Alive ✘", data="halive"), 
         Button.inline("✘ DC_Alive ✘", data="dalive")], 
        [Button.inline("✘ Back ✘", data="alive")], 
        [Button.inline("🚫 Cancel 🚫", data="settings")], 
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"name")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Name..!!\nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var ALIVE_NAME <Telegraph Link>`\n\nRemove <> this.l**",
            buttons=[
       [Button.inline("✘ Back ✘", data="alive")],
       [Button.inline("🚫 Cancel 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aimg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.alive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var ALIVE_PIC <Telegraph Link>`\n\nRemove <> this.**",
            buttons=[
       [Button.inline("✘ Back ✘", data="img")],
       [Button.inline("🚫 Cancel 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"fimg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.falive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var FRI_IMAGE <Telegraph Link>`\n\nRemove <> this.**",
            buttons=[
       [Button.inline("✘ Back ✘", data="img")],
       [Button.inline("🚫 Cancel 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dalive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.dalive` \nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var ALIVE_PHOTTO <Telegraph Link>`\n\nRemove <> this.**",
            buttons=[
       [Button.inline("✘ Back ✘", data="img")],
       [Button.inline("🚫 Cancel 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"halive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(

       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for .halive..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var HELL_IMG <Telegraph Link>`\n\nRemove <> this.**",
            buttons=[
       [Button.inline("✘ Back ✘", data="img")],
       [Button.inline("🚫 Cancel 🚫", data="settings")],  
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
       [Button.inline("✘ Pm permit Text ✘", data="text"),
       Button.inline("✘ Pm permit Media ✘", data="media")],
       [Button.inline("🚫 Cancel 🚫", data="settings")],  
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"media")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit Pic..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](t.me/Dark_Fussion_chat)\n\nJust type\n\n`.set var LIGHTNING_BOT_PIC <Telegraph Link>`\n\nRemove <> this.**",
            buttons=[
       [Button.inline("✘ Back ✘", data="permit")],
       [Button.inline("🚫 Cancel 🚫", data="settings")],  
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"settings")))
async def help(event):
    await event.delete()
   if event.query.user_id == bot.uid:
       await tgbot.send_message(
            event.chat_id,
            message=f"**Which type of setting do you want to edit?\nYou can anything from these..!!\nAny kind for help do join [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat)**",
            buttons=[
        [Button.inline("✘ Alive ✘", data="alive"), 
         Button.inline("✘ Pm Permit ✘", data="permit")], 
        [Button.inline("✘ Chat Bot ✘", data="chat"), 
         Button.inline("✘ Vc Bot ✘", data="Vc_Bot")], 
        [Button.inline("✘ Back ✘", data="red")], 
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
