# coding=utf-8
from channels import route
from channels.routing import include

chat_routing = [
    route('websocket.connect',
          'consumers.consumers.msg_connect'),
    route('websocket.receive',
          'consumers.consumers.msg_message'),
    route('websocket.disconnect',
          'consumers.consumers.msg_disconnect'),


]

routing = [
    include(chat_routing, path=r'^/'),
    route('chat-messages',
          'consumers.consumers.msg_consumer'),
]
