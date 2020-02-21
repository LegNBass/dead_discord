import os

from dotenv import load_dotenv
from bot import LiveDead


def main():
    load_dotenv()

    token = os.getenv('DISCORD_TOKEN')

    ld = LiveDead(token)
    ld.run()


if __name__ == '__main__':
    main()
