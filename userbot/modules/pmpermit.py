#Special module to block pms automatically
from telethon.tl.functions.contacts import BlockRequest
import sqlite3
from telethon import TelegramClient, events
from userbot import bot
from userbot import PM_AUTO_BAN
from userbot import COUNT_PM
from userbot import LOGGER, LOGGER_GROUP


@bot.on(events.NewMessage(incoming=True))
<<<<<<< HEAD
=======
#@bot.on(events.MessageEdited(incoming=True))
>>>>>>> c3ebdfa... fix bug
async def permitpm(e):
  if PM_AUTO_BAN:
    global COUNT_PM
    if e.is_private and not (await e.get_sender()).bot:
       from userbot.modules.sql_helper.pm_permit_sql import is_approved
       E=is_approved(e.chat_id)
       if not E:
           await e.reply("`Bleep Blop! This is a Bot. Don't fret. \n\nMy Master hasn't approved you to PM. \
Please wait for my Master to look in, he would mostly approve PMs.\n\n\
<<<<<<< HEAD
As far as i know, he doesn't usually approve Retards.`")
           if e.chat_id not in COUNT_PM:
              COUNT_PM.update({e.chat_id:1})
           else:
              COUNT_PM[e.chat_id]=COUNT_PM[e.chat_id]+1
           if COUNT_PM[e.chat_id]>4:
               await e.respond('`You were spamming my Master\'s PM, which I don\'t like. I\'mma Report Spam.`')
               del COUNT_PM[e.chat_id]
               await bot(BlockRequest(e.chat_id))
               if LOGGER:
                   name = await bot.get_entity(e.chat_id)
                   name0 = str(name.first_name)
                   await bot.send_message(LOGGER_GROUP,'['+ name0 +'](tg://user?id='+str(e.chat_id)+')'+" was just another retarded nibba")


@bot.on(events.NewMessage(outgoing=True,pattern='^.approvepm$'))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.approvepm$"))
=======
As far as i know, he doesn't usually approve Retards.`" :
                await e.reply(
                    "`Bleep Blop! This is a Bot. Don't fret. \n\nMy Master hasn't approved you to PM. \
Please wait for my Master to look in, he would mostly approve PMs.\n\n\
As far as i know, he doesn't usually approve Retards.`"
                )
                if NOTIF_OFF:
                    await bot.send_read_acknowledge(e.chat_id)
                if e.chat_id not in COUNT_PM:
                    COUNT_PM.update({e.chat_id: 1})
                else:
                    COUNT_PM[e.chat_id] = COUNT_PM[e.chat_id] + 1
                if COUNT_PM[e.chat_id] > 4:
                    await e.respond(
                        "`You were spamming my Master's PM, which I don't like. I'mma Report Spam.`"
                    )
                    del COUNT_PM[e.chat_id]
                    await bot(BlockRequest(e.chat_id))
                    if LOGGER:
                        name = await bot.get_entity(e.chat_id)
                        name0 = str(name.first_name)
                        await bot.send_message(
                            LOGGER_GROUP,
                            "["
                            + name0
                            + "](tg://user?id="
                            + str(e.chat_id)
                            + ")"
                            + " was just another retarded nibba",
                        )


@bot.on(events.NewMessage(outgoing=True,pattern="^.notifoff$"))
#@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifoff$"))
async def notifoff(e):
    global NOTIF_OFF
    NOTIF_OFF=True
    await e.edit("`Notifications silenced!`")


@bot.on(events.NewMessage(outgoing=True,pattern="^.notifon$"))
#@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifon$"))
async def notifoff(e):
    global NOTIF_OFF
    NOTIF_OFF=False
    await e.edit("`Notifications unmuted!`")


@bot.on(events.NewMessage(outgoing=True, pattern="^.approve$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.approve$"))
>>>>>>> c3ebdfa... fix bug
async def approvepm(e):
  if not e.text[0].isalpha():
    from userbot.modules.sql_helper.pm_permit_sql import approve
    approve(e.chat_id)
    await e.edit("`Approved to PM!`")
    if LOGGER:
        aname = await bot.get_entity(e.chat_id)
        name0 = str(name.first_name)
        await bot.send_message(LOGGER_GROUP,'['+ name0 +'](tg://user?id='+str(e.chat_id)+')'+" was approved to PM you.")
