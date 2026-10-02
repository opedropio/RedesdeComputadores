from socket import*
serverName = "10.0.99.150"
serverPort = 1215
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(3)
try:
    mensagem =  input("Escreva uma mensagem: ")
    clientSocket.sendto(mensagem.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("Resposta do servidor: ", modifiedMessage.decode())
except timeout:
    print("O Pacote foi perdido ou servidor fora do ar ---> Servidor sem resposta")
finally: 
    clientSocket.close()


