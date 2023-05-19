import socket, os, sys, syslog
from datetime import datetime

dir = os.path.dirname(os.path.abspath(__name__))
facility = syslog.LOG_LOCAL7
server_port = 8080
try:
    server_ip = sys.argv[1]
except:
    server_ip = 'localhost'


def log_message(message):
    with open(f"{dir}/logs/log.txt", "a") as log_file:
        log_file.write(message)

def start_server():
    syslog.syslog(facility | syslog.LOG_INFO, "HTTP Honeypot started.")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print("Listening on {}:{}...".format(server_ip, server_port))

    while True:
        conn, addr = server_socket.accept()
        print(f"New connection from {addr[0]}:{addr[1]} to HTTP Honeypot.")
        syslog.syslog(facility | syslog.LOG_INFO, f"New connection from {addr[0]}:{addr[1]} to HTTP Honeypot.")

        while True:
            try:
                # base data
                now = datetime.now()
                formatted_datetime = now.strftime("%Y/%m/%d %H:%M:%S")
                client_request = conn.recv(4096).decode("utf-8")
                log_message(f"[{formatted_datetime}] - [{client_request}]\n")
                syslog.syslog(facility | syslog.LOG_INFO, f"[{formatted_datetime}] - [{client_request}]")

                # http message
                html_content  = "HTTP/1.1 200 OK\r\n"
                html_content += "Content-Type: text/html\r\n"
                html_content += "\r\n"
                html_content += "<!DOCTYPE html>\r\n"
                html_content += "<html>\r\n"
                html_content += "<head>\r\n"
                html_content += "<title>Server HTTP</title>\r\n"
                html_content += "</head>\r\n"
                html_content += "<body>\r\n"
                html_content += "<h1>Benvenuto nel server HTTP!</h1>\r\n"
                html_content += "</body>\r\n"
                html_content += "</html>\r\n"
                conn.sendall(html_content.encode("utf-8"))

            except:
                log_message(f"[{formatted_datetime}] - Error: scan attempt or malformed data from {addr[0]}:{addr[1]}. \n")
                syslog.syslog(facility | syslog.LOG_INFO, f"Error: scan attempt or malformed data from {addr[0]}:{addr[1]}.")
                break

start_server()
