import hastebin
import pybase64
import random,re,os,signal
import subprocess
from userbot import bot
from telethon import TelegramClient, events
from userbot import LOGGER, LOGGER_GROUP


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.pip (.+)'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.pip (.+)'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.pip (.+)"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.pip (.+)"))
>>>>>>> c3ebdfa... fix bug
async def pipcheck(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    a=await e.reply('`Searching . . .`')
    r='`' + subprocess.run(['pip3', 'search', e.pattern_match.group(1)], stdout=subprocess.PIPE).stdout.decode() + '`'
    await e.edit(r)


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.paste?(\\s)'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.paste?(\\s)'))
=======
######Will put del.dog later lmao sorry Tillie
@bot.on(events.NewMessage(outgoing=True, pattern="^.paste?(\\s)"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.paste?(\\s)"))
>>>>>>> c3ebdfa... fix bug
async def haste_paste(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    message=e.text
    await e.edit('`Pasting text . . .`')
    text=str(message[7:])
    await e.edit('`Paste successful! Check it here: `' + hastebin.post(text))


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.log'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.log'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.log"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.log"))
>>>>>>> c3ebdfa... fix bug
async def log(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    textx=await e.get_reply_message()
    if textx:
         message = textx
         message = str(message.message)
    else:
        message = e.text
        message = str(message[4:])
    if LOGGER:
        await (await e.get_reply_message()).forward_to(LOGGER_GROUP)
        await e.edit("`Logged Successfully`")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True, pattern='^.speed$'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.speed$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.speed$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.speed$"))
>>>>>>> c3ebdfa... fix bug
async def speedtest(e):
     if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
            l=await e.reply('`Running speed test . . .`')
            k=subprocess.run(['speedtest-cli'], stdout=subprocess.PIPE)
            await l.edit('`' + k.stdout.decode()[:-1] + '`')
            await e.delete()


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.hash (.*)'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.hash (.*)'))
async def hash(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    hashtxt_ = e.pattern_match.group(1)
    hashtxt=open('hashdis.txt','w+')
    hashtxt.write(hashtxt_)
    hashtxt.close()
    md5=subprocess.run(['md5sum', 'hashdis.txt'], stdout=subprocess.PIPE)
    md5=md5.stdout.decode()
    sha1=subprocess.run(['sha1sum', 'hashdis.txt'], stdout=subprocess.PIPE)
    sha1=sha1.stdout.decode()
    sha256=subprocess.run(['sha256sum', 'hashdis.txt'], stdout=subprocess.PIPE)
    sha256=sha256.stdout.decode()
    sha512=subprocess.run(['sha512sum', 'hashdis.txt'], stdout=subprocess.PIPE)
    subprocess.run(['rm', 'hashdis.txt'], stdout=subprocess.PIPE)
    sha512=sha512.stdout.decode()
    ans='Text: `' + hashtxt_ + '`\nMD5: `' + md5 + '`SHA1: `' + sha1 + '`SHA256: `' + sha256 + '`SHA512: `' + sha512[:-1] + '`'
    if len(ans) > 4096:
        f=open('hashes.txt', 'w+')
        f.write(ans)
        f.close()
        await bot.send_file(e.chat_id, 'hashes.txt', reply_to=e.id, caption="`It's too big, in a text file and hastebin instead. `" + hastebin.post(ans[1:-1]))
        subprocess.run(['rm', 'hashes.txt'], stdout=subprocess.PIPE)
    else:
        await e.reply(ans)


@bot.on(events.NewMessage(outgoing=True,pattern='^.base64 (en|de) (.*)'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.base64 (en|de) (.*)'))
async def endecrypt(e):
 if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
     if e.pattern_match.group(1) == 'en':
         lething=str(pybase64.b64encode(bytes(e.pattern_match.group(2), 'utf-8')))[2:]
         await e.reply('Encoded: `' + lething[:-1] + '`')
     else:
         lething=str(pybase64.b64decode(bytes(e.pattern_match.group(2), 'utf-8'), validate=True))[2:]
         await e.reply('Decoded: `' + lething[:-1] + '`')


@bot.on(events.NewMessage(outgoing=True, pattern='^.random'))
@bot.on(events.MessageEdited(outgoing=True, pattern='^.random'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.hash (.*)"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.hash (.*)"))
async def hash(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        hashtxt_ = e.pattern_match.group(1)
        hashtxt = open("hashdis.txt", "w+")
        hashtxt.write(hashtxt_)
        hashtxt.close()
        md5 = subprocess.run(["md5sum", "hashdis.txt"], stdout=subprocess.PIPE)
        md5 = md5.stdout.decode()
        sha1 = subprocess.run(["sha1sum", "hashdis.txt"], stdout=subprocess.PIPE)
        sha1 = sha1.stdout.decode()
        sha256 = subprocess.run(["sha256sum", "hashdis.txt"], stdout=subprocess.PIPE)
        sha256 = sha256.stdout.decode()
        sha512 = subprocess.run(["sha512sum", "hashdis.txt"], stdout=subprocess.PIPE)
        subprocess.run(["rm", "hashdis.txt"], stdout=subprocess.PIPE)
        sha512 = sha512.stdout.decode()
        ans = (
            "Text: `"
            + hashtxt_
            + "`\nMD5: `"
            + md5
            + "`SHA1: `"
            + sha1
            + "`SHA256: `"
            + sha256
            + "`SHA512: `"
            + sha512[:-1]
            + "`"
        )
        if len(ans) > 4096:
            f = open("hashes.txt", "w+")
            f.write(ans)
            f.close()
            await bot.send_file(
                e.chat_id,
                "hashes.txt",
                reply_to=e.id,
                caption="`It's too big, in a text file and hastebin instead. `"
                + hastebin.post(ans[1:-1]),
            )
            subprocess.run(["rm", "hashes.txt"], stdout=subprocess.PIPE)
        else:
            await e.reply(ans)


@bot.on(events.NewMessage(outgoing=True, pattern="^.base64 (en|de) (.*)"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.base64 (en|de) (.*)"))
async def endecrypt(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if e.pattern_match.group(1) == "en":
            lething = str(pybase64.b64encode(bytes(e.pattern_match.group(2), "utf-8")))[
                2:
            ]
            await e.reply("Encoded: `" + lething[:-1] + "`")
        else:
            lething = str(
                pybase64.b64decode(
                    bytes(e.pattern_match.group(2), "utf-8"), validate=True
                )
            )[2:]
            await e.reply("Decoded: `" + lething[:-1] + "`")


@bot.on(events.NewMessage(outgoing=True, pattern="^.random"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.random"))
>>>>>>> c3ebdfa... fix bug
async def randomise(e):
  if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
    r=(e.text).split()
    index=random.randint(1,len(r)-1)
    await e.edit("**Query: **\n`"+e.text+'`\n**Output: **\n`'+r[index]+'`')


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.alive$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.alive$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.alive$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.alive$"))
>>>>>>> c3ebdfa... fix bug
async def amialive(e):
    if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        await e.edit("`Master! I am alive😁`")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.chatid$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.chatid$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.chatid$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.chatid$"))
>>>>>>> c3ebdfa... fix bug
async def chatidgetter(e):
    if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        await e.edit('Chat ID: `'+str(e.chat_id)+'`')


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.restart$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.restart$'))
async def restart_the_bot(e):
	await e.edit("`Thank You master! I am taking a break!`")


	os.execl(sys.executable, sys.executable, *sys.argv)
@bot.on(events.NewMessage(outgoing=True,pattern='^.pingme$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.pingme$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.updatebleeding$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.updatebleding$"))
async def restart_the_bot(e):
    await e.edit("`Please wait while I upstream myself!`")
    bot.disconnect()
    try:
        subprocess.run(["python", "-m", "userbot", "test", "haha"])
    except:
        pass

@bot.on(events.NewMessage(outgoing=True, pattern="^.updatestable$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.updatestable$"))
async def restart_the_bot(e):
    await e.edit("`Please wait while I upstream myself!`")
    bot.disconnect()
    try:
        subprocess.run(["python", "-m", "userbot", "test", "haha", "yes"])
    except:
        pass

@bot.on(events.NewMessage(outgoing=True, pattern="^.pingme$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.pingme$"))
>>>>>>> c3ebdfa... fix bug
async def pingme(e):
 if not e.text[0].isalpha():
    k=subprocess.run(['ping','-c','3','google.com'], stdout=subprocess.PIPE)
    await e.edit('`' + k.stdout.decode()[:-1] + '`')


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.shutdown'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.shutdown'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.sleep( [0-9]+)?$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.sleep( [0-9]+)?$"))
async def killdabot(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        if not " " in e.pattern_match.group(1):
            await e.reply("Syntax: `.shutdown [seconds]`")
        else:
            counter = int(e.pattern_match.group(1))
            await e.edit("`I am sulking and snoozing....`")
            time.sleep(2)
            await bot.send_message(
                LOGGER_GROUP,
                "You put the bot to sleep for " + str(counter) + " seconds",
            )
            time.sleep(counter)


@bot.on(events.NewMessage(outgoing=True, pattern="^.shutdown$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.shutdown$"))
>>>>>>> c3ebdfa... fix bug
async def killdabot(e):
    if not e.text[0].isalpha():
        message = e.text
        counter=int(message[10:])
        await e.reply('`Goodbye *Windows XP shutdown sound*....`')
        time.sleep(2)
        await bot.send_message(LOGGER_GROUP,"You shutdown the bot for "+str(counter)+" seconds")
        time.sleep(counter)


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='.support'))
@bot.on(events.MessageEdited(outgoing=True,pattern='.support'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.support$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.support$"))
>>>>>>> c3ebdfa... fix bug
async def bot_support(e):
    if not e.text[0].isalpha():
        await e.edit("Report bugs here: @userbot_support")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.repo$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.repo$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.repo$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.repo$"))
>>>>>>> c3ebdfa... fix bug
async def repo_is_here(e):
    if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        await e.edit('https://github.com/baalajimaestro/Telegram-UserBot/')


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.supportchannel$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.supportchannel$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.supportchannel$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.supportchannel$"))
>>>>>>> c3ebdfa... fix bug
async def support_channel(e):
    if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        await e.edit('t.me/maestro_userbot_channel')


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.sysdetails$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.sysdetails$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.sysd$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.sysd$"))
>>>>>>> c3ebdfa... fix bug
async def sysdetails(e):
    if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        r='`' + subprocess.run(['neofetch', '--off', '--color_blocks off', '--bold off', '--cpu_temp', 'C', '--cpu_speed','on','--cpu_cores', 'physical','--stdout'], stdout=subprocess.PIPE).stdout.decode() + '`'
        await e.edit(r)


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.botversion$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.botversion$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.botversion$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.botversion$"))
>>>>>>> c3ebdfa... fix bug
async def bot_ver(e):
    if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        await e.edit('`UserBot Version: Modular r2.07-b`')


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern='^.userid$'))
@bot.on(events.MessageEdited(outgoing=True,pattern='^.userid$'))
=======
@bot.on(events.NewMessage(outgoing=True, pattern="^.userid$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.userid$"))
>>>>>>> c3ebdfa... fix bug
async def chatidgetter(e):
    if not e.text[0].isalpha() and e.text[0]!="!" and e.text[0]!="/" and e.text[0]!="#" and e.text[0]!="@":
        message = await e.get_reply_message()
        if message:
            if not message.forward:
                user_id = message.sender.id
                if message.sender.username:
                    name = '@' + message.sender.username
                else:
                    name = '**' + message.sender.first_name + '**'

            else:
                user_id = message.forward.sender.id
                if message.forward.sender.username:
                    name = '@' + message.forward.sender.username
                else:
<<<<<<< HEAD
                    name = '*' + message.forward.sender.first_name + '*'
            await e.edit('This beautiful person named {} has this amazing id: `{}`'.format(name, user_id))
=======
                    name = "*" + message.forward.sender.first_name + "*"
            await e.edit("**Name:** {} \n**User ID:** `{}`".format(name, user_id))

@bot.on(events.NewMessage(outgoing=True, pattern="^\$"))
async def rextestercli(e):
    stdin = ""
    message = e.text

    if len(message.split()) > 1:
        regex = re.search('^\$([\w.#+]+)\s+([\s\S]+?)(?:\s+\/stdin\s+([\s\S]+))?$', message, re.IGNORECASE)
        language = regex.group(1)
        code = regex.group(2)
        stdin = regex.group(3)



        try:
            regexter = Rextester(language, code, stdin)
        except CompilerError as exc:
            await e.edit(str(exc))
            return

        output = ""
        output += "**Language:**\n```{}```".format(language)
        output += "\n\n**Source:** \n```{}```".format(code)

        if regexter.result:
            output += "\n\n**Result:** \n```{}```".format(regexter.result)

        if regexter.warnings:
            output += "\n\n**Warnings:** \n```{}```\n".format(regexter.warnings)

        if regexter.errors:
            output += "\n\n**Errors:** \n'```{}```".format(regexter.errors)

        await e.edit(output)


@bot.on(events.NewMessage(outgoing=True, pattern="^.unmutechat$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.unmutechat$"))
async def unmute_chat(e):
        if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
            try:
                from userbot.modules.sql_helper.keep_read_sql import unkread
            except:
                await e.edit('`Running on Non-SQL Mode!`')
            unkread(str(e.chat_id))
            await e.edit("```Unmuted this chat Successfully```")


@bot.on(events.NewMessage(outgoing=True, pattern="^.mutechat$"))
#@bot.on(events.MessageEdited(outgoing=True, pattern="^.mutechat$"))
async def mute_chat(e):
        if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
            try:
                from userbot.modules.sql_helper.keep_read_sql import kread
            except Exception as er:
                print(er)
                await e.edit("`Running on Non-SQL mode!`")
                return
            await e.edit(str(e.chat_id))
            kread(str(e.chat_id))
            await e.edit("`Shush! This chat will be silenced!`")
            if LOGGER:
                await bot.send_message(
                    LOGGER_GROUP,
                    str(e.chat_id) + " was silenced.")


@bot.on(events.NewMessage(incoming=True))
#@bot.on(events.MessageEdited(incoming=True))
async def keep_read(e):
    try:
        from userbot.modules.sql_helper.keep_read_sql import is_kread
    except:
        return
    K = is_kread()
    if K:
      for i in K:
        if i.groupid == str(e.chat_id):
            await bot.send_read_acknowledge(e.chat_id)
>>>>>>> c3ebdfa... fix bug
