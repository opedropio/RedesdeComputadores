from socket import*
serverPort = 1215
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverSocket))
print("O servidor está ativo e operante")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    
    