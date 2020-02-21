import re
import discord

from utils.relisten import RelistenAPI


class LiveDead(discord.Client):
    _message_rules = (
        (lambda message: re.match(r'\d{4}-\d{2}-\d{2}', message.content.strip()), lambda self, match: self.relisten_api.format_show(match.group())),
    )

    def __init__(self, token):
        self.token = token
        self.relisten_api = RelistenAPI()
        super().__init__()

    async def on_ready(self):
        print(f'{self.user} has connected to Discord')
        print(f"Connected to {self.guilds}")

    # Meat 'n taters
    async def on_message(self, message):
        if message.author == self.user:
            return  # Never reply to myself
        for rule, response in self._message_rules:
            if result := rule(message):
                try:
                    await message.channel.send(
                        embed=response(
                            self, result
                        )
                    )
                except Exception:
                    await message.channel.send(
                        "No Show found for that date."
                    )
                break

    def run(self):
        super().run(self.token)
