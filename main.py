import logging

try:
    import settings
except ImportError:
    import settings_default as settings
    exit("Rename settings_default to settings and set the TOKEN")
from bot import Bot


def configure_logging():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


if __name__ == '__main__':
    configure_logging()
    client = Bot()
    client.run(settings.TOKEN)
