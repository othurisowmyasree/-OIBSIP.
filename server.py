import socket
import threading

host = "127.0.0.1"
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            clients.remove(client)
            client.close()
            break

def receive():
    print("Server started...")
    while True:
        client, addr = server.accept()
        print(f"Connected: {addr}")

        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()