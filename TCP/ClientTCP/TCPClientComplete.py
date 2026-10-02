from socket import*
import CifraCesar

serverName = "10.0.99.150"
serverPort = 1215

chave = 1

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5)
try:
    clientSocket.connect((serverName, serverPort))
    sentence = input ('Escreva uma mensagem: ')
    sentenceCifrada = CifraCesar.cifrar(sentence,chave)
    print(f"Enviando (cifrada): {sentenceCifrada}")
    clientSocket.send(sentenceCifrada.encode())
    modifiedSentence = clientSocket.recv(1024).decode(errors="replace")
    print(f"Recebido (cifrada): {modifiedSentence}")
    print("Servidor: ",CifraCesar.decifrar (modifiedSentence,chave))
except timeout:
    print(f'Tempo de espera esgotado, o servidor {serverName} não respondeu')
except ConnectionRefusedError:
        print(f'Conexão recusada: O servidor {serverName} não está funcionando na porta {serverPort}')
finally:
     clientSocket.close()





