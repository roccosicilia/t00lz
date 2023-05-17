import socket, os, sys, syslog
from datetime import datetime

dir = os.path.dirname(os.path.abspath(__name__))
facility = syslog.LOG_LOCAL7
server_ip = sys.argv[1]
company_name = sys.argv[2]

def log_message(message):
    with open(f"{dir}/logs/log.txt", "a") as log_file:
        log_file.write(message)

def start_server():
    syslog.syslog(facility | syslog.LOG_INFO, "SSH Honeypot started.")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, 2222))
    server_socket.listen(1)
    print("In attesa di connessioni...")

    while True:
        conn, addr = server_socket.accept()
        print(f"New connection from {addr[0]}:{addr[1]} to SSH Honeypot.")
        syslog.syslog(facility | syslog.LOG_INFO, f"New connection from {addr[0]}:{addr[1]} to SSH Honeypot.")

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
                log_message(f"[{formatted_datetime}] - Login attempt from {addr[0]}:{addr[1]} for user {login.strip()} and password {password.strip()}.\n")
                syslog.syslog(facility | syslog.LOG_INFO, f"Login attempt from {addr[0]}:{addr[1]} for user {login.strip()} and password {password.strip()}.")

                # error message
                error_message = "Invalid credentials.\n"
                conn.sendall(error_message.encode())

                # attempts counter
                if att > 3:
                    # error message
                    error_message = "Connection closed.\n"
                    conn.sendall(error_message.encode())
                    log_message(f"[{formatted_datetime}] - Connection closed for {addr[0]}:{addr[1]}: to many attempts. \n")
                    syslog.syslog(facility | syslog.LOG_INFO, f"Connection closed for {addr[0]}:{addr[1]}: to many attempts.")
                    break
                att += 1

            except:
                log_message(f"[{formatted_datetime}] - Error: scan attempt or malformed data from {addr[0]}:{addr[1]}. \n")
                syslog.syslog(facility | syslog.LOG_INFO, f"Error: scan attempt or malformed data from {addr[0]}:{addr[1]}.")
                break

        conn.close()

start_server()
