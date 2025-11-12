import socket
# Definindo o host e a porta do servidor
HOST = '0.0.0.0'
PORT = 5000
# ------------------------------------------------

# Arte ASCII do jogo -----------------------------
LOGO = r'''
██     ██ ██    ██ ██████       ██████   █████  ███    ███ ███████ ███████ 
██     ██ ██    ██ ██   ██     ██       ██   ██ ████  ████ ██      ██      
██  █  ██ ██    ██ ██████      ██   ███ ███████ ██ ████ ██ █████   ███████ 
██ ███ ██  ██  ██  ██          ██    ██ ██   ██ ██  ██  ██ ██           ██ 
 ███ ███    ████   ██           ██████  ██   ██ ██      ██ ███████ ███████ 
'''

NOMEGAME = r'''
  _      ___   _____       __     __ __         ___   //| __        ____              __  
 | | /| / / | / / _ \  __ / /__  / //_/__ ___  / _ \_|/||/ /  ___ _/ __/__  ___  ____/ /__
 | |/ |/ /| |/ / ___/ / // / _ \/ ,< / -_) _ \/ ___/ _ \/ /__/ _ `/\ \/ _ \/ _ \/ __/  '_/
 |__/|__/ |___/_/     \___/\___/_/|_|\__/_//_/_/   \___/____/\_,_/___/ .__/\___/\__/_/\_\ 
                                                                    /_/                   
'''
# -------------------------------------------------

# Criando o socket do servidor e ligando ao host e a porta | Usado modelo TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print(f'''Servidor WVP Games Funcionando!\nLocal Servidor: {HOST}\nPorta Servidor: {PORT}
      \nAguardando Cliente...''')
# ------------------------------------------------

# Estabelecendo conexão com o cliente
conexao, endereco = servidor.accept()
print(f'Conectado: {endereco}')
print(f'{LOGO}')
conexao.sendall('Você conectou ao servidor ⓌⓋⓅ Ⓖⓐⓜⓔⓢ!'.encode('utf-8'))
# ------------------------------------------------
# Recebendo mensagem do cliente e exibindo no servidor
mensagem = conexao.recv(1024).decode('utf-8')
print(f'Mensagem recebida: {mensagem}')
# ------------------------------------------------

# Fechando a conexão com o cliente e o servidor
conexao.close()
servidor.close()
# ------------------------------------------------