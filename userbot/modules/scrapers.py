import wikipedia
from google_images_download import google_images_download
import urbandict
import subprocess
import re
from datetime import datetime, timedelta
from telethon import TelegramClient, events
from userbot import bot,LOGGER,LOGGER_GROUP
from gtts import gTTS
import os
from py_translator import Translator
langi="en"


@bot.on(events.NewMessage(outgoing=True, pattern="^.img (.*)"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.img (.*)"))
async def img_sampler(e):
  if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
   await e.edit('Processing...')
   start=round(time.time() * 1000)
   s = e.pattern_match.group(1)
   lim = re.findall(r"lim=\d+", s)
   try:
     lim = lim[0]
     lim = lim.replace('lim=', '')
     s = s.replace('lim='+lim[0], '')
   except IndexError:
     lim = 2
   response = google_images_download.googleimagesdownload()
   arguments = {"keywords":s,"limit":lim, "format":"jpg"}   #creating list of arguments
   paths = response.download(arguments)   #passing the arguments to the function
   lst = paths[s]
   await bot.send_file(await bot.get_input_entity(e.chat_id), lst)
   end=round(time.time() * 1000)
   msstartend=int(end) - int(start)
   await e.edit("Done. Time taken: "+str(msstartend) + 's')


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern=r'^.google (.*)'))
@bot.on(events.MessageEdited(outgoing=True,pattern=r'^.google (.*)'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern=r"^.google (.*)"))
#@bot.on(events.MessageEdited(outgoing=True, pattern=r"^.google (.*)"))
>>>>>>> c3ebdfa... fix bug
async def gsearch(e):
      if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        match = e.pattern_match.group(1)
        result_=subprocess.run(['gsearch', match], stdout=subprocess.PIPE)
        result=str(result_.stdout.decode())
        await bot.send_message(await bot.get_input_entity(e.chat_id), message='**Search Query:**\n`' + match + '`\n\n**Result:**\n' + result, reply_to=e.id, link_preview=False)
        if LOGGER:
           await bot.send_message(LOGGER_GROUP,"Google Search query "+match+" was executed successfully")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern=r'^.wiki (.*)'))
@bot.on(events.MessageEdited(outgoing=True,pattern=r'^.wiki (.*)'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern=r"^.wiki (.*)"))
#@bot.on(events.MessageEdited(outgoing=True, pattern=r"^.wiki (.*)"))
>>>>>>> c3ebdfa... fix bug
async def wiki(e):
      if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        match = e.pattern_match.group(1)
        result=wikipedia.summary(match)
        await bot.send_message(await bot.get_input_entity(e.chat_id), message='**Search:**\n`' + match + '`\n\n**Result:**\n' + result, reply_to=e.id, link_preview=False)
        if LOGGER:
           await bot.send_message(LOGGER_GROUP,"Wiki query "+match+" was executed successfully")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.ud (.*)'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.ud (.*)'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.ud (.*)"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.ud (.*)"))
>>>>>>> c3ebdfa... fix bug
async def ud(e):
  if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
   await e.edit("Processing...")
   str = e.pattern_match.group(1)
   mean = urbandict.define(str)
   if len(mean) >= 0:
    await e.edit('Text: **'+str+'**\n\nMeaning: **'+mean[0]['def']+'**\n\n'+'Example: \n__'+mean[0]['example']+'__')
    if LOGGER:
        await bot.send_message(LOGGER_GROUP,"ud query "+str+" executed successfully.")
   else:
    await e.edit("No result found for **"+str+"**")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.tts'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.tts'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.tts"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.tts"))
>>>>>>> c3ebdfa... fix bug
async def tts(e):
  if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    textx=await e.get_reply_message()
    replye = e.text
    if textx:
         replye = await e.get_reply_message()
         replye = str(replye.message)
    else:
        replye = str(replye[5:])
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    tts = gTTS(replye,langi)
    tts.save("k.mp3")
    with open("k.mp3", "rb") as f:
        linelist = list(f)
        linecount = len(linelist)
    if linecount == 1:
        try:                       #tts on personal chats is broken
            tts = gTTS(replyes,langi)
            tts.save("k.mp3")
        except:
            await e.edit("`Some Internal Error! Try Again!`")
            return
    with open("k.mp3", "r") as speech:
        await bot.send_file(e.chat_id, 'k.mp3', voice_note=True)
        os.remove("k.mp3")
        if LOGGER:
              await bot.send_message(LOGGER_GROUP,"tts of "+replye+" executed successfully!")
        await e.delete()


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.trt'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.trt'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.trt"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.trt"))
>>>>>>> c3ebdfa... fix bug
async def translateme(e):
  if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    global langi
    translator=Translator()
    textx=await e.get_reply_message()
    message = e.text
    if textx:
         message = textx
         text = str(message.message)
    else:
        text = str(message[4:])
    reply_text=translator.translate(text, dest=langi).text
    reply_text="`Source: `\n"+text+"`\n\nTranslation: `\n"+reply_text
    await bot.send_message(e.chat_id,reply_text)
    await e.delete()
    if LOGGER:
        await bot.send_message(LOGGER_GROUP,"Translate query "+message+" was executed successfully")


<<<<<<< HEAD
@bot.on(events.NewMessage(pattern='.lang',outgoing=True))
@bot.on(events.MessageEdited(pattern='.lang',outgoing=True))
=======
@bot.on(events.NewMessage(pattern=".lang", outgoing=True))
#@bot.on(events.MessageEdited(pattern=".lang", outgoing=True))
>>>>>>> c3ebdfa... fix bug
async def lang(e):
  if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
      global langi
      message=await bot.get_messages(e.chat_id)
      langi = str(message[0].message[6:])
      if LOGGER:
         await bot.send_message(LOGGER_GROUP,"tts language changed to **"+langi+"**")
         await e.edit("tts language changed to **"+langi+"**")
