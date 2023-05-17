import socket
import os

dir = os.path.dirname(os.path.abspath(__name__))
server_ip = '172.25.82.136'  ## use your server ip

def log_message(message):
    with open("log.txt", "a") as log_file:
        log_file.write(message + "\n")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, 8888))
    server_socket.listen(1)
    print("In attesa di connessioni...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connessione accettata da {addr[0]}:{addr[1]}")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            log_message(data)

        conn.close()

start_server()
