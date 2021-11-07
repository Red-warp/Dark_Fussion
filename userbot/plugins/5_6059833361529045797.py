#Happy Diwali plugin by @A_B_HA_Y_AB 
#Uploaded on @opplugins channel
#Kang with credits else gay

from . import *

@bot.on(admin_cmd(pattern=r"hdw$"))
@bot.on(sudo_cmd(pattern="hdw$", allow_sudo=True))

async def _(event):
   
    animation_interval = 3
    animation_ttl = range(4)
    event = await edit_or_reply(event, "Happy Diwali ❤")
    animation_chars = [
        """┌───── •✧✧• ─────┐
    🎉HAPPY DIWALI 🎇 
└───── •✧✧• ─────┘""",
"""Dear friends, celebrate this meaningful occasion by spreading love and laughter! Happy Diwali!""",
"""。　☆ 。　　☆。　　☆ 
★。　＼　　｜　　／。　★
 　   　 Happy Diwali 🥳。 
★。　／　　｜　　＼。　★ 
。　☆。 　　。　　☆。""",
"""GIVE OUT CHILDREN A GREEN FUTURE. SAY NO TO FIREWORKS. HAPPY DIWALI 2021!""",
]

    for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
