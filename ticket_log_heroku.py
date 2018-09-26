import discord
import os
from discord.ext import commands
from config import *
import asyncio

async def ticketlog(channel,user,bot):
    #Channel must be a discord.TextChannel
    #User must be a discord.User of the theead
    """Create the logs"""
    LOGS = []
    async for message in channel.history(limit=10000000):
        if message.author == bot.user:
            time = f"{message.created_at.year}-{message.created_at.month}-{message.created_at.day} {message.created_at.hour}:{message.created_at.minute}:{message.created_at.second} UTC"
            ### Have to do time to get message time
            LOGS.append(f"\n[{time}] {message.content}")
        else:
            ### Have to do the get message time
            time = f"{message.created_at.year}-{message.created_at.month}-{message.created_at.day} {message.created_at.hour}:{message.created_at.minute}:{message.created_at.second} UTC"

            LOGS.append(f"\n[{time}] {message.author.name}#{message.author.discriminator} : {message.content}")


     ### Add topic of thread
     ###SAME HAVE TO DO TIME time is channel creation date
    LOGS.append(f"THREADS FOR {user.name}#{user.discriminator} ({str(user.id)}) on {channel.created_at} UTC")
    LOGS = LOGS[::-1]
    #Determine the filename to save logs as
    log_no = "LOG"
    file = open(f"{str(user.id)}-{str(log_no)}.txt","w")
    for item in LOGS:
        try:
          file.write(item)
        except:
            pass
    file.close()
    channel = bot.get_channel(int(os.environ.get("DiscordModmailLogChannel")))
    file = open(f"{str(user.id)}-{str(log_no)}.txt","rb")
    await channel.send(content=f"New Thread with {user.name}#{user.discriminator} closed.",file=discord.File(fp=file))
    chn2 = discord.utils.get(bot.guilds,id=int(os.environ.get("StaffGuildID")))
    chn3 = discord.utils.get(chn2.channels,name="mm-logs")
    file = open(f"{str(user.id)}-{str(log_no)}.txt","rb")
    await chn3.send(file=discord.File(fp=file))
    file.close()
    
