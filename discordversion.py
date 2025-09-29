import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

@bot.command()
async def rps(ctx, user_choice: str):
    choices = ['rock', 'paper', 'scissors']
    user_choice = user_choice.lower()
    
    if user_choice not in choices:
        await ctx.send("Invalid choice! Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    await ctx.send(f"You chose: {user_choice}\n"
                   f"Computer chose: {computer_choice}\n"
                   f"{result}")

# Replace 'YOUR_TOKEN_HERE' with your bot token
bot.run('YOUR_TOKEN_HERE')
