import discord
import random
import string
import asyncio

intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot
client = discord.Client(intents=intents)

# Define the role name that has permission to use the command
allowed_role_name = "Owner"  # Change this to the actual role name

@client.event
async def on_ready():
    print(f'Good to go as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.invite'):
        # Check if the user has the allowed role
        allowed_role = discord.utils.get(message.guild.roles, name=allowed_role_name)
        if allowed_role is None:
            await message.channel.send("The allowed role was not found.")
            return

        if allowed_role in message.author.roles:
            # Generate a random string of letters and numbers with length 45
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=45))

            # Mention the user who executed the command and make the random string a spoiler
            response = f'{message.author.mention}, here is your invite code: ||{random_string}||\n\n**Credits: Mario <3**'

            # Send the response to the same text channel where the command was executed
            response_message = await message.channel.send(response)

            # Wait for 15 seconds
            await asyncio.sleep(15)

            # Delete both the bot's response and the user's message
            await message.delete()
            await response_message.delete()
        else:
            # Execute silently if the user does not have the role
            pass

# Run the bot with your token
bot_token = 'MTE1Mjg3MTAxNjE3MTgzNTQ3Mg.GvzYxD.yiVwTqNdv_qS1KiVg1VEGHdtA-CZ8QVn88RPv8'
client.run(bot_token)