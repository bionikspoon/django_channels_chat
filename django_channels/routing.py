# coding=utf-8
from channels import route
from channels.routing import include

chat_routing = [
    route('websocket.connect',
          'chat.consumers.msg_connect'),
    route('websocket.receive',
          'chat.consumers.msg_message'),
    route('websocket.disconnect',
          'chat.consumers.msg_disconnect'),


]

routing = [
    include(chat_routing, path=r'^/'),
    route('chat-messages',
          'chat.consumers.msg_consumer'),
]
