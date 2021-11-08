"""
Say something interesting...
Syntax: .bid
    by @Deonnn
Quotes credits: Being logical Channel
"""


from telethon import events


@borg.on(events.NewMessage(pattern=r"\.bid", outgoing=True))
async def bid(event):
    giveVar = event.text
    bid = giveVar[4:5]
    if not bid:
        bid = "😂"
    await event.edit(
        f"{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}                     {bid}{bid}\n{bid}{bid}                     {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}                     {bid}{bid}\n{bid}{bid}                     {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n\n{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n          {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}\n\n{bid}{bid}                           {bid}{bid}\n{bid}{bid}{bid}                       {bid}{bid}\n{bid}{bid}{bid}{bid}                 {bid}{bid}\n{bid}{bid}  {bid}{bid}               {bid}{bid}\n{bid}{bid}     {bid}{bid}            {bid}{bid}\n{bid}{bid}         {bid}{bid}        {bid}{bid}\n{bid}{bid}             {bid}{bid}    {bid}{bid}\n{bid}{bid}                 {bid}{bid}{bid}{bid}\n{bid}{bid}                     {bid}{bid}{bid}\n{bid}{bid}                          {bid}{bid}\n\n           {bid}{bid}{bid}{bid}{bid}\n     {bid}{bid}{bid}{bid}{bid}{bid}{bid}\n   {bid}{bid}                   {bid}{bid}\n {bid}{bid}                       {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n {bid}{bid}                       {bid}{bid}\n   {bid}{bid}                   {bid}{bid}\n      {bid}{bid}{bid}{bid}{bid}{bid}{bid}\n            {bid}{bid}{bid}{bid}{bid}\n\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}                      {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                         {bid}{bid}\n{bid}{bid}                      {bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}{bid}\n{bid}{bid}{bid}{bid}{bid}{bid}{bid}"
    )
    
    
from userbot import CMD_HELP   
    
CMD_HELP.update(
    {
         "bid": "✘** Cmds** ✘: `5`\
        \n\n✘ **Cmd: ** `.alive`\
        \n➥ **Info: ** __A kind of showing bot details__\
        \n\n✘ **Cmd: ** `.falive`\
        \n➥ **Info: ** __A kind of showing bot details__\
        \n\n✘ **Cmd : ** `.halive`\
       \n➥ **Info: ** __A kind of showing bot details__\
        \n\n✘ **Cmd: ** `.valive`\
       \n➥ **Info: ** __A kind of showing bot details__\
       \n\n✘ **Cmd: ** `.dalive`\
       \n➥ **Info: ** __A kind of showing bot details__\
       \n\n👩‍💻 **Usage : __To check userbot if it is alive.__**"
    }
)
