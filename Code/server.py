####### SERVER ########

import socket
import strToArray
import movimentServos


def Main():
    print("IP Adress: ")
    s = socket.socket()
    print(str(socket.gethostbyname(socket.gethostname())))
    host = '192.168.43.73'
    #socket.gethostbyname(socket.gethostname()) 
    port = 12345

    #s = socket.socket()
    s.bind((host,port))

    s.listen(5)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:

            break
        
        print( data + " recived")
        c.send(data.encode('utf-8'))
        mimoPose = strToArray.convert(data)
        print(mimoPose)
        movimentServos.colocarAngles(mimoPose)
        
    c.close()

if __name__ == '__main__':
    Main()