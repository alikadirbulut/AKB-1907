import sys
import tkinter as tk
import socket

#
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("192.168.1.17", 1235))
data = None


def key_input(event):
    # print ('Key:', event.char)ww
    key_press = event.char
    data = key_press.lower()
    print(data)
    clientSocket.send(data.encode())

    # if key_press.lower() == 'w':
    #
    #     clientSocket.send(data.encode())
    # elif key_press.lower() == 's':
    #
    # elif key_press.lower() == 'a':
    #     sol(sleep_time)
    # elif key_press.lower() == 'd':
    #     sag(sleep_time)
    # elif key_press.lower() =='q':
    #     sola_donus(sleep_time)
    # elif key_press.lower() == 'e':
    #     saga_donus(sleep_time)
    # else:
    #     gpio.cleanup()


root = tk.Tk()
root.bind('<KeyPress>', key_input)
root.mainloop()
