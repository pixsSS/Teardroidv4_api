from deta import Deta
from os import getenv

deta = Deta(getenv("a0DMX4stpyDW_N1mcUWepmmcYQn73L2QbRA7r1AXqFHJN"))


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
