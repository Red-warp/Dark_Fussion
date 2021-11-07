from telethon import events
from userbot.utils import lightning_cmd
from userbot import CMD_HELP
@borg.on(lightning_cmd(pattern=r"repo", outgoing=True))
async def hapy(event):
     a="Hᴇʀᴇ Is ᴀ ᴏᴘ ʙᴏᴛ ᴡiᴛᕼ sᴛᴜɴɴIɴɢ ᕼᴇʟᴘ ʙʏ #TᴇᴀᴍFᴜssIᴏɴ \n\n[Đ₳Ɽ₭ Ƒմʂʂìօղ](https://github.com/TeamFussion/Dark_Fussion)"
     await event.edit(a)
