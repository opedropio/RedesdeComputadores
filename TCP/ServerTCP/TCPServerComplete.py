from socket import *
import CifraCesar

serverPort = 1215
chave = 1

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
                        recebidoCifrado = data.decode(errors = "Replace")
                        sentence = CifraCesar.decifrar(recebidoCifrado, chave)
                        print(f'Recebido de {addr}(cifrado): {recebidoCifrado}')
                        print(f'Mensagem decifrada: {sentence}')
                        respostaservidor = sentence [::-1]
                        connectionSocket.send(CifraCesar.cifrar(respostaservidor, chave).encode())
            except timeout:
                  print(f"Tempo de espera esgotado, aguardando mensagem de {addr}")
            finally:
                      connectionSocket.close()
except KeyboardInterrupt:
       print(f'O servidor foi encerrado')
finally:
       serverSocket.close()

