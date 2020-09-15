import socket
import time

def status():
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.13' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP, TCP_PORT))
        response = s.recv(BUFFER_SIZE)
    except socket.error:
        print("Socket error")
        s.close()
    s.send(b"programState\n")
    response = s.recv(BUFFER_SIZE)
    print(response)
    s.close()
    return str(response)

def perform_task(cmd):
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.13' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP, TCP_PORT))
        response = s.recv(BUFFER_SIZE)
    except socket.error:
        print("Socket error")
        s.close()

    st = "load /programs/{}.urp\n".format(cmd)
    s.send(bytearray(st,'utf8'))
    response = s.recv(BUFFER_SIZE)
    s.send(b"play\n")
    response = s.recv(BUFFER_SIZE)
    s.close()

perform_task("lego")
