# Bumpr
A Discord SelfBot/UserBot which auto bumps the server every 2nd hour on Disboard. <br />
Suitable for hosting on repl.it since it is not time based. **__[USES SLASH COMMAND]__**

# Requirements:
-> A discord account to be used as selfbot/userbot. <br />
-> A bump reminder bot, there are many out there.

# How it works:
Since many would tend to host the selfbot/userbot on repl.it, no time module is used here because of the known fact that the repl goes down frequently for a while. <br />

Instead, the bot sends the slash command of bump whenever it is pinged in the chat. There are many bump reminder bots out there, which can be used for this purpose. <br />

The owner must ping the bot once for setting up the reminder, which automatically loops the bump for future.

# Setup:
Simply just fill out details needed in bot.py as **strings**. <br />

TOKEN = token of account to be used as selfbot/userbot <br />
ownerID = your user id <br />
reminder_botID = user id of the bot used to remind for bump <br />
prefix = user id of selfbot within angle brackets after @.

That's it, you're welcome.
