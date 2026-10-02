from socket import*
serverPort = 1215
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("O servidor está ativo e operante")
try: 
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        print(f'Recebido de {clientAddress}: {message.decode()}')
        serverSocket.sendto(modifiedMessage.encode(),clientAddress)
except KeyboardInterrupt:
    print("Servidor fechado")
finally:
    serverSocket.close()
    



