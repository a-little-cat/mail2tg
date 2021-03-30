from telegram import bot
from imbox import Imbox
import threading
import datetime
import requests

server_list = ['imap.qq.com', "imap.mxhichina.com"]
username_list = ['123@qq.com', '123']
password_list = ['123', '123']

token = '123:123-123'
chatId = '123'


def check_mail():
    for server, username, password in zip(server_list, username_list, password_list):
        with Imbox(server,
                   username=username,
                   password=password,
                   ssl=True,
                   ssl_context=None,
                   starttls=False) as imbox:

            unread_inbox_messages = imbox.messages(unread=True)
            for uid, message in unread_inbox_messages:
                try:
                    note = "{} sent to {}\n{}\n{}".format(
                    message.sent_from[0]["name"], message.sent_to[0]["email"], message.subject, message.body["plain"][0][:50])
                except Exception:
                    note = "someone sent to email to you"
                url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(
                    token, chatId, note)
                requests.get(url)
                imbox.mark_seen(uid)


def create_timer():
    t = threading.Timer(60, create_timer)
    t.start()
    check_mail()


if __name__ == "__main__":
    create_timer()
