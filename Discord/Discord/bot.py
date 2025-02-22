import discord
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Now get the token
token = os.getenv('TOKEN')
print(f'Token: {token}')  # This will help debug if the token is loaded correctly

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now online')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        u_message = str(message.content)
        channel = str(message.channel)
        print(f'{username}: {u_message} in {channel}')
        await message.channel.send(u_message)

    client.run(token)

if __name__ == '__main__':
    run_discord_bot()


# import discord
# import os

# def run_discord_bot():
#     intents = discord.Intents.default()
#     intents.message_content = True
#     client = discord.Client(intents=intents)

#     @client.event
#     async def on_ready():  # Corrected from 'on_read' to 'on_ready'
#         print(f'{client.user} is now online')
    
#     @client.event
#     async def on_message(message):
#         if message.author == client.user:
#             return
        
#         username = str(message.author)
#         u_message = str(message.content)
#         channel = str(message.channel)
#         print(f'{username}: {u_message} in {channel}')
#         await message.channel.send(u_message)

#     client.run(os.getenv('TOKEN'))

# if __name__ == '__main__':
#     run_discord_bot()