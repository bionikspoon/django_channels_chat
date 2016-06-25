# coding=utf-8
from channels import Group
from channels.auth import channel_session_user_from_http, channel_session_user


@channel_session_user_from_http
def chat_connect(message, room):
    group = Group('chat-%s' % room)
    group.add(message.reply_channel)
    group.send({
        'text': '[%s] connected' % message.user.username,
    })


@channel_session_user
def chat_message(message, room):
    Group('chat-%s' % room).send({
        'text': '[%s] %s' % (message.user.username, message.content['text']),
    })


@channel_session_user
def chat_disconnect(message, room):
    group = Group('chat-%s' % room)
    group.discard(message.reply_channel)
    group.send({
        'text': '[%s] disconnected' % message.user.username,
    })
