from django.urls import path

from api.chatconsumer import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),  # WebSocket route
]