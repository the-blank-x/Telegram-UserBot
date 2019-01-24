import sqlite3
from telethon import TelegramClient, events
from userbot import bot
import re
from userbot import LOGGER, LOGGER_GROUP
from sqlalchemy import Column, String, UnicodeText, Boolean, Integer, distinct, func
import time
import asyncio


@bot.on(events.NewMessage(incoming=True))
#@bot.on(events.MessageEdited(incoming=True))
async def filter_incoming_handler(e):
    if not (await e.get_sender()).bot:
        from userbot.modules.sql_helper.filter_sql import get_filters
        listes= e.text.split(" ")
        E=get_filters(e.chat_id)
        for t in E:
            for r in listes:
                pro = re.fullmatch(t.keyword,r,flags=re.IGNORECASE)
                if pro:
                      await e.reply(t.reply)
                      return


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.addfilter\\s.*'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.addfilter\\s.*'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.filter\\s.*"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.filter\\s.*"))
>>>>>>> c3ebdfa... fix bug
async def add_filter(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
     from userbot.modules.sql_helper.filter_sql import add_filter
     message=e.text
     kek=message.split()
     string=""
     for i in range(2,len(kek)):
         string=string+" "+str(kek[i])
     add_filter(str(e.chat_id),kek[1],string)
     await e.edit("```Filter added successfully```")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.nofilter\\s.*'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.nofilter\\s.*'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.stop\\s.*"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.stop\\s.*"))
>>>>>>> c3ebdfa... fix bug
async def remove_filter(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
     from userbot.modules.sql_helper.filter_sql import remove_filter
     message=e.text
     kek=message.split(" ")
     remove_filter(e.chat_id,kek[1])
     await e.edit("```Filter removed successfully```")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.rmfilters$'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.rmfilters$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.rmfilters$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.rmfilters$"))
>>>>>>> c3ebdfa... fix bug
async def kick_marie_filter(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    await e.edit("```Will be kicking away all Marie filters.```")
    time.sleep(3)
    r = await e.get_reply_message()
    filters = r.text.split('-')[1:]
    for filter in filters:
        await e.reply('/stop %s' % (filter.strip()))
        await asyncio.sleep(0.3)
    await e.respond('/filter filters @baalajimaestro kicked them all')
    await e.respond("```Successfully purged Marie filters yaay!```\n Gimme cookies @baalajimaestro")
    if LOGGER:
          await bot.send_message(LOGGER_GROUP,"I cleaned all Marie filters at "+str(e.chat_id))


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.get filters$'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.get filters$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.filters$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.filters$"))
>>>>>>> c3ebdfa... fix bug
async def filters_active(e):
    if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        from userbot.modules.sql_helper.filter_sql import get_filters
        transact="Filters active on this chat: \n\n"
        E=get_filters(e.chat_id)
        for i in E:
            transact=transact+"🔹 "+i.keyword+"\n"
        await e.edit(transact)
