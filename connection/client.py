import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(user, password, action):

    USER = user.encode(FORMAT)
    PASSWORD = password.encode(FORMAT)
    ACTION = action.encode(FORMAT)

    # For user
    msg_length = len(USER)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(USER)
    print(client.recv(2048).decode(FORMAT))

    # For password
    msg_length = len(PASSWORD)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(PASSWORD)
    print(client.recv(2048).decode(FORMAT))

    # For action
    msg_length = len(ACTION)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(ACTION)
    print(client.recv(2048).decode(FORMAT))
