from django.urls import re_path

from . import consumers

# use re_path due to limitations in URLRouter
websocket_urlpatterns = [
	re_path(r'ws/', consumers.MessageConsumer.as_asgi()),
]