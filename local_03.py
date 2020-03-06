import requests
from websocket import create_connection

url = 'http://localhost:1880/python'
myobj = {'desenovolvedor': 'misael'}

ws = create_connection("ws://localhost:1880/ws/statusCom")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()

