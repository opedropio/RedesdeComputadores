from socket import*
serverName = "servername"
serverPort = 1215
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input ('Escreva uma mensagem: ')
clientSocket.send(sentence.encode())
modificedSentence = clientSocket.recv(1024)
print("Servidor: ", modificedSentence.decode())
clientSocket.close()
