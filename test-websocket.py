import os
import django
import asyncio
import datetime
import random
import json
import websockets
from decouple import config


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from chatapp.models import Conversation
from user.models import User
from chatapp.models import Message
from django.db.models import Q
from chatapp.serializers import ConversationSerializer


async def time(websocket, path):
    while True:
        requestPayload = json.loads(await websocket.recv())
        if requestPayload.get('text') and requestPayload.get('sender') and requestPayload.get('receiver'):
            print("wwwwwwwwwww")
            sender_id = requestPayload.get('sender', None)
            receiver_id = requestPayload.get('receiver', None)
            text = requestPayload.get('text', None)
            sender = User.objects.filter(id=sender_id).first()
            receiver = User.objects.filter(id=receiver_id).first()

            if sender:
                conversation = Conversation.objects.filter(Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender)).first()
                if conversation:
                    chat_id = conversation
                    message = Message.objects.create(sender=sender, receiver=receiver, text=text, conversation_id=conversation, attachment="")
                else:
                    conversation = Conversation.objects.create(sender=sender, receiver=receiver)
                    message = Message.objects.create(sender=sender, receiver=receiver, text=text, conversation_id=conversation, attachment="")
                convo = (ConversationSerializer(instance=conversation).data)

                data = {
                    
                        "conversation": convo
                }
                try:
                    await websocket.send(json.dumps(data))            
                except Exception as e:
                    await websocket.send(json.dumps(str(e)))            
                await asyncio.sleep(random.random() * 3)
                    
        elif requestPayload.get('user_id'):
            print("hiiiiiiii")
            user_id = requestPayload.get('user_id', None)
            user = User.objects.filter(id=user_id).first()

            data = {}
            if user:
                conversation = Conversation.objects.filter(Q(sender=user) | Q(receiver=user))
                if conversation:
                    serializer = ConversationSerializer(conversation, many=True)
                    # if serializer.is_valid():
                    #     serializer.save()
                    data = {
                            "status": True,
                            "message": "Successful",
                            "conversation": serializer.data
                    }
                else:
                    data = {"message": "No conversation", "status": False, "status_code": 404}
            else:
                data = {"message": "No user", "status": False, "status_code": 404}

            try:
                await websocket.send(json.dumps(data))
            except Exception as e:
                await websocket.send(json.dumps(str(e)))
            await asyncio.sleep(random.random() * 3)

        elif requestPayload.get('user1_id') and requestPayload.get('user2_id'):
            print("heeeeyyyyy")
            user1_id = requestPayload.get('user1_id', None)
            user2_id = requestPayload.get('user2_id', None)
            data = {}
            conversation = Conversation.objects.filter(Q(sender=user1_id, receiver=user2_id) | Q(sender=user2_id, receiver=user1_id)).first()
            if conversation:
                convo = (ConversationSerializer(instance=conversation).data)
                # if serializer.is_valid():
                #     serializer.save()
                data = {
                        "status": True,
                        "message": "Successful",
                        "conversation_id": convo
                }
            else:
                data = {"message": "Conversation does not exist", "status": False, "status_code": 404}
           
            
            try:
                await websocket.send(json.dumps(data))
            except Exception as e:
                await websocket.send(json.dumps(str(e)))
            await asyncio.sleep(random.random() * 3)

        elif requestPayload.get('message_id'):
            print("BBBBBBBBBBB")
            data = {}
            message_id = requestPayload.get('message_id', None)
            message = Message.objects.filter(id=message_id)
            if message:
                message.delete()
               
                data = {
                        "status": True,
                        "message": "Successful",
                }
            else:
                data = {"message": "Message does not exist", "status": False, "status_code": 404}
            
            try:
                await websocket.send(json.dumps(data))
            except Exception as e:
                await websocket.send(json.dumps(str(e)))
            await asyncio.sleep(random.random() * 3)

        elif requestPayload.get('conversation_id'):
            print("AAAAAAAAAA")
            data = {}
            conversation_id = requestPayload.get('conversation_id', None)
            conversation = Conversation.objects.filter(id=conversation_id)
            if conversation:
                conversation.delete()
               
                data = {
                        "status": True,
                        "message": "Successful",
                }
            else:
                data = {"message": "Conversation does not exist", "status": False, "status_code": 404}
            
            try:
                await websocket.send(json.dumps(data))
            except Exception as e:
                await websocket.send(json.dumps(str(e)))
            await asyncio.sleep(random.random() * 3)


async def main():
    async with websockets.serve(time, "localhost", config("WEBSOCKET_PORT")):
        await asyncio.Future()  # run forever
asyncio.run(main())

