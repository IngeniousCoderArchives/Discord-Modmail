# Main Bot Script
import discord
import os
from config import *
from discord.ext import commands
from ticket_log_heroku import ticketlog as create_tlog
import textwrap
from contextlib import redirect_stdout
from discord import Webhook, RequestsWebhookAdapter
import time
from random import choice
import ast
import io, traceback
from datetime import datetime, timedelta
t_1_uptime = time.perf_counter()

default_config = {
"MainGuildID" : int(os.environ.get("MainGuildID")),
"StaffGuildID" : int(os.environ.get("StaffGuildID")),
"ModMailCatagoryID" : int(os.environ.get("ModMailCatagoryID")),
"DiscordModmailLogChannel" : int(os.environ.get("DiscordModmailLogChannel")),
"BotToken" : os.environ.get("BotToken"),
"BotPlayingStatus" : os.environ.get("BotPlayingStatus"),
"BotPrefix" : os.environ.get("BotPrefix"),
"LogCommands" : os.environ.get("LogCommands"),
"BotBoundToGuilds" : os.environ.get("BotBoundToGuilds"),
"BotDMOwnerOnRestart" : os.environ.get("BotDMOwnerOnRestart"),
"BotAutoReconnect" : os.environ.get("BotAutoReconnect")
}

bot = commands.Bot(command_prefix=default_config.get('BotPrefix'),description="IngeniousCoder's Modmail Bot")
bot.remove_command("help")



@bot.event
async def on_ready():
    global bot_owner
    bot_owner = await bot.application_info()
    bot_owner = bot_owner.owner
    guild = discord.utils.get(bot.guilds,id=default_config.get("StaffGuildID"))
    already_done = False
    overwrites = {
      guild.default_role: discord.PermissionOverwrite(read_messages=False),
      guild.me: discord.PermissionOverwrite(read_messages=True)
     }
    for channel in guild.channels:
        if channel.name == "MMDATA":
            already_done = True
    if not already_done:
        await bot_owner.send("A Catagory MMDATA has been created. DO NOT delete **anything there.** **DO NOT SEND ANY MESSAGES INTO ANY CHANNEL TOO.**")
        catag = await guild.create_category_channel(name="MMDATA",overwrites=overwrites)
        txt = await guild.create_text_channel(name="mm-ticket-cache",category=catag)
        await txt.edit(topic="{}")
        txt = await guild.create_text_channel(name="mm-logs",category=catag)
        await txt.edit(topic="{}")
        txt = await guild.create_text_channel(name="mm-blacklist",category=catag)
        await txt.edit(topic="[]")
    
    print("Bot has logged in!")
    if default_config.get("BotDMOwnerOnRestart"):
        await bot_owner.send("The Modmail Bot has Restared! \nNote: You specified for the bot to message you on restart. To disable, Change BotDMOwnerOnRestart in config.py to False.")
    await bot.change_presence(activity=discord.Game(name=default_config.get("BotPlayingStatus")))
    if default_config.get("BotBoundToGuilds"):
        for guild in bot.guilds:
            if guild.id == default_config.get("MainGuildID") or guild.id == default_config.get("StaffGuildID"):
                pass
            else:
                await guild.leave()
                print(f"Left {guild.name} as it is not the staff / main guild. If you do not want me to leave guilds that are not the main / staff guilds, specify in the config.")


@bot.event
async def on_command(ctx):
    if default_config.get("LogCommands"):
        #Log
        user = ctx.author
        guild = ctx.guild
        if guild == None:
            guild = FakeDMGuild(name="DMs")
        print(f"{user.name}#{user.discriminator} used command `{ctx.message.content}` in {guild.name}.")
        file = open("Logs.txt","r")
        now_content = file.read()
        file.close()
        file = open("Logs.txt","w")
        write_content = now_content+f"\n{user.name}#{user.discriminator} in {guild.name} : {ctx.message.content}"
        file.write(write_content)
        file.close()


class FakeDMGuild():
    def __init__(self,name):
        self.name = name


def GetTime(sec):
    sec = timedelta(seconds=round(sec))
    d = datetime(1,1,1) + sec

    print("DAYS:HOURS:MIN:SEC")
    print("%d Days, %d Hours, %d Minutes and %d Seconds." % (d.day-1, d.hour, d.minute, d.second))
    return "%d Days, %d Hours, %d Minutes and %d Seconds." % (d.day-1, d.hour, d.minute, d.second)


