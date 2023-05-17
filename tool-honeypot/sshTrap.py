import socket
import os

dir = os.path.dirname(os.path.abspath(__name__))
server_ip = '172.25.82.136'  ## use your server ip

def process_data(data):
    if data == "5":
        return "grazie"
    else:
        return "Dato non valido"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, 2222))
    server_socket.listen(1)
    print("In attesa di connessioni...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connessione accettata da {addr[0]}:{addr[1]}")

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            
            print(f"Dato ricevuto: {data}")

            response = process_data(data)
            conn.sendall(response.encode())

        conn.close()

start_server()