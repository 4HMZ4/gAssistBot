import csv
import random
import discord

from discord.ext import commands
from lib.csvReader import csvReader
from lib.getToken import getToken as token


## Setup intents for the server
intents = discord.Intents.default()
intents.members = True


## Initialize the bot command and assign prefix aswel as intents 
bot = commands.Bot(command_prefix='g.', intents=intents)


########################################################
#### Boring Bot Init
########################################################


## checks if server is up
@bot.event
async def on_ready():
    print('Script successfully logged in')


## Checks to see if a member has joined the guild
@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server')


## Checks to see if a member has left the guild
@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')


########################################################
#### Fun Stuff
########################################################


@bot.command()
async def ping(ctx):
    await ctx.send(f":ping_pong: Pong! {round(bot.latency * 1000)}ms")

@bot.command(aliases=['🎱', '8ball'])
async def _8ball(ctx, *, question=""):
    if question == "":
        await ctx.send("You need to ask 8ball a question.")
    else:
        await ctx.send(f'Question: {question}\nAnswer:   {random.choice(csvReader("./data/lists/eightBall-responses.csv"))}')


########################################################
#### Moderator Stuff
########################################################


## Clear the chat
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    if amount == 0:
        await ctx.send("dont be silly")
    else:
        await ctx.channel.purge(limit=amount+1)


## Kick Users
@bot.command()
@commands.has_role('moderator')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Banned {member.mention}. Reason: {reason}")


## Ban Users
@bot.command()
@commands.has_role('moderator')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}. Reason: {reason}")


## Unban Users
@bot.command()
@commands.has_role('moderator')
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    memberName, memberdiscriminator = member.split('#')

    for banEntry in bannedUsers:
        user = banEntry.user

        if (user.name, user.discriminator) == (memberName, memberdiscriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return


########################################################
#### Cogs
########################################################

# Need to work on cogs
 

bot.run(token())



