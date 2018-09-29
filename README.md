

# Discord Modmail
Version 1.0.0 
## Setup

1. Install python 3.6 to your local device. Please tick on add python to path when installing

2. Change the values in config.py 

3. Run ```run_launcher.bat``` and follow instructions!

## Setup (Heroku)

**DISCLAIMER : HEROKU IS A FREE HOSTING PLATFORM AND I MADE THE BOT SUPPORT HEROKU. HOWEVER, AS THE CODE FOR HEROKU IS DIFFERENT FROM THE STANDARD CODE (ye fuck storage on heroku), UPDATES THAT GO TO THE MAIN BOT MIGHT NOT BE ROLLED OUT INSTANTLY ON THE HEROKU VERSION.**

1. Fork this repository.

2. Get an account on heroku.com.

3. Press "Create a new app", select "Python app", give your app a name.

4. At deploy, select "Github" And link to your forked repo.

5. Press "Manual Deploy"

6. Go to the settings tab, press reveal config vars.

7. Enter ALL the config variables listed below and their respective value. The end result should be something like [this](https://cdn.discordapp.com/attachments/490011895663820811/494074082292137985/unknown.png)


|Config Var|Value|
|------|-------|
|MainGuildID|int:The Main Guilds's ID|
|StaffGuildID|int:The Staff Guild's ID. Can be the same as MainGuildID.|
|ModMailCatagoryID|int:The Modmail Catagory's ID|
|DiscordModmailLogChannel|int:The ID of the Modmail Logging Channel|
|**BotToken**|str:The Bot's Token|
|BotPlayingStatus|str:The Bot's Playing Status|
|BotPrefix|str:The Bot's Prefix|
|LogCommands|bool:True/False. Since you are hosting on heroku, this would not affect regardless of input, but it must be a boolean.|
|BotBoundToGuilds|bool:True/False. Weather the bot should be bounded to the Main and Staff Guilds.|
|BotDMOwnerOnRestart|bool:True/False. Wheater the bot should DM bot owner when restart.|
|BotAutoReconnect|bool:True/False Wheater the bot should auto-reconnect if it becomes disconnected.|
|**FROM_HEROKU**|True. THIS MUST BE TRUE.|

Reference : You can refer to this video which teaches you how to host a bot in heroku. However, please DO NOT FOLLOW STEP BY STEP because your target here is to get a feel on how to create a bot on heroku not follow what it teaches. 

Video : https://www.youtube.com/watch?v=6za78ipFzg4 (see from 2:13 minute mark)


8. Go to Workers, and start the worker.

9. The bot is up!

## Usage

### Commands

Do ```{prefix}help``` in the staff guild for help.


## Support

Open a ticket here, or email eltontay11@gmail.com . 

## Donate

Love the bot? Donate and help me out! https://patreon.com/eltontay11


# FAQ

Q: Which users get access to the channels for the modmail thread?

A: It depends on the permission settings of the Mod Mail Catagory.

--------------
Q: Which users can use the modmail commands?

A: Modmail commands can only be used in the modmail thread channels. Thus, whoever can see the channels can use the commands!
   
   However, for other administrative commands, Manage Server is required.
   
-----------------
Q: When FROM_HEROKU is specified, it creates three channels. Can I delete them?

A: NO. The bot stores data on the channels. As such, those channels cannot be deleted, renamed or modified in any way.

# TODO

- View whole blacklist

- Show edited messages from user

- Custom Start/Close Thread messages

- Ratings , rate <uuid>

- Reverse typing proxy

- Anonymous reply

- Use user's top role instead of (Mod)

- From_HEROKU if one or more data channels deleted, automatically recreate them. 