@bot.command()
async def help(ctx):
    if ctx.guild.id == default_config.get("StaffGuildID"):
      prefix = default_config.get("BotPrefix")
      main_guild = bot.get_guild(default_config.get("MainGuildID"))
      help1 = discord.Embed(title='Hello!', description=f"I am an instance of [IngeniousCoder\'s Modmail Bot](https://github.com/IngeniousCoder/Discord-Modmail). DM me to contact the moderators of {main_guild.name}!", colour=0xDEADBF)
      help1.set_author(name='IngeniousCoder\'s Modmail Bot',icon_url="https://cdn.discordapp.com/attachments/388917080570986526/490075804496297995/8eebd924aeb72f681f0bc7c94226883e.png")
      help1.add_field(name="Help me!",value="Donate to me [here](https://patreon.com/eltontay11) or [Star my repository!](https://github.com/IngeniousCoder/Discord-Modmail)",inline=False)
      help1.add_field(name="{}uptime".format(prefix), value="Shows bot uptime", inline=False)
      help1.add_field(name="{}help".format(prefix), inline=False, value="Shows the help message.")
      help1.add_field(name="{}info".format(prefix), inline=False, value="Shows bot info.")
      help1.add_field(name="**{}reply <msg>**".format(prefix), inline=False, value="Reply to a message thread. `Alias : r`")
      help1.add_field(name="**{}close**".format(prefix), inline=False, value="Close a thread.")
      help1.add_field(name="**{}logs <uuid>**".format(prefix), inline=False, value="Get modmail logs for a user.")
      help1.add_field(name="**{}eval <code>**".format(prefix), inline=False, value="Evaluate a code.")
      help1.add_field(name="**{}blacklist <user>**".format(prefix), inline=False, value="Blacklist a user from using modmail. **If user has an existing thread, he/she is allowed to finish the thread.**")
      help1.add_field(name="**{}unblacklist <code>**".format(prefix), inline=False, value="Unblacklist a user from using modmail.")
      help1.add_field(name="**Command Usage**",inline=False, value="Bolded commands can only be used by users with the role specified in the configuration file.")
      help1.set_footer(text="IngeniousMail™ V1.0 - Soruce code is available in Github!")
      await ctx.send(embed=help1)
    else:
      await ctx.send("This command only works in the staff guild. If you are a user who wants to use the bot, information can be found here : https://github.com/IngeniousCoder/Discord-Modmail")



#@bot.command()
#@commands.check(can_use_staff_commands)
#async def info(ctx):
#    await ctx.send("Hi!")

@bot.command()
async def info(ctx):
    guild_main = bot.get_guild(default_config.get("MainGuildID"))
    main_guild = guild_main
    t_2_uptime = time.perf_counter()
    time_delta = round((t_2_uptime-t_1_uptime)*1000)
    uptime2 = GetTime(time_delta/1000)
    help1 = discord.Embed(title='Hello!', description=f"I am an instance of [IngeniousCoder\'s Modmail Bot](https://github.com/IngeniousCoder/Discord-Modmail). DM me to contact the moderators of {main_guild.name}!", colour=0xDEADBF)
    help1.set_author(name='IngeniousCoder\'s Modmail Bot',icon_url="https://cdn.discordapp.com/attachments/388917080570986526/490075804496297995/8eebd924aeb72f681f0bc7c94226883e.png")
    help1.add_field(name="Help me!",value="Donate to me [here](https://patreon.com/eltontay11) or [Star my repository!](https://github.com/IngeniousCoder/Discord-Modmail)",inline=False)
    help1.add_field(name="Uptime", value=f"{uptime2}", inline=False)
    help1.add_field(name="Operating on", value=guild_main.name)
    help1.add_field(name="Discord.py Rewrite Version", value=discord.__version__)
    help1.add_field(name="Source", value="https://github.com/IngeniousCoder/Discord-Modmail")
    help1.set_footer(text="IngeniousMail™ V1.0 - Soruce code is available in Github!")
    await ctx.send(embed=help1)


@bot.command()
async def uptime(ctx):
  t_2_uptime = time.perf_counter()
  time_delta = round((t_2_uptime-t_1_uptime)*1000)
  await ctx.send("I have been up for `{}`!".format(GetTime(time_delta/1000)))

