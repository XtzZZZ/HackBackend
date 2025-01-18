import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from api.routing import websocket_urlpatterns  # Import WebSocket routes

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles normal HTTP requests
    "websocket": URLRouter(websocket_urlpatterns),  # Handles WebSocket connections
})
