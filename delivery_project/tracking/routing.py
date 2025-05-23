# tracking/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/delivery/(?P<order_id>\w+)/$', consumers.DeliveryConsumer.as_asgi()),
]
