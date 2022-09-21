import asyncio

class BotTasks:
    def __init__(self, bot, u_id):
        self.bot = bot
        self.u_id = u_id

    async def add_task(self, text, freq): # everyday 9:00 take pills
        text = 
        self.freq = 
        self.task = lambda _ : self.bot.send_message(self.u_id, text)

