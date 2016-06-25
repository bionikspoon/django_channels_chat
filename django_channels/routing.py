# coding=utf-8
from channels import route
from channels.routing import include

chat_routing = [
    route('websocket.connect',
          'consumers.consumers.chat_connect',
          path=r'^/(?P<room>[a-zA-Z0-9_]+)/$'),
    route('websocket.receive',
          'consumers.consumers.chat_message',
          path=r'^/(?P<room>[a-zA-Z0-9_]+)/$'),
    route('websocket.disconnect',
          'consumers.consumers.chat_disconnect',
          path=r'^/(?P<room>[a-zA-Z0-9_]+)/$'),

]

routing = [
    include(chat_routing, path=r'^/chat'),
]
