# coding=utf-8
from channels import route

channel_routing = [
    route('websocket.connect', 'consumers.consumers.ws_connect'),
    route('websocket.receive', 'consumers.consumers.ws_message'),
    route('websocket.disconnect', 'consumers.consumers.ws_disconnect'),
]
