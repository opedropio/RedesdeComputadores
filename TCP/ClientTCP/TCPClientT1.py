from socket import*
serverName = "10.0.99.150"
serverPort = 1215
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5)
try:
    clientSocket.connect((serverName, serverPort))
    sentence = input ('Escreva uma mensagem: ')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print("Servidor: ", modifiedSentence.decode())
except timeout:
    print(f'Tempo de espera esgotado, o servidor {serverName} não respondeu')
except ConnectionRefusedError:
        print(f'Conexão recusada: O servidor {serverName} não está funcionando na porta {serverPort}')
finally:
     clientSocket.close()





