import socket
import os

dir = os.path.dirname(os.path.abspath(__name__))
server_ip = '172.25.82.136'  ## use your server ip

def simulate_ssh(addr):
    username = input("Username: ")
    password = input("Password: ")

    with open("{}/ssh_log.txt".format(dir), "a") as log_file:
        log_file.write(f"IP: {addr[0]}:{addr[1]}, Username: {username}, Password: {password}\n")
        log_file.write("Invalid credentials\n")

    print("Invalid credentials")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, 22))
server_socket.listen(1)

print("Listening... ")

while True:
    conn, addr = server_socket.accept()
    print(f"Connessione accettata da {addr[0]}:{addr[1]}")
    simulate_ssh(addr)
    conn.close()
