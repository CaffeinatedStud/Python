import socket,os
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverAddress = ("xxx.xxx.xx.xx", xxxx)
server_socket.bind(serverAddress)
server_socket.listen(5)

i=0
while True:
    print("waiting for connection")
    connection, client_address = server_socket.accept()
    print("connection from", client_address)
    directory = client_address[0]
     
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    data = connection.recv(16)
    print(data.decode())
    if data.decode() == "png":
        try:
            now = datetime.datetime.now()

            rightnow = now.strftime("%Y-%m-%d-%H-%M")
            image = str(i) + "_" + "image" + rightnow  + ".png"
            print(image)

            fp = open(directory + '/' + image, 'wb')
            # print("connection", connection)
            while True:
                data = connection.recv(4096)
                if not data:
                    break
                fp.write(data)
            fp.close()
            print("Data received ", i)
            i+=1
        except socket.error:
            print("socket Error")
    else:
        text = "log.txt"
        print(text)
        txt = open(directory + '/' + text, 'wb')
        while True:
            txtdata = connection.recv(4)
            if not txtdata:
                break
            txt.write(txtdata)
        txt.close()
        print("log received")
print("Data Received Successfully")
connection.close()
exit()
