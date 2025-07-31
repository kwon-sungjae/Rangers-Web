from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
import json
import time as T

from chat.models import Chat
from common.models import User
from chat.filtering import classify_sentence

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        nickname = text_data_json['userinfo']
        url = text_data_json['url']
        create_date = datetime.now()
        time = str(create_date.strftime('%Y-%m-%d %H:%M:%S'))

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'time' : time,
                'nickname' : nickname,
                'url' : url
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        time = event['time']
        nickname = event['nickname']
        url = event['url']
        urllist = url.split('/')
        
        lastchat = Chat.objects.values().order_by('-create_date')[:1][0]
        lastnickname = lastchat['author_id']
        lastchatmessage = lastchat['message']
        lastdate = str(lastchat['create_date']).split(' ')
        lastdate = (lastdate[1].split('+'))[0].split('.')[0]
        user = User.objects.get(nickname=nickname)
        
        lastdate = lastdate.split(':')
        lastdate = int(lastdate[0])*24*60+int(lastdate[1])*60+int(lastdate[2])
        
        nowtime = time.split(' ')[1]
        nowtime = nowtime.split(':')
        nowtime = int(nowtime[0])*24*60+int(nowtime[1])*60+int(nowtime[2])
        vilification = bool(classify_sentence(message))
        if message != '':
            if not (user.id==lastnickname and message==lastchatmessage and abs(lastdate-nowtime)<=2):
                if vilification:
                    Chat.objects.create(roomname=urllist[-2],author_id=user.id,message=message,vilification=vilification)
                    user.counting-=30
                    if user.counting<0:
                        user.counting = 0
                    user.save()
                else:
                    Chat.objects.create(roomname=urllist[-2],author_id=user.id,message=message,vilification=vilification)
                    if user.counting<1000:
                        user.counting+=1
                    user.save()

        counting = user.counting
        widthcounting = counting/10
        
        time = time.split(' ')
        time = time[0].split('-')+time[1].split(':')
        time[3] = int(time[3])
        if time[3]==12:
            time[5] = '오후'
        elif time[3]>12:
            time[3]-=12
            time[5] = '오후'
        else:
            time[5] = '오전'
        time = time[0]+'년 '+str(int(time[1]))+'월 '+str(int(time[2]))+'일 '+str(time[3])+':'+time[4]+' '+time[5]
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'time' : time,
            'nickname' : nickname,
            'counting' : str(counting),
            'widthcounting' : str(widthcounting),
            'is_artist' : str(user.is_artist),
            'room_name':urllist[-2],
            'profileimageurl':user.profileimage.url,
            'vil':str(int(vilification)),
        }))