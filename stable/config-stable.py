# This is the configuration file for IngeniousCoder’s Modmail.
# Only Edit things if you know what you are doing. If not, do not change the default Value.
# ALL VARIABLES ARE REQUIRED UNLESS SPECIFIED.
# Entering a wrong value may crash the launcher and / or bot.
# CONFIG START

# MainGuildID : The main Guild’s ID For mod mail to be used in.
# StaffGuildID : The staff Guild’s ID For mod mail to be used in. This will be the server where all Modmail Threading and Logging will occur.
# ModMailCatagoryID : The Catagory ID of the Catagory Modmail shohld use.

MainGuildID = 00000000000
StaffGuildID = 00000000000
ModMailCatagoryID = 00000000000

# ModMail Main Configuration

# PossibleTopicOptions : List of possible topics of the thread.

# Tier1SupportDiscordRoleID : The Discord Role ID of the Tier 1 Support Role. Users with this role will be labelled Tier 1 Support

# Tier2SupportDiscordRoleID : The Discord Role ID of the Tier 2 Support Role. Users with this role will be labelled Tier 2 Support

# Tier3SupportDiscordRoleID : The Discord Role ID of the Tier 3 Support Role. Users with this role will be labelled Tier 3 Support

# ModMailCannotReplyIfNoTier : If set to True, users with no support tier rank cannot reply to modmail. If False. the optional Value, ModmailNoTierLabel, will be set to the label if somebody with no tier rank replies. Remember to uncomment it if you are using it.

ModMailCannotReplyIfNoTier = True
#ModmailNoTierLabel = "Unranked"

# Users will be labelled based on their topmost role.

PossibleTopicOptions = ["Staff","Bot"]
Tier1SupportDiscordRoleID = 00000
Tier2SupportDiscordRoleID = 00000
Tier3SupportDiscordRoleID = 00000

# DiscordRoleRequiredToCloseThreads : The RoleID of the role required to close threads. Leave as None to default to Tier 1 Support

DiscordRoleRequiredToCloseThreads = None

# DiscordModmailLogChannel : The channel where the bot should send log to. Put 0 to disable, Put 1 to make the bot automatically create one.

DiscordModmailLogChannel = 0

# BotToken : The bot token for the Oauth2 App.
# BotPlayingStatus : The bot playing status as shown in discord.
BotToken = "ABCDEFG"

# The 4 options below take booleans (True / False).
# LogCommands : Set if the bot should log into the logs folder.
# BotBoundToGuilds : Set if the bot should be bound to the Main and Staff Guilds. (Should the bot auto-leave other guilds when it is added to them?)
# BotDMOwnerOnRestart : Set if the bot should DM the Oauth2 Owner everytime on Restart.
# BotAutoReconnect : Set if the bot should Automatically Reconnect when disconnected.

LogCommands = True
BotBoundToGuiids = True
BotDMOwnerOnRestart = False
BotAutoReconnect = True

#End of config.

