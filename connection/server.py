import socket
import threading
import connection.database as db


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

data_list = []


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else:
                pass

            data_list.append(msg)

            if len(data_list) == 3:
                # send to DB
                user = data_list[0]
                password = data_list[1]
                action = data_list[2]
                print("PRE " + str(data_list))
                # save or delete to DB
                if action == "start":
                    db.adding(user, password)
                elif action == "stop":
                    db.deleting(user, password)
                else:
                    pass
                data_list.clear()
            else:
                pass

            print(f"[{addr}] {msg}")
            print("POST " + str(data_list))
            conn.send("Msg received".encode(FORMAT))

    conn.close()





def start_server():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")




print("[STARTING] server is starting...")
#start_server()