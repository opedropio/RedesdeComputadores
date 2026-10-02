from socket import *
serverPort = 1215
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("O servidor está ativo e operante")
try: 
    while True:
            connectionSocket, addr = serverSocket.accept()
            print(f'Conexão de {addr}')
            connectionSocket.settimeout(15)
            try: 
                  data = connectionSocket.recv(1024)
                  if data:
                        sentence = data.decode()
                        capitalizedSentence = sentence.upper()
                        print(f'Recebido de {addr}: {sentence}')
                        connectionSocket.send(capitalizedSentence.encode())
            except timeout:
                  print(f"Tempo de espera esgotado, aguardando mensagem de {addr}")
            finally:
                      connectionSocket.close()
except KeyboardInterrupt:
       print(f'O servidor foi encerrado')
finally:
       serverSocket.close()




