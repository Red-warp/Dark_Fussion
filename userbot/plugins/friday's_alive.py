"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import os
import time

from userbot import ALIVE_NAME, Lastupdate
from userbot.plugins import currentversion
from userbot.utils import lightning_cmd, sudo_cmd

FRI_IMAGE = os.environ.get("FRI_IMAGE", None)
if FRI_IMAGE is None:
    FRI_IMG = "https://te.legra.ph/file/91e5001521689a5967b0a.mp4"
else:
    FRI_IMG = FRI_IMAGE


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

pm_caption = (f"     __**Đ₳Ɽ₭ Ƒմʂʂìօղ - Ⲟⲛⳑⲓⲛⲉ**__\n\n╔═════𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐔𝐒════❍⊱❁۪۪\n")
pm_caption += "║\n"
pm_caption += "║⪼ **SYSTEMS STATS**\n"
pm_caption += "║⪼ **Telethon Version:** `1.21.0` \n"
pm_caption += "║⪼ **Python:** `3.9.96` \n"
pm_caption += f"║⪼ **Uptime** : `{uptime}` \n"
pm_caption += "║⪼ **Database Status:**  `Functional`\n"
pm_caption += "║⪼ **Current Branch** : `master`\n"
pm_caption += f"║⪼ **Version** : `{currentversion}`\n"
pm_caption += f"║⪼ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "║⪼ **Heroku Database** : `AWS - Working`\n"
pm_caption += "║⪼ **License** : [GNU](https://github.com/TeamFussion/Dark_Fussion/master/LICENSE)\n"
pm_caption += "║⪼ **Copyright** : By [ཞ𝔼𝔻 𝕎𝔸ℝℙ](GitHub.com/TeamFussion)\n"
pm_caption += "║⪼ **Check Stats By Doing** `.status`. \n"
pm_caption += "║\n"
pm_caption += "╚═════𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐔𝐒════❍⊱❁۪۪"


@borg.on(lightning_cmd(pattern=r"falive"))
@borg.on(sudo_cmd(pattern=r"falive", allow_sudo=True))
async def friday(falive):
    await falive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(falive.chat_id, FRI_IMG, caption=pm_caption)
    await falive.delete()
