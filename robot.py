
import socket
<<<<<<< HEAD
import math
from types import SimpleNamespace

class UR_programmer():

    def __init__(self, ip, simulate):
        #Socket til at sende kommandoer til robotten
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(10)
        self.connected = False

        #Tegneparametre:
        self.tegnehojde = 0.00601
        #Grænser for tegningen (x-min, y-min, x-max, y-max)
        #Robot 3: x [-0.525, -0.325] y [-0.542, -0.265]
        self.tegne_limits = [-0.525, -0.542, -0.325, -0.265]
        self.home_pos = b'    movej(p[-0,409,-0.322, 0.200, 1.95, 0.012, -0.088])\n'

        #Husk at kontrollere ip-adressen!
        if not simulate:
            self.connect(ip)
            print("forbindelse ok")
        else:
            self.s = SimpleNamespace()
            self.s.send = lambda a : print(a)

    def connect(self, ip):
        #TCP_IP ='10.130.58.11'
        #Husk at kontrollere ip-adressen!
        TCP_IP = ip
        TCP_PORT = 30002
        BUFFER_SIZE = 1024

        try:
            #print("Opening IP Address" + TCP_IP)
            self.s.connect((TCP_IP, TCP_PORT))
            response = self.s.recv(BUFFER_SIZE)
            self.connected = True
        except socket.error:
            print("Socket error")
            self.s.close()


    def move_home(self):
        #Prædefineret home-position:
        #(Når vi skal sende en streng til robotten,
        # skal den konverteres til et bytearray
        # derfor står der b foran strengen.)
        self.s.send(b'def myProg():\n')
        self.s.send(self.home_pos)
        self.s.send(b'end\n')


    def move_xyz(self, x, y, z):
        '''
        Denne funktion laver et UR-script program, og sender det til robotten.
        Programmet vil indeholde en enkelt movel-kommando, til punktet x,y,z,
        der er givet som argumenter til denne funktion.

        Bemærk: Der kontrolleres ikke grænser på hverken x, y eller z!
        (Denne funktion er ikke beregnet til tegning, men til transport)
        '''
        #Når vi skal sende en streng til robotten,
        # skal den konverteres til et bytearray
        # derfor står der b' foran strengen.
        self.s.send(b'def myProg():\n')
        #Vi læser robottens aktuelle konfiguration,
        # for at genbruge rotationen.
        self.s.send(b'  var_1=get_actual_tcp_pose()\n')
        st = '  var_1[0] = {:.5f}\n'.format(x)
        self.s.send(bytearray(st,'utf8'))
        st = '  var_1[1] = {:.5f}\n'.format(y)
        self.s.send(bytearray(st,'utf8'))
        st = '  var_1[2] = {:.5f}\n'.format(z)
        self.s.send(bytearray(st,'utf8'))
        self.s.send(b'  movel(var_1)\n')
        #self.s.send(bytearray(st,'utf8'))
        self.s.send(b'end\n')


    def move_path(self, path):

        self.s.send(self.home_pos)
        self.s.send(b'end\n')

        print('Program sendt til robot.')
        if limit_error:
            print('(Mindst et punkt blev udeladt, fordi det lå udenfor tegneområdet)')


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
=======
import time

def status():
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.14' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
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
    TCP_IP = '10.130.58.14' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(10)
    try:
        s.connect((TCP_IP, TCP_PORT))
>>>>>>> RobotCode
        response = s.recv(BUFFER_SIZE)
        s.close()
<<<<<<< HEAD
=======

    st = "load /programs/{}.urp\n".format(cmd)
    s.send(bytearray(st,'utf8'))
    response = s.recv(BUFFER_SIZE)
    s.send(b"play\n")
    response = s.recv(BUFFER_SIZE)
    s.close()


def stop_task(cmd):
    TCP_PORT = 29999
    BUFFER_SIZE = 1024
    TCP_IP = '10.130.58.14' #INDTAST DEN RIGTIGE IP-ADRESSE HER!
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
    s.send(b"stop\n")
    response = s.recv(BUFFER_SIZE)
    s.close()

#perform_task("roed_klods")

stop_task("roed_klods")
>>>>>>> RobotCode
