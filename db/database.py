from deta import Deta
from os import getenv

deta = Deta(getenv("678785ffhfhfjh"))


def client_db():
    return deta.Base("xxx")


def notification_db():
    return deta.Base("notification")


def command_db():
    return deta.Base("command")


def auth_db():
    return deta.Base("auth")


async def tear_drive():
    return deta.Drive("teardroid")
