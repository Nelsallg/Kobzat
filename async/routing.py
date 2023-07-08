from django.urls import re_path

from ..async import consumers

websocket_urlpatterns = [
    re_path(r'ws/form-updates/$', consumers.FormUpdatesConsumer.as_asgi()),
]
