from os import getenv

class Config(object):
      API_HASH = "9dd6f3f8110ed095116029288f331eeb"
      API_ID = 13591765
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = "5599515627:AAEFqC05zXS1Qw2f04wJ0A7w2GmdDgKh7VQ"
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))
