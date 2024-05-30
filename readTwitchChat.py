import os
from dotenv import load_dotenv
from twitchio import Client

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variables
token = os.getenv('TOKEN')

class Bot(Client):

    def __init__(self):
        super().__init__(token=token, initial_channels=['itsRyanHiga'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Ignore messages from StreamElements
        if message.author.name.lower() == 'streamelements':
            return
        
        # Check if the message contains a question mark
        if '?' in message.content:
            with open("questions.txt", "a") as file:
                file.write(f'{message.author.name}: {message.content}\n')
        
        # Print the name of the chatter and their message
        print(f'{message.author.name}: {message.content}')

bot = Bot()
bot.run()
