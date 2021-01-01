import socket
import time
from control import *

sleep_time = 0.050
MAX_LENGTH = 4096
HOST = '192.168.1.12'
PORT = 1243
autopts_server_running = False
autopts_server_process = None

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print('------------------ ------------------')
        print('Connected by', addr, flush=True)

        while True:
            data = conn.recv(MAX_LENGTH)
#             print('Received', repr(data), flush=True)

            if data == b'w':
                ileri()
                time.sleep(sleep_time)
                bosta()
            if data == b'a':
                sol()
                time.sleep(sleep_time)
                bosta()
            if data == b's':
                geri()
                time.sleep(sleep_time)
                bosta()
            if data == b'd':
                sag()
                time.sleep(sleep_time)
                bosta()
            if data == b'q':
                saga_donus()
                time.sleep(sleep_time)
                bosta()
            if data == b'e':
                sola_donus()
                time.sleep(sleep_time)
                bosta()
            if data == b'x':
                stop()
                sys.exit()
            else:
                 print("Our value: Bos")
