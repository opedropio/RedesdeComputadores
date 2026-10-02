from socket import*
serverName = "10.0.99.150"
serverPort = 1215
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Escreva uma menssagem:")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage())
clientSocket.close()