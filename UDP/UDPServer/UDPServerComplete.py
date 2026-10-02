from socket import*
import CifraCesar

serverPort = 1215
chave = 2

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("O servidor está ativo e operante")

try: 
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        recebidoCifrado = message.decode(errors="replace")
        mensagem = CifraCesar.decifrar(recebidoCifrado, chave)
        print(f'Recebido de {clientAddress} (cifrado): {recebidoCifrado}')
        print(f'Mensagem decifrada: {mensagem}')
        resposta = mensagem[::-1]
        serverSocket.sendto(CifraCesar.cifrar(resposta, chave).encode(),clientAddress)
except KeyboardInterrupt:
    print("Servidor fechado")
finally:
    serverSocket.close()