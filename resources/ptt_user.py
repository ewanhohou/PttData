from models.ptt_user import PttUserModel
import os
import setting


class PttUser():
    def __init__(self, id):
        self.id = id
        self.acc = os.getenv("ptt_acc")
        self.pswd = os.getenv("ptt_pswd")

    def get(self):
        user = PttUserModel(self.id, self.acc, self.pswd).get_user()
        if not user:
            return {
                'errcode': 1,
                'message': 'username not exist!'
            }
        return {
            'errcode': 0,
            'message':
            {
                'id': user.getID(),
                'money': str(user.getMoney()),
                'loginTime':  str(user.getLoginTime()),
                'legalPost': str(user.getLegalPost()),
                'illegalPost': str(user.getIllegalPost()),
                'state': user.getState(),
                'mail': user.getMail(),
                'lastLogin': user.getLastLogin(),
                'lastIP': user.getLastIP(),
                'fiveChess': user.getFiveChess(),
                'chess': user.getChess(),
                'signatureFile': user.getSignatureFile(),
            }}

    def get_posts(self, crawlHandler):
        PttUserModel(
            self.id, self.acc, self.pswd).get_posts(crawlHandler)
