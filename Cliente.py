import socket

HOST = '127.0.0.1'
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))
print(f'Conectado!{HOST}:{PORT}')

mensagem = cliente.recv(1024).decode('utf-8')
print(f'Servidor: {mensagem}')
cliente.sendall('Cliente conectado!'.encode('utf-8'))
cliente.close()