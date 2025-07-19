import discord
from discord.ext import commands
import dotenv

from api import fetchEmergencyById
from functions import convertToDiscordTimestamp

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='emerg', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')

@bot.tree.command(name='ping', description='Check the bot\'s latency')
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.response.send_message(f'Pong! Latency: {latency:.2f} ms')
    
@bot.tree.command(name='find', description='find an emergency by ID')
async def find(ctx, emergency_id: int): 
    emergency = fetchEmergencyById(emergency_id)
    if emergency != None:
        emergencyinfo = emergency[0]
        location = emergency[1]['coordinates']
        embed = discord.Embed(title=emergencyinfo['category1'], description=f"{emergencyinfo['category2']}\nStarted {convertToDiscordTimestamp(emergencyinfo['created'])}")
        embed.add_field(name='Location', value=f'[{emergencyinfo['location']}](https://www.google.com/maps/search/?api=1&query={location[1]}%2c{location[0]})', inline=False)
        await ctx.response.send_message(embed=embed)
    else:
        print(emergency)
        await ctx.response.send_message(f'No emergency found with ID: {emergency_id}', ephemeral=True)
        
    
@bot.tree.command()
async def sync(ctx):
    if ctx.user.id == 780303451980038165:
        synced = await bot.tree.sync()

        await ctx.response.send_message(
            f"Synced {len(synced)} commands."
        )
        return
    else:
        await ctx.response.send_message("You do not have permission to sync commands.", ephemeral=True)
    
    
DISCORD_TOKEN = dotenv.get_key('.env', 'DISCORD_TOKEN')
if not DISCORD_TOKEN:
    raise ValueError("Please set the DISCORD_TOKEN environment variable")
bot.run(DISCORD_TOKEN)