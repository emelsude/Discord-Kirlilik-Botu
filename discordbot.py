import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def welcome(ctx):
    await ctx.send("Welcome to our server! Remember to be kind and supportive!")

@bot.command()
async def survey(ctx, *, question):
    await ctx.send(f"Survey: {question}")
    await ctx.send("Please respond with your answer.")

    # Collect responses in a channel
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        response = await bot.wait_for('message', check=check, timeout=30)
        await ctx.send(f"Thank you for your response: {response.content}")
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond!")

@bot.command()
async def kind_reminder(ctx):
    await ctx.send("Remember to treat everyone with kindness! 💖")

@bot.command()
async def report(ctx, user: discord.Member, *, reason):
    # Logic to report user (for now just a placeholder message)
    await ctx.send(f"Reported {user.mention} for: {reason}. Thank you for helping keep the community safe!")

@report.error
async def report_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Please mention a valid user to report.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please provide a reason for the report.")

bot.run('YOUR_BOT_TOKEN')
