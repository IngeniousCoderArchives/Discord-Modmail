# This is the configuration file for IngeniousCoder’s Modmail.
# Only Edit things if you know what you are doing. If not, do not change the default Value.
# ALL VARIABLES ARE REQUIRED UNLESS SPECIFIED.
# Entering a wrong value may crash the program.
# CONFIG START

# MainGuildID : The main Guild’s ID For mod mail to be used in.
# StaffGuildID : The staff Guild’s ID For mod mail to be used in. This will be the server where all Modmail Threading and Logging will occur.
# ModMailCatagoryID : The Catagory ID of the Catagory Modmail shohld use.

MainGuildID = 00000000000
StaffGuildID = 00000000000
ModMainCatagoryID = 00000000000

# ModMail Main Configuration

# PossibleTopicOptions : List of possible topics of the thread.

# Tier1SupportDiscordRoleID : The Discord Role ID of the Tier 1 Support Role. Users with this role will be labelled Tier 1 Support

# Tier2SupportDiscordRoleID : The Discord Role ID of the Tier 2 Support Role. Users with this role will be labelled Tier 2 Support

# Tier3SupportDiscordRoleID : The Discord Role ID of the Tier 3 Support Role. Users with this role will be labelled Tier 3 Support

# ModMailCannotReplyIfNoTier : If set to True, users with no support tier rank cannot reply to modmail. If False. the optional Value, ModmailNoTierLabel, will be set to the label if somebody with no tier rank replies.

ModMailCannotReplyIfNoTier = True
#ModmailNoTierLabel = "Unranked"

# Users will be labelled based on their topmost role.

PossibleTopicOptions = ["Staff","Bot"]
Tier1SupportDiscordRoleID = 00000
Tier2SupportDiscordRoleID = 00000
Tier3SupportDiscordRoleID = 00000

# BotOwnerID : The bot owner’s ID. Bot owner may use Administrative Commands.

BotOwnerID = 0000000000

# DiscordRoleRequiredToCloseThreads : The RoleID of the role required to close threads. Leave Blank to default to Tier 1 Support

DiscordRoleRequiredToCloseThreads = 000000000

#End of config.

