from discum.utils.slash import SlashCommander
import discum
import time
import random

ownerID = "" #OWNER ID
reminder_botID = "" #REMINDER BOT ID
selfbot_ID = "" #SELFBOT ID
TOKEN = "" #TOKEN


bot = discum.Client(token=TOKEN,log=False)

def bump(resp, prefix):
  if resp.event.message:
    m = resp.parsed.auto()
    if prefix in m['content']:
      if m['author']['id'] == ownerID or m['author']['id'] == reminder_botID:
        time.sleep(random.randint(4,15))
        guildID = m['guild_id']
        channelID = m['channel_id']
        slashCmds = bot.getSlashCommands("302050872383242240").json()
        s = SlashCommander(slashCmds)
        data = s.get(['bump'])
        bot.triggerSlashCommand("302050872383242240", channelID, guildID=guildID, data=data)
        print('Bumped!')
      else:
        channelID = m['channel_id']
        bot.sendMessage(channelID,message='Do not ping me unnecessarily.')

prefix = f"<@{selfbot_ID}>"
bot.gateway.command({"function": bump, "params": {"prefix": prefix}})
bot.gateway.run(auto_reconnect=True)
