import inspect
import hastebin
import subprocess
from userbot import LOGGER, LOGGER_GROUP
from telethon import TelegramClient, events
from userbot import bot


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.eval'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.eval'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.eval"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.eval"))
>>>>>>> c3ebdfa... fix bug
async def evaluate(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    evaluation = eval(e.text[6:])
    if evaluation:
      if len(evaluation) > 4096:
          f=open('output.txt', 'w+')
          f.write(evaluation)
          f.close()
          await bot.send_file(e.chat_id, 'output.txt', reply_to=e.id, caption="`Output too large, sending as file`")
          subprocess.run(['rm', 'sender.txt'], stdout=subprocess.PIPE)
      await e.edit("**Query: **\n`"+e.text[6:]+'`\n**Result: **\n`'+str(evaluation)+'`')
    else:
      await e.edit("**Query: **\n`"+e.text[6:]+'`\n**Result: **\n`No Result Returned/False`')
    if LOGGER:
      await bot.send_message(LOGGER_GROUP,"Eval query "+e.text[6:]+" was executed successfully")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern=r'^.exec (.*)'))
@bot.on(events.MessageEdited(outgoing=True, pattern=r'^.exec (.*)'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern=r"^.exec (.*)"))
#@bot.on(events.MessageEdited(outgoing=True, pattern=r"^.exec (.*)"))
>>>>>>> c3ebdfa... fix bug
async def run(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
  code = e.raw_text[5:]
  exec(
   f'async def __ex(e): ' +
   ''.join(f'\n {l}' for l in code.split('\n'))
  )
  result = await locals()['__ex'](e)
  if result:
      if len(result) > 4096:
          f=open('output.txt', 'w+')
          f.write(result)
          f.close()
          await bot.send_file(e.chat_id, 'output.txt', reply_to=e.id, caption="`Output too large, sending as file`")
          subprocess.run(['rm', 'output.txt'], stdout=subprocess.PIPE)
      await e.edit("**Query: **\n`"+e.text[5:]+'`\n**Result: **\n`'+str(result)+'`')
  else:
   await e.edit("**Query: **\n`"+e.text[5:]+'`\n**Result: **\n`'+'No Result Returned/False'+'`')
  if LOGGER:
     await bot.send_message(LOGGER_GROUP,"Exec query "+e.text[5:]+" was executed successfully")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.term'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.term'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.term"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.term"))
>>>>>>> c3ebdfa... fix bug
async def terminal_runner(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    message=e.text
    command = str(message)
    list_x=command.split(' ')
    result=subprocess.run(list_x[1:], stdout=subprocess.PIPE)
    result=str(result.stdout.decode())
    if len(result) > 4096:
        f=open('output.txt', 'w+')
        f.write(result)
        f.close()
        await bot.send_file(e.chat_id, 'sender.txt', reply_to=e.id, caption="`Output too large, sending as file`")
        subprocess.run(['rm', 'output.txt'], stdout=subprocess.PIPE)
    await e.edit("**Query: **\n`"+str(command[6:])+'`\n**Output: **\n`'+result+'`')
    if LOGGER:
        await bot.send_message(LOGGER_GROUP,"Terminal Command "+ str(list_x[1:])+" was executed sucessfully")
