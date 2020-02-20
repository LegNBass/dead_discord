import os
import discord

from types import MethodType
from dotenv import load_dotenv

load_dotenv()


class LiveDead:
    def __init__(self):
        self.client = discord.Client()
        self.token = os.getenv('DISCORD_TOKEN')

        async def on_ready(self):
            print(f'{self.client.user} has connected to Discord')

        self.on_ready = self.client.event(MethodType(
            on_ready, self
        ))

    def run(self):
        self.client.run(self.token)
