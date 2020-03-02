from websocket import create_connection
ws = create_connection("ws://localhost:1880/ws/teste")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
print("Sent")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()