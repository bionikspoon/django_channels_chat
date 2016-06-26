# coding=utf-8
from channels import route
from channels.routing import include

chat_routing = [
    route('websocket.connect',
          'chat.consumers.chat_connect'),
    route('websocket.receive',
          'chat.consumers.chat_message'),
    route('websocket.disconnect',
          'chat.consumers.chat_disconnect'),


]

routing = [
    include(chat_routing, path=r'^/'),
    route('chat-messages',
          'chat.consumers.chat_consumer'),
]
