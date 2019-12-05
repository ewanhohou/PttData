import common.ptt_data as ptt
from PTTLibrary import PTT


class PttUserModel:

    def __init__(self, id, acc, pswd):
        self.id = id
        self.bot = PTT.Library()
        self.acc = acc
        self.pswd = pswd

    def get_user(self):
        try:
            ptt.login(self.bot, self.acc, self.pswd)
            user = ptt.get_user(self.bot, self.id)
            ptt.logout(self.bot)
        except PTT.Exceptions.NoSuchUser:
            return None
        return user

    def get_posts(self, crawlHandler, range=5):
        try:
            ptt.login(self.bot, self.acc, self.pswd)
            ptt.get_posts(self.bot, self.id, range, crawlHandler)
            ptt.logout(self.bot)
        except PTT.Exceptions.NoSuchUser:
            return None
