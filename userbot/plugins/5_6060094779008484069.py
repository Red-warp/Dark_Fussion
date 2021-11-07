

from telethon import events
import asyncio
from userbot.utils import admin_cmd
import importlib.util
import random, re

@borg.on(admin_cmd(pattern="diwali$"))

async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 30)
    await event.edit("🥰Happy Diwali🥰")
    animation_chars = [          
              "❤️happy♥️diwali❤️\n❤️happy♥️diwali♥️\n❤️happy♥️diwali♥️\n❤️happy♥️diwali♥️\n♥️happy❤️diwali♥️\n❤️happy♥️diwali❤️\n♥️happy❤️diwali♥️\n❤️happy♥️diwali❤️\n♥️happy❤️diwali♥️\n❤️happy♥️diwali❤️\n♥️happy❤️diwali♥️\n♥️happy❤️diwali❤️\n♥️happy❤️diwali♥️\n♥️happy♥️diwali♥️\n❤️happy♥️diwali♥️\n❤️happy♥️diwali♥️\n❤️happy♥️diwali♥️",
              "💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙\n💙happy💙diwali💙",
              "💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜\n💜happy💜diwali💜",
              "💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖\n💖happy💖diwali💖",
              "💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚\n💚happy💚diwali💚",
              
              "[ㅤ](https://telegra.ph/file/0bd9215efcd23a55dd115.mp4)"
          ]
    for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %6 ], link_preview=True)#