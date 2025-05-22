from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class LocationUpdateView(APIView):
    def post(self, request):
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        order_id = request.data.get('order_id')

        # Database में Save करने के लिए कोड डाल सकते हैं (optional)

        # WebSocket group को location update भेजें
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'order_{order_id}', {
                'type': 'location_update',
                'latitude': latitude,
                'longitude': longitude,
                'order_id': order_id,
            }
        )

        return Response({'status': 'Location updated'})
