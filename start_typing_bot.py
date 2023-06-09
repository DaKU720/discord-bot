import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents) # "!" Your prefix.

@bot.event 
async def on_connect(): 
    print("conecting with your advanced bot ...")


@bot.event
async def on_ready():
    print("Bot is Ready!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Sandy Radio")) # Bot Activity, choose one activity and paste it. 
    print("")


@commands.has_role("bot_manager") # "bot_manager" Discord role to be in command.      
@bot.command() 
async def speak(ctx, *, text): # "speak" command name.
        message = ctx.message
        await message.delete()
        await ctx.send(f"{text}")


bot.run("") # paste your bot token inside.


### Different discord activities
# Playing status
# await bot.change_presence(activity=discord.Game(name="a game"))

# Streaming status
# await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Listening status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Watching status
# await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
