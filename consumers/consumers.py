# coding=utf-8
from channels import Group


def ws_message(message):
    Group('chat').send({
        'text': '[user] %s' % message.content['text'],
    })


def ws_add(message):
    Group('chat').add(message.reply_channel)


def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)
