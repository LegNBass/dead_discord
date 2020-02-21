import re
import discord


class LiveDead(discord.Client):
    _message_rules = (
        (lambda message: re.match(r'\d{4}-\d{2}-\d{2}', message.content), lambda match: f"The date is {match.group()}"),
    )

    def __init__(self, token):
        self.token = token
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
                await message.channel.send(response(result))

    def run(self):
        super().run(self.token)
