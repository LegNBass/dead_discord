import discord


class LiveDead(discord.Client):
    def __init__(self, token):
        self.token = token
        super().__init__()

    async def on_ready(self):
        print(f'{self.user} has connected to Discord')
        print(f"Connected to {self.guilds}")

    def run(self):
        super().run(self.token)
