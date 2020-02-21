import requests
import discord


class RelistenAPI:
    base_url = "https://api.relisten.net"
    api_prefix = "api/v2"
    headers = {
        "accept": "application/json"
    }

    def __init__(self, artist='grateful-dead'):
        self.artist = artist

    @property
    def artists(self):
        return requests.get(
            f"{self.base_url}/{self.api_prefix}/artists",
            headers=self.headers
        ).json()

    def show(self, show_date):
        response = requests.get(
            f"{self.base_url}/{self.api_prefix}/artists/{self.artist}/shows/{show_date}",
            headers=self.headers
        )
        if response.status_code == 200:
            try:
                source = next(iter(
                    response.json().get("sources", [])
                ))
                return 200, source
            except StopIteration:
                return []
        else:
            return response.status_code, response.json()

    def format_show(self, date):
        code, sources = self.show(date)
        if code == 200:
            url = sources['links'][0]['url']
            description = sources['description']

            tracks = [
                track for _set in sources['sets'] for track in _set['tracks']
            ]
            # print(tracks)
            embed = discord.Embed(
                title=date,
                description=description,
                url=url
            )
            for ix, track in enumerate(tracks, 1):
                embed.add_field(
                    name=ix,
                    value=f"[{track['title']}]({track['mp3_url'].replace('mp3', 'shn').replace('download', 'details')})",
                    inline=False
                )
            return embed


if __name__ == "__main__":
    # Shell entrypoint for testing
    import sys
    import json
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'show',
        help="The date of the show in YYYY-MM-DD format"
    )
    args = parser.parse_args()

    api = RelistenAPI()
    try:
        sys.stdout.write(
            json.dumps(api.show(args.show)[1])
        )
    except IOError:
        pass
