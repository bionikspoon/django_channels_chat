# coding=utf-8
from channels import Group, Channel
from channels.auth import channel_session_user_from_http, channel_session_user
from channels.sessions import channel_session

from .models import ChatMessage


def msg_consumer(message):
    room = message.content['room']
    print('msg_consumer', 'room', room)

    message = message.content['message']
    ChatMessage.objects.create(room=room, message=message)

    group = Group('chat-%s' % room)
    group.send({'text': message})


@channel_session
def msg_connect(message):
    room = message.content['path'].strip('/')
    print('msg_connect', 'room', room)
    message.channel_session['room'] = room

    group = Group('chat-%s' % room)
    group.add(message.reply_channel)


@channel_session
def msg_message(message):
    room = message.channel_session['room']
    print('msg_message', 'room', room)
    Channel('chat-messages').send({
        'room': room,
        'message': message['text']
    })


@channel_session
def msg_disconnect(message):
    room = message.channel_session['room']
    print('msg_disconnect', 'room', room)

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
