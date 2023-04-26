
import time
import os, sys, base64
import platform
import subprocess
import select

file = "./stream.txt"

def mytail(file):
    file.seek(0, os.SEEK_END)
    while True:
        # read last line of file
        line = file.readline()
        # sleep if file hasn't been updated
        if not line:
            time.sleep(45)
            continue
        yield line

if __name__ == '__main__':
    
    logfile = open(file,"r")
    loglines = mytail(logfile)
    # iterate over the generator
    for line in loglines:
        # print(line)
        message_array = line.split(", ")
        message_array = message_array[::2]  # 1/2 elements
        #message_array = message_array[::4]  # 1/4 elements
        #message_array = message_array[::6]  # 1/6 elements
        message_b64 = []
        for element in message_array:
            # message_b64.append(chr(int(element)))
            message_b64.append(chr(element))
        message = ''.join(message_b64)
        try:
            base64_bytes = message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            print(message)
        except:
            print("Encoding error!")
