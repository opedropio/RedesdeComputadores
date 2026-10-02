
"""
from socket import*

---> O modulo socket forma a base de todas as 
comunicacoes python, quando importamos podemos criar
sockets dentro do programa. 

serverPort = 1215

---> Variavel oferecemos a porta que estabelecemos o socket
nesse caso 1000+215 (matricula)

serverSocket = socket(AF_INET, SOCK_DGRAM)

---> Nessa linha cria-se o socket do servidor (serverSocket),
passando o primeiro parametro AF_NET que indica que a rede
subjacete esta usando IPv4. O segundo parametro SOCK_DGRAM
indica que e uma conexao UDP 

serverSocket.bind(("", serverSocket))

---> Vincula o numero de porta ao socket do servidor, 
assim quando enviado um pacote enviado uma mensagem na porta
1215 no IP do servidor e direcionado a este socket. E o UDPserver
entra no laco while

print("O servidor está ativo e operante")

---> Funcao do python que será exibida quando o servidor estiver ativo 

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
    
    
---> A primeira linha quando o pacote chega no socket do servidor
os dados são colocado na variavel message e o IP origem na variavel
clientAddress que contem IP e porta do cliente, assim o servidor
sabe para onde direcionar a resposta. 
Segunda linha modifica a mensagem enviado pelo cliente e atraves 
do metodo upper() passa para letras maisculas. 
A terceira linha vincula o IP e porta do cliente a mensagem maiscula
enviando o pacote para o socket do servidor e a internet estraga o pacote
ao IP do cliente.
    
    """