Aplicações cliente-servidor com sockets UDP e TCP em Python. 

Redes de Computadores: Sockets UDP e TCP

Primeira atividade avaliativa do módulo de segurança WEB (Cibersegurança, UFU, 2026/2). O repositório reúne duas aplicações cliente-servidor em Python que abrem sockets e trocam dados com os protocolos UDP e TCP, conforme as seções 2.7.1 e 2.7.2 do livro Redes de Computadores e a Internet (Kurose e Ross, 8ª ed.). A porta utilizada é a 1215 (1000 + 3 últimos dígitos da matrícula).

Objetivos
Consolidar conhecimentos em programação e desenvolvimento seguro.
Aplicar conceitos de segurança da informação e cibersegurança, como cifragem de mensagens, timeouts e tratamento de entradas inesperadas.
Compreender na prática a diferença entre comunicação sem conexão (UDP) e orientada a conexão (TCP).
Documentar a evolução acadêmica e prática durante a graduação.
Manter um portfólio organizado dos projetos desenvolvidos.
Conteúdo
Aplicação UDP (UDP/UDPServerT1.py e UDP/UDPClientT1.py)
Socket SOCK_DGRAM, bind na porta 1215, recvfrom e sendto.
O servidor devolve a mensagem em maiúsculas para o endereço do cliente.
O cliente usa settimeout, pois o UDP não garante a entrega.
Aplicação TCP (TCP/TCPServerT1.py e TCP/TCPClientT1.py)
Socket SOCK_STREAM, com listen, accept (um socket dedicado por cliente), send e recv.
Mensagens trafegam cifradas com uma cifra de César (chave 3): o servidor decifra, inverte o texto e responde cifrado. A cifra tem finalidade didática, pois é trivial de quebrar.
Robustez
Timeouts no cliente e no servidor.
Tratamento de conexão recusada e de conexão interrompida pelo cliente.
Bytes inválidos não derrubam o servidor.
Encerramento limpo com Ctrl+C.
Docker (TCP/Dockerfile): imagem para executar o servidor TCP.
Como executar (Python 3, sem dependências externas):

# em dois terminais diferentes, na raiz do repositório
python3 UDP/UDPServerT1.py     # e depois: python3 UDP/UDPClientT1.py
python3 TCP/TCPServerT1.py     # e depois: python3 TCP/TCPClientT1.py

# servidor TCP com Docker (dentro da pasta TCP/)
docker build -t tcp-1215 .
docker run -d --name tcp1215 --restart unless-stopped -p 1215:1215 tcp-1215

Nos clientes, serverName é 127.0.0.1 para testes locais e 10.0.99.150 para o servidor da turma.

Tecnologias Utilizadas
Python (biblioteca padrão socket)
Sockets UDP e TCP
Docker
Git
GitHub
Conceitos de Cibersegurança (cifra de César, robustez de serviços de rede)

Desenvolvido durante o curso de Bacharelado em Cibersegurança - UFU.
