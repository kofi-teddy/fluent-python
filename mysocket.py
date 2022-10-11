import asyncio
import datetime
import random, json
import websockets
async def time(websocket, path):     
    while True:
        #now = datetime.datetime.utcnow().isoformat() + "Z"
        #print("rr", websocket)
        requestPayload = json.loads(await websocket.recv())  
        #user_data = User.getAllUsers()
        data = {
                "date": "now",
                "data": requestPayload,
                #"users": (user_data),
                "test": [1, 4, 6]
        }
        #print(">>>>> ", type(user_data), type([1, 4, 6]))
        try:
            await websocket.send(json.dumps(data))            
        except Exception as e:
            await websocket.send(json.dumps(str(e)))            
        await asyncio.sleep(random.random() * 3)
async def main():
    async with websockets.serve(time, "localhost", 5005):
        await asyncio.Future()  # run forever
asyncio.run(main())