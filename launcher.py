# Launcher

"""
The MIT License (MIT)
Copyright (c) 2015-2016 IngeniousCoder
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import time
import os
import sys
import platform
import shutil
from time import strftime
from time import localtime
try:
    import pip
except:
    pip = None
try:
    from config import *  #From local dir
except:
    print("Config cannot be loaded!")
    input("Press any key to exit.")
    exit()

LAUNCHER_MENU = """

--------------------------------
| INGENIOUSCODER's MODMAIL BOT |
--------------------------------
Select an option:
1. View Configuration
2. Start Bot
3. Reset Configuration
4. Reset Bot (and Data)
5. Setup (Use if bot cannot run when Starting)

For support, please submit a issue in Github."""

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
IS_64BIT = platform.machine().endswith("64")
PYTHON_OK = sys.version_info >= (3, 5)

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def wait():
    input("Press enter to continue.")
    
print("Setting Up...")
if not PYTHON_OK:
    print("Your python is outdated. Please update your python version.")
    wait()

def log(text,type1="INFO"):
  timenow = strftime("%Y-%m-%d %H:%M:%S", localtime())
  logtext = f"{timenow} [{type1}] {text}"
  print(logtext)
  

log("Logging is now set up.")

def config():
    #View Configuration
    log("Notice. If Python Throws an error, it means the config is corrupted and cannot be loaded.","NOTICE")
    
    log("Loading Config...")
    time.sleep(2)
    #Load Config
    if ModMailCannotReplyIfNoTier:
        NoTier = "True"
        NoTierLabel = "Not Set due to above value."
    else:
        NoTier = "False"
        try:
          NoTierLabel  = ModmailNoTierLabel
        except:
          log("Config Variable ModmailNoTierLabel was not set!","WARN")
          wait()
          exit()
    topics = ""
    for item in PossibleTopicOptions:
        topics = topics + f"{item},"
    if topics == "":
        topics = "None"
    else:
      topics = topics[:-1]
    if DiscordRoleRequiredToCloseThreads == None:
        rolethread = "Not Set"
    else:
        rolethread = str(DiscordRoleRequiredToCloseThreads)
    if DiscordModmailLogChannel == 0:
        logid = "Disabled."
    else:
        logid = str(DiscordModmailLogChannel)
    #logs, bound, dmrestart, AutoReconnect : The boolean formatters
    if LogCommands:
        logs = "True"
    else:
        logs = "False"
    if BotBoundToGuilds:
        bound = "True"
    else:
        bound = "False"
    if BotDMOwnerOnRestart:
        dmrestart = "True"
    else:
        dmrestart = "False"
    if BotAutoReconnect:
        disconnect = "True"
    else:
        disconnect = "False"
    #Set up config screen
    config_screen = [f"--------------------------------\n",
                     f"|     CUSTOM CONFIG VALUES     |\n",
                     f"--------------------------------\n",
                     f"Main Guild ID                           : {str(MainGuildID)}\n",
                     f"Staff Guild ID                          : {str(StaffGuildID)}\n",
                     f"Mod Mail Catagory ID                    : {str(ModMailCatagoryID)}\n",
                     f"No Tier Users Can Reply?                : {NoTier}\n",
                     f"No Tier Label                           : {NoTierLabel}\n",
                     f"Topic List                              : {topics}\n",
                     f"Tier 1 Support Role ID                  : {str(Tier1SupportDiscordRoleID)}\n",
                     f"Tier 2 Support Role ID                  : {str(Tier2SupportDiscordRoleID)}\n",
                     f"Tier 3 Support Role ID                  : {str(Tier3SupportDiscordRoleID)}\n",
                     f"Role Required to close threads          : {rolethread}\n",
                     f"Discord Modmail Logging Channel ID      : {logid}\n",
                     f"Logging output to logs?                 : {logs}\n",
                     f"Bot Bound to Home Guild(s) ?            : {bound}\n",
                     f"Bot DMs Owner when restarted?           : {dmrestart}\n",
                     f"Bot Auto Reconnects after Disconnected? : {disconnect}\n"]
    clear_screen()
    for item in config_screen:
        print(item)
    wait()
    home()
    
#WHEN VIEWING CONFIG, WARN IF CONFIG IS NOT EDITED YET (config.py is same as stable-config.py)

def home():
    clear_screen()
    print(LAUNCHER_MENU)
    while True:
        """ OPTIONS
            1. View Configuration
            2. Start Bot
            3. Reset Configuration
            4. Reset Bot (and Data)
            5. Setup (Use if bot cannot run when Starting)"""
        try:
            u_i = int(input("Please enter the option number > "))
        except:
            print("Invalid Input. Try again.")
            pass
        if u_i == 1:
            config()
        elif u_i == 2:
            start()
        elif u_i == 3:
            reset_config()
        elif u_i == 4:
            reset_bot()
        elif u_i == 5:
            setup()
        else:
            print("Input not recognised.")




def start():
    #Start bot
    return

def reset_config():
    #Reset config
    return

def reset_bot():
    #Reset bot
    return

def setup():
    #Setup and install requirements
    return



home()

