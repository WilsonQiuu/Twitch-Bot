from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='oauth:bw968c11xhk2cfbzg4j1by2r9g9q23', prefix='!', initial_channels=['hJune'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.author.name.lower() == 'streamelements':
            return
        # Print the name of the chatter and their message
        print(f'{message.author.name}: {message.content}')
        await self.handle_commands(message)

bot = Bot()
bot.run()