@bot.command(pass_context=True)
async def eval(ctx, *, body: str):
    """Evaluates a code"""

    env = {
        'bot': bot,
        'ctx': ctx,
        'channel': ctx.message.channel,
        'author': ctx.message.author,
        'guild': ctx.message.guild,
        'message': ctx.message,
       }
    if ctx.message.author.id == bot_owner.id or ctx.message.author.id == 487791223831134219:
      env.update(globals())

      stdout = io.StringIO()

      to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

      try:
          exec(to_compile, env)
      except Exception as e:
          return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

      func = env['func']
      try:
         with redirect_stdout(stdout):
            ret = await func()
      except Exception as e:
          value = stdout.getvalue()
          await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
      else:
          value = stdout.getvalue()
          try:
              await message.add_reaction('\u2705')
          except:
              pass

          if ret is None:
              if value:
                  await ctx.send(f'```py\n{value}\n```')
          else:
              pass

@bot.event
async def on_message(message):
    if message.author.id == 487791223831134219 and message.content == "Ingenious!":
      await message.channel.send("true")
    if message.guild is not None:
        if not message.author.bot:
          await bot.process_commands(message)
    else:
        if not message.author.bot:
        #Create the Modmail Thread.
          thread = await CheckThread(message.author)
          if thread is None:
            THREAD = await CreateThread(message.author)
            await ReplyTo(THREAD,message)
          else:
            await ReplyTo(thread,message)




#Modmail code
class ModMailThread():
    def __init__(self,channel,user):
        self.channel = channel #The discord.Channel
        self.user = user #The discord.User


async def CheckThread(user):
     """Check if a user has an existing thread
       IF the user has an existing thread, returns the ModMailThread object. If not, returns None"""
     guild = discord.utils.get(bot.guilds,id=default_config.get("MainGuildID"))
     channel = discord.utils.get(guild.channels,name="mm-ticket-cache")
     data = ast.literal_eval(channel.topic)
     thread_chn = data.get(user.id,None)
     if thread_chn is None:
         #passed is either invalid, or no user

         for key,value in data.items():
           if value == user.id:
                 return ModMailThread(channel=user,user=bot.get_user(key))
         return None
     #Create the ModMailThread
     return ModMailThread(channel=bot.get_channel(thread_chn),user=user)



async def CreateThread(user):
    """Create a thread. yields a ModMailThread Object"""
    guild = discord.utils.get(bot.guilds,id=default_config.get("MainGuildID"))
    channel = discord.utils.get(guild.channels,name="mm-blacklist")
    blacklist = ast.literal_eval(channel.topic)
    if user.id in blacklist:
        await user.send("You are blacklisted from using modmail!")
        return
    catag = bot.get_channel(default_config.get("ModMailCatagoryID"))
    guild = bot.get_guild(default_config.get("StaffGuildID"))
    chn = await guild.create_text_channel(f"{user.name}-{user.discriminator}",category=catag)
    await chn.send(f"@here Modmail Thread with **{user.name}#{user.discriminator}** has been started.")
    await user.send("Thank you for the message. A staff member will reply to you as soon as possible.")    
    guild = discord.utils.get(bot.guilds,id=default_config.get("MainGuildID"))
    channel = discord.utils.get(guild.channels,name="mm-ticket-cache")
    data = ast.literal_eval(channel.topic)
    data[user.id] = chn.id
    await channel.edit(topic=str(data))
    logs = await get_all_logs(guild)
    log = 0
    for key,value in logs.items():
        if key.startswith(f"{str(user.id)}"):
            log += 1
    if not log == 0:
        await chn.send(f"User has {log} previous logs! Do `{default_config.get('BotPrefix')}logs {str(user.id)}` to view them!")
    return ModMailThread(channel=chn,user=user)

async def ReplyTo(thread2,message,mod=False):
    """Reply to a thread. thread should be a ModMailThread Object.
       Returns 200 if success, 404 if fail. 403 if DM Error.
       mod = True specifies that it is the Moderator Replying to the thread."""
    attach = []
    for attachm in message.attachments:
        attach.append(attachm.url)
    if not mod:
      await thread2.channel.send(f"**{thread2.user.name}#{thread2.user.discriminator}:** {message.content}")
      if not len(attach) == 0:
          #AttachmentFormatter
          attachment_msg = ""
          for attach2 in attach:
              attachment_msg = attachment_msg+f", {attach2}"
          if attachment_msg != "":
              attachment_msg = attachment_msg[1:]
          await thread2.channel.send(f"Attachments : {attachment_msg}")
      return 200
    else:
      await thread2.channel.send(f"**(Mod) {mod.name}#{mod.discriminator}**: {message.content}")
      if not len(attach) == 0:
          #AttachmentFormatter
          attachment_msg = ""
          for attach2 in attach:
              attachment_msg = attachment_msg+f", {attach2}"
          if attachment_msg != "":
              attachment_msg = attachment_msg[1:]
          await thread2.channel.send(f"Attachments : {attachment_msg}")
      try:
          await thread2.user.send(f"**{mod.name}#{mod.discriminator}**: {message.content}")
          if not len(attach) == 0:
            #AttachmentFormatter
            attachment_msg = ""
            for attach2 in attach:
              attachment_msg = attachment_msg+f", {attach2}"
            if attachment_msg != "":
              attachment_msg = attachment_msg[1:]
            await thread2.user.send(f"Attachments : {attachment_msg}")
            return 2001
          return 200
      except:
          await thread2.channel.send(f"Cannot DM the user!")
          return 403


