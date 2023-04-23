
import time
import os
import platform

last_status_t = int(time.time())
val = True

while val:
    file_status = os.stat("./stream.txt")
    file_status_t = file_status.st_ctime
    if file_status_t > last_status_t:
        print("file change")
        last_status_t = file_status_t
    else:
        print(file_status.st_ctime, last_status_t)
