import discord
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = "NjI5MTU1OTg3NDIwMzQ4NDE2.XaGwhQ.zicmivcccJwafNV7cB6p2TSCO8o"
BOT_PREFIX = ("&")
bot = commands.Bot(command_prefix=BOT_PREFIX, description='Hi')

@bot.command(pass_context=True)
async def userping(ctx):
    for members in bot.get_all_members():
        try:

                  await members.send("Ok Recommend for you to join this group: https://discord.gg/GnP4PDA")
        except:
        	print("Error_00x58880: Close This! Bot spammed")


bot.run('NjI5MTU1OTg3NDIwMzQ4NDE2.XaGwhQ.zicmivcccJwafNV7cB6p2TSCO8o')
