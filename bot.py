import discord
import requests
from bs4 import BeautifulSoup

try:
    import settings
except ImportError:
    import settings_default as settings
    exit("Rename settings_default to settings and set the TOKEN")


class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.__response = requests.get(settings.URL_SITE_TO_PARSE_FILMS+"/filmy.html")
        self.__soup = BeautifulSoup(self.__response.text, "lxml")

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('hello'):
            await message.channel.send('Hello!')

        if "films" in message.content:
            films = self.__soup.find_all("div", class_="movie")
            for film in films:
                info = film.find("div", class_="info")
                title = info.find("div", class_="title").text
                await message.channel.send(title)
