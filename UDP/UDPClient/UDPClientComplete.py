from socket import*
import CifraCesar

serverName = "10.0.99.150"
serverPort = 1215

chave = 2

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(3)


try:
    mensagem =  input("Escreva uma mensagem: ")
    mensagemCifrada = CifraCesar.cifrar(mensagem, chave)
    print(f"Enviando (cifrada): {mensagemCifrada}")
    clientSocket.sendto(mensagemCifrada.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    respostaCifrada = modifiedMessage.decode(errors="replace")
    print(f"Recebido (cifrado): {respostaCifrada}")
    print("Resposta do servidor: ", CifraCesar.decifrar(respostaCifrada,chave))
except timeout:
    print("O Pacote foi perdido ou servidor fora do ar ---> Servidor sem resposta")
finally: 
    clientSocket.close()
