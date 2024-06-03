import os
from dotenv import load_dotenv
from twitchio import Client
import time
from collections import deque

# the old items are only removed when a new message triggers and event_message

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variables
token = os.getenv('TOKEN')

queue = deque(maxlen=100) # Max of 100 items in the queue

class Bot(Client):

    def __init__(self):
        super().__init__(token=token, initial_channels=['hJune'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        # Ignore messages from StreamElements
        if message.author.name.lower() == 'streamelements':
            return
        
        # # Check if the message contains a question mark
        if '?' in message.content:
            with open("questions.txt", "a") as file:
                file.write(f'{message.author.name}: {message.content}\n')
        
        # Print the name of the chatter and their message
        print(f'{message.author.name}: {message.content}')
        
        current_time = time.time()
        queue.append((message.author.name, message.content , current_time))
        
        # Remove old entries from the queue
        while queue and current_time - queue[0][2] > 1 * 60:
            queue.popleft()
        
        with open("chat.txt", "w") as file:
            for entry in queue:
                file.write(f'{entry[0]}: {entry[1]}\n')

bot = Bot()
bot.run()
