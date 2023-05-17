import socket
import os
from datetime import datetime

dir = os.path.dirname(os.path.abspath(__name__))
server_ip = '172.25.82.136'  ## use your server ip
company_name = "CONTOSO Inc."

def log_message(message):
    with open(f"{dir}/logs/log.txt", "a") as log_file:
        log_file.write(message)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, 2222))
    server_socket.listen(1)
    print("In attesa di connessioni...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connessione accettata da {addr[0]}:{addr[1]}")

         # attempts counter
        att = 1

        while True:
            try:
                # base data
                now = datetime.now()
                formatted_datetime = now.strftime("%Y/%m/%d %H:%M:%S")

                # login message
                login_message  = "\n"
                login_message += "/********************************************************************************/\n"
                login_message += "/* Authorized access only!                                                      */\n"
                login_message += "/* If you are not authorized to access or use this system, disconnect now!      */\n"
                login_message += "/********************************************************************************/\n"
                login_message += "\n"
                login_message += "Username: "
                conn.sendall(login_message.encode())

                # insert username
                login = conn.recv(4096).decode()
                if login == 'stopit':
                    break

                # insert password
                password_message = "Password: "
                conn.sendall(password_message.encode())
                password = conn.recv(4096).decode()
                if password == 'stopit':
                    break

                # logging
                log_message(f"[{formatted_datetime}] - {addr[0]}:{addr[1]} - Login attempt for user {login.strip()} and password {password.strip()} \n")

                # error message
                error_message = "Invalid credentials.\n"
                conn.sendall(error_message.encode())

                # attempts counter
                if att > 3:
                    # error message
                    error_message = "Connection closed.\n"
                    conn.sendall(error_message.encode())
                    log_message(f"[{formatted_datetime}] - Connection closed: to many attempts. \n")
                    break
                att += 1

            except:
                log_message(f"[{formatted_datetime}] - Error: scan attempt or malformed data. \n")

        conn.close()

start_server()