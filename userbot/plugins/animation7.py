import asyncio
from collections import deque

from . import mention


@bot.on(lightning_cmd(pattern=r"happy?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"happy?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "`I am so Happy.....`")
    deq = deque(list("😇✨🍫✨😇✨🍫✨🦋✨😊"))
    for _ in range(48):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)
        

@bot.on(lightning_cmd(pattern=r"smile$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"smile$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(70)
    event = await edit_or_reply(event, "smile")
    animation_chars = [
        "🙂",
        "🙃",
        "☺️",
        "😊",
        "😏",
        "😌",
        "🙃",
        "🙂",
        "☺️",
        "🍫",
        "😄",
        "😇",
        "You are special for me..",
        "You are so cute 😍",
        "You are special for me.."
        "You are so cute 😍",
        "🙂",
        "🙃",
        "☺️",
        "😊",
        "😏",
        "😌",
        "🙃",
        "🙂",
        "☺️",
        "🍫",
        "😄",
        "😇",
        "Now Smile!!😇😇 ",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


CMD_HELP.update(
    {
        "animation7": """**Plugin : **`animation7`
        
**Commands in animation7 are **
  •  `.happy`
  •  `.smile`
  •  by @Akki_ThePro
**Function : **__Different kinds of animation commands check yourself for their animation .__"""
    }
)
