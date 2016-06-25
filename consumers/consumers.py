# coding=utf-8
from channels import Group
from channels.auth import channel_session_user_from_http, channel_session_user
from channels.sessions import channel_session


@channel_session_user_from_http
def ws_connect(message):
    room = message.content['path'].strip('/')
    message.channel_session['room'] = room
    Group('chat-%s' % message.user.username[0]).add(message.reply_channel)


@channel_session_user
def ws_message(message):
    Group('chat-%s' % message.user.username[0]).send({
        'text': '[user] %s' % message.content['text'],
    })


@channel_session_user
def ws_disconnect(message):
    Group('chat-%s' % message.user.username[0]).discard(message.reply_channel)