@bot.command()
async def reply(ctx,*,message=None):
    if message is None:
        await ctx.send("No content to send!")
        return
    thread = await CheckThread(ctx.message.channel)
    if thread is None:
        await ctx.send("This is not a modmail thread!")
        return
    print(thread)  
    number = await ReplyTo(thread2=thread,message=FakeMessage(content=message,attachments=ctx.message.attachments),mod=ctx.author)
    if not number == 2001:
      await ctx.message.delete()

@bot.command()
async def r(ctx,*,message=None):
    if message is None:
        await ctx.send("No content to send!")
        return
    thread = await CheckThread(ctx.message.channel)
    if thread is None:
        await ctx.send("This is not a modmail thread!")
        return
    print(thread)  
    number = await ReplyTo(thread2=thread,message=FakeMessage(content=message,attachments=ctx.message.attachments),mod=ctx.author)
    if not number == 2001:
      await ctx.message.delete()


class FakeMessage():
    def __init__(self,content,attachments):
        self.content = content
        self.attachments = attachments #list

@bot.command()
async def close(ctx):
    thread = await CheckThread(ctx.channel)
    if thread is None:
        await ctx.send("This is not a modmail thread!")
        return
    print(thread)
    await ctx.send("Closing Thread...")
    #Generate thread logs
    await create_tlog(ctx.channel,thread.user,bot)
    guild = discord.utils.get(bot.guilds,id=default_config.get("MainGuildID"))
    channel = discord.utils.get(guild.channels,name="mm-ticket-cache")
    data = ast.literal_eval(channel.topic)
    data.pop(thread.user.id)
    await channel.edit(topic=str(data))
    await ctx.channel.delete()
    await thread.user.send(f"Your modmail thread has been closed by {ctx.message.author.name}#{ctx.message.author.discriminator}. Please reply to start a new therad.")


@bot.command()
@commands.has_permissions(manage_guild=True)
async def logs(ctx,user:discord.Member):
    logs = await get_all_logs(ctx.guild)
    log = False
    for key,value in logs.items():
        if key.startswith(f"{str(user.id)}"):
            await ctx.send(value)
            log = True
    if not log:
        await ctx.send("No logs found!")


    
async def get_all_logs(guild):
    returnob = {}
    channel = discord.utils.get(guild.channels,name="mm-logs")
    async for message in channel.history(limit=2000000):
        try:
          logfile = message.attachments[0]
          colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
          returnob[f"{logfile.filename}-{colour}"] = logfile.url
        except:
          pass
    return returnob
        

@bot.command()
@commands.has_permissions(manage_guild=True)
async def blacklist(ctx,user:discord.User):
    guild = discord.utils.get(bot.guilds,id=default_config.get("MainGuildID"))
    channel = discord.utils.get(guild.channels,name="mm-blacklist")
    current = ast.literal_eval(channel.topic)
    if not user.id in current:
      current.append(user.id)
    else:
      await ctx.send("Already blacklisted!")
      return
    await channel.edit(topic=str(current))
    await ctx.send("Done!")


@bot.command()
@commands.has_permissions(manage_guild=True)
async def unblacklist(ctx,user:discord.User):
    guild = discord.utils.get(bot.guilds,id=default_config.get("MainGuildID"))
    channel = discord.utils.get(guild.channels,name="mm-blacklist")
    current = ast.literal_eval(channel.topic)
    try:
        current.remove(user.id)
    except:
        await ctx.send("User is not blacklisted!")
        return
    await channel.edit(topic=str(current))
    await ctx.send("Done!")

    
bot.run(default_config.get("BotToken"),reconnect=default_config.get("BotAutoReconnect"))
