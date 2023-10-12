import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    category_id = 1141399881769029653  # Replace with your category ID
    category = bot.get_channel(category_id)

    if category is None:
        print("Invalid category ID.")
        return

    if isinstance(category, discord.CategoryChannel):
        for channel in category.channels:
            try:
                await channel.delete()
            except discord.Forbidden:
                print(f"Cannot delete channel {channel.name} due to permissions.")
        print(f"All channels in the category {category.name} have been deleted.")
    else:
        print("The provided ID is not a valid category.")

bot.run('MTE0MTM5NDMyMDExNzcyNzI0NA.GbCQM7.NOmw0y2RCwG3gIZ8o0qR0XOk3KWYm4_xmTf_qk')
