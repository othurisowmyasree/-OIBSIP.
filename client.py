import socket
import threading

host = "127.0.0.1"
port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

def write():
    while True:
        message = input("")
        client.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()