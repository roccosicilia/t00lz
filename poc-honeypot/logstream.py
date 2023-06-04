import json
import socket


SERVER_IP = '192.168.1.100'
SERVER_PORT = 5000

# socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

data = {
    'ojb': 'AAA',
    'desc': 'BBB',
    'info': 30
}

json_data = json.dumps(data)
sock.sendall(json_data.encode())
sock.close()
