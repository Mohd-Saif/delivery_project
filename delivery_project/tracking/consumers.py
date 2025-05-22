import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DeliveryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.order_id = self.scope['url_route']['kwargs']['order_id']
        self.group_name = f'order_{self.order_id}'

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def location_update(self, event):
        # WebSocket client को डेटा भेजना
        await self.send(text_data=json.dumps({
            'latitude': event['latitude'],
            'longitude': event['longitude'],
            'order_id': event['order_id'],
        }))

