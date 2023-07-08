from channels.generic.websocket import AsyncWebsocketConsumer

class FormUpdatesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Connectez-vous à un groupe WebSocket
        await self.channel_layer.group_add('form_updates', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Déconnectez-vous du groupe WebSocket
        await self.channel_layer.group_discard('form_updates', self.channel_name)

