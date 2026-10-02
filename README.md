# Redes de Computadores: Sockets UDP e TCP

Primeira atividade avaliativa de Cibersegurança - UFU 2026/2.

Este repositório contém duas aplicações cliente-servidor desenvolvidas em Python para demonstrar comunicação utilizando os protocolos UDP e TCP, conforme o conteúdo de programação de sockets estudado em Kurose e Ross.

## Objetivos

* Implementar uma comunicação cliente-servidor utilizando UDP.
* Implementar uma comunicação cliente-servidor utilizando TCP.
* Praticar a criação, configuração e utilização de sockets.
* Demonstrar o envio e recebimento de mensagens entre cliente e servidor.
* Utilizar uma cifra de César para cifrar e decifrar as mensagens.

## Estrutura do projeto

```text
TCP/
├── ClientTCP/
│   ├── CifraCesar.py
│   ├── TCPClientComplete.py
│   ├── TCPClientKUROSE.py
│   ├── TCPClientT1.py
│   └── ...
└── ServerTCP/
    ├── CifraCesar.py
    ├── TCPServerComplete.py
    ├── TCPServerKUROSE.py
    ├── TCPServerT1.py
    └── ...

UDP/
├── UDPClient/
│   ├── CifraCesar.py
│   ├── UDPClientComplete.py
│   ├── UDPClientKUROSE.py
│   ├── UDPClientT1.py
│   └── ...
└── UDPServer/
    ├── CifraCesar.py
    ├── UDPServerComplete.py
    ├── UDPServerKUROSE.py
    ├── UDPServerT1.py
    └── ...
```

## Aplicação UDP

A aplicação UDP utiliza:

* `socket.AF_INET`
* `socket.SOCK_DGRAM`
* `bind()`
* `sendto()`
* `recvfrom()`

O cliente envia uma mensagem cifrada para o servidor.

O servidor:

1. recebe a mensagem;
2. decifra utilizando a cifra de César;
3. inverte a mensagem;
4. cifra novamente;
5. envia a resposta ao cliente.

### Executando o UDP

Na raiz do repositório, abra dois terminais.

**Terminal 1 - servidor UDP:**

```bash
python3 UDP/UDPServer/UDPServerComplete.py
```

**Terminal 2 - cliente UDP:**

```bash
python3 UDP/UDPClient/UDPClientComplete.py
```

## Aplicação TCP

A aplicação TCP utiliza:

* `socket.AF_INET`
* `socket.SOCK_STREAM`
* `bind()`
* `listen()`
* `accept()`
* `connect()`
* `send()`
* `recv()`

O cliente estabelece uma conexão com o servidor e envia uma mensagem cifrada.

O servidor:

1. aceita a conexão;
2. recebe a mensagem;
3. decifra a mensagem;
4. inverte o texto;
5. cifra novamente;
6. envia a resposta ao cliente.

### Executando o TCP

Na raiz do repositório, abra dois terminais.

**Terminal 1 - servidor TCP:**

```bash
python3 TCP/ServerTCP/TCPServerComplete.py
```

**Terminal 2 - cliente TCP:**

```bash
python3 TCP/ClientTCP/TCPClientComplete.py
```

## Cifra de César

As mensagens utilizadas na comunicação são cifradas com uma cifra de César.

A implementação está no arquivo:

```text
CifraCesar.py
```

A cifra preserva letras maiúsculas e minúsculas e mantém espaços, números e outros caracteres sem alteração.

## Porta

A aplicação utiliza a porta:

```text
1215
```

Essa porta deve corresponder ao valor definido no enunciado da atividade.

## Testes

As aplicações TCP e UDP foram executadas localmente utilizando:

```text
127.0.0.1
```

Os testes demonstraram o envio e recebimento das mensagens entre cliente e servidor.

## Tecnologias

* Python 3
* Biblioteca `socket`
* Git
* GitHub

## Atividade

Universidade Federal de Uberlândia - UFU

Curso de Cibersegurança

1ª Atividade Avaliativa - 2026/2
