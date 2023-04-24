
import time
import os, sys
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
        message_array = message_array[::4]  # 1/4 elements
        message_b64 = []
        for element in message_array:
            message_b64.append(chr(int(element)))
        message = ''.join(message_b64)
        print(message)