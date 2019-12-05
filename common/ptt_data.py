# -*- coding: utf-8 -*
import sys
from PTTLibrary import PTT


def login(pttBot, id, password):
    try:
        pttBot.login(
            id,
            password,
            KickOtherLogin=False)
    except PTT.Exceptions.LoginError:
        pttBot.log('登入失敗')
        sys.exit()
    except PTT.Exceptions.WrongIDorPassword:
        pttBot.log('帳號密碼錯誤')
        sys.exit()
    except PTT.Exceptions.LoginTooOften:
        pttBot.log('請稍等一下再登入')
        sys.exit()
    pttBot.log('登入成功')


def logout(pttBot):
    pttBot.logout()


def get_user(pttBot, id):
    user = pttBot.getUser(id)
    # pttBot.log('使用者ID: ' + user.getID())
    # pttBot.log('使用者經濟狀況: ' + str(user.getMoney()))
    # pttBot.log('登入次數: ' + str(user.getLoginTime()))
    # pttBot.log('有效文章數: ' + str(user.getLegalPost()))
    # pttBot.log('退文文章數: ' + str(user.getIllegalPost()))
    # pttBot.log('目前動態: ' + user.getState())
    # pttBot.log('信箱狀態: ' + user.getMail())
    # pttBot.log('最後登入時間: ' + user.getLastLogin())
    # pttBot.log('上次故鄉: ' + user.getLastIP())
    # pttBot.log('五子棋戰績: ' + user.getFiveChess())
    # pttBot.log('象棋戰績:' + user.getChess())
    # pttBot.log('簽名檔:' + user.getSignatureFile())
    return user


def show_condition(Board, SearchType, Condition):
    if SearchType == PTT.PostSearchType.Keyword:
        Type = '關鍵字'
    if SearchType == PTT.PostSearchType.Author:
        Type = '作者'
    if SearchType == PTT.PostSearchType.Push:
        Type = '推文數'
    if SearchType == PTT.PostSearchType.Mark:
        Type = '標記'
    if SearchType == PTT.PostSearchType.Money:
        Type = '稿酬'

    print(f'{Board} 使用 {Type} 搜尋 {Condition}')


def get_posts(pttBot, id, size, crawlHandler):
    postList = [
        ('ALLPOST', PTT.PostSearchType.Author, id),
        # ('Gossiping', PTT.PostSearchType.Keyword, '[公告]'),
        # ('Gossiping', PTT.PostSearchType.Author, 'ReDmango'),
        # ('Gossiping', PTT.PostSearchType.Push, '10'),
        # ('Gossiping', PTT.PostSearchType.Mark, 'm'),
        # ('Gossiping', PTT.PostSearchType.Money, '5'),
        # ('Gossiping', PTT.PostSearchType.Push, '-100'),
        # ('Gossiping', PTT.PostSearchType.Push, '150'),
    ]

    for (Board, SearchType, Condition) in postList:
        show_condition(Board, SearchType, Condition)
        NewestIndex = pttBot.getNewestIndex(
            PTT.IndexType.BBS,
            Board,
            SearchType=SearchType,
            SearchCondition=Condition,
        )
        if(NewestIndex > 1000):
            continue
        if(NewestIndex < size):
            StartIndex = 1
        else:
            StartIndex = NewestIndex - size + 1
        print(f'{Board} StartIndex {StartIndex}')
        print(f'{Board} 最新文章編號 {NewestIndex}')
        ErrorPostList, DelPostList = pttBot.crawlBoard(
            crawlHandler,
            PTT.CrawlType.BBS,
            Board,
            StartIndex=StartIndex,
            EndIndex=NewestIndex,
            SearchType=SearchType,
            SearchCondition=Condition,
            Query=True,  # Optional
        )


def createPost(post):
    if post.getDeleteStatus() != PTT.PostDeleteStatus.NotDeleted:
        if post.getDeleteStatus() == PTT.PostDeleteStatus.ByModerator:
            print(f'[板主刪除][{post.getAuthor()}]')
        elif post.getDeleteStatus() == PTT.PostDeleteStatus.ByAuthor:
            print(f'[作者刪除][{post.getAuthor()}]')
        elif post.getDeleteStatus() == PTT.PostDeleteStatus.ByUnknow:
            print(f'[不明刪除]')
        return {}
    return {
        'aid': post.getAID(),
        'title': post.getTitle(),
        'author': post.getAuthor(),
        'url': post.getWebUrl(),
        'date': post.getDate(),
        'money': str(post.getMoney()),
        'ip': post.getIP(),
        'date': post.getDate(),
        'board': post.getBoard(),
        'list_date': post.getListDate(),
        'location': post.getLocation(),
        'push': post.getPushNumber(),
    }
