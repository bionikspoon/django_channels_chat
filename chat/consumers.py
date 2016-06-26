# coding=utf-8
import json

from channels import Group, Channel
from channels.auth import channel_session_user_from_http, channel_session_user

from .models import ChatMessage


def chat_consumer(message):
    room = message.content['room']
    text = message.content['message']
    username = message.content['username']
    ChatMessage.objects.create(room=room, message=message)

    data = json.dumps({'message': text, 'username': username})

    group = Group('chat-%s' % room)
    group.send({'text': data})


@channel_session_user_from_http
def chat_connect(message):
    room = message.content['path'].strip('/')
    message.channel_session['room'] = room

    group = Group('chat-%s' % room)
    group.add(message.reply_channel)


@channel_session_user
def chat_message(message):
    room = message.channel_session['room']
    Channel('chat-messages').send({
        'room': room,
        'message': message['text'],
        'username': message.user.username,
    })


@channel_session_user
def chat_disconnect(message):
    room = message.channel_session['room']

    group = Group('chat-%s' % room)
    group.discard(message.reply_channel)

#
# @channel_session_user_from_http
# def chat_connect(message, room):
#     group = Group('chat-%s' % room)
#     group.add(message.reply_channel)
#     group.send({
#         'text': '[%s] connected' % message.user.username,
#     })
#
#
# @channel_session_user
# def chat_message(message, room):
#     Group('chat-%s' % room).send({
#         'text': '[%s] %s' % (message.user.username, message.content['text']),
#     })
#
#
# @channel_session_user
# def chat_disconnect(message, room):
#     group = Group('chat-%s' % room)
#     group.discard(message.reply_channel)
#     group.send({
#         'text': '[%s] disconnected' % message.user.username,
#     })
