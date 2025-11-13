import socket
import threading

# Definindo o host e a porta do servidor
HOST = '0.0.0.0'
PORT = 5000
# ------------------------------------------------

clientesOnline = []
lock = threading.Lock()

def gerenciarCliente(conexao, endereco):
    print(f'Conectado: {endereco}')
    conexao.sendall('Você conectou ao servidor ⓌⓋⓅ Ⓖⓐⓜⓔⓢ!'.encode('utf-8'))
    
    try:
        modo = conexao.recv(1024).decode('utf-8').strip().lower()

        if not modo:
            conexao.close()
            return
        
        if modo == 'online':
            print(f'{endereco}: Modo Online.')
            conexao.sendall('Modo Online selecionado. Aguardando outro jogador...'.encode('utf-8'))

            with lock:
                clientesOnline.append(conexao)
                if len(clientesOnline) >= 2:
                    jogador1 = clientesOnline.pop(0)
                    jogador2 = clientesOnline.pop(0)
                    jogador1.sendall('Outro jogador conectado! Iniciando jogo...'.encode('utf-8'))
                    jogador2.sendall('Outro jogador conectado! Iniciando jogo...'.encode('utf-8'))
                    iniciarPartida(jogador1, jogador2)

        elif modo == 'maquina':
            print(f'{endereco}: Modo Contra Máquina.')
            conexao.sendall('Modo Contra Máquina selecionado. Iniciando jogo...'.encode('utf-8'))
            conexao.close()
        
        else:
            conexao.sendall('Modo inválido. Conexão encerrada.'.encode('utf-8'))
            conexao.close()
    
    except Exception as e:
        print(f'Erro com {endereco}: {e}')
        conexao.close()

# Criando o socket do servidor e ligando ao host e a porta | Usado modelo TCP
def iniciarServidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f'''Servidor WVP Games Funcionando!\nLocal Servidor: {HOST}\nPorta Servidor: {PORT}
        \nAguardando Cliente...''')
    
    while True:
        conexao, endereco = servidor.accept()
        threadCliente = threading.Thread(target=gerenciarCliente, args=(conexao, endereco))
        threadCliente.start()
# ------------------------------------------------

def iniciarPartida(jogador1, jogador2):

    artes = {
        'pedra': '🪨',
        'papel': '📄',
        'tesoura': '✂️',
        'lagarto': '🦎',
        'spock': '🖖'
    }

    try:
        jogador1.sendall('Iniciando partida! Você é o Jogador 1.'.encode('utf-8'))
        jogador2.sendall('Iniciando partida! Você é o Jogador 2.'.encode('utf-8'))
        jogada1 = jogador1.recv(1024).decode('utf-8').strip().lower()
        jogada2 = jogador2.recv(1024).decode('utf-8').strip().lower()

        print(f"Jogador 1: {jogada1} | Jogador 2: {jogada2}")

        art1 = artes.get(jogada1, '?')
        art2 = artes.get(jogada2, '?')
        duelo = f"Jogador1 {art1} VS {art2} jogador2\n"
        jogador1.sendall(duelo.encode('utf-8'))
        jogador2.sendall(duelo.encode('utf-8'))

        regras = {
            "tesoura": ["papel", "lagarto"],
            "papel": ["pedra", "spock"],
            "pedra": ["tesoura", "lagarto"],
            "lagarto": ["spock", "papel"],
            "spock": ["tesoura", "pedra"]
        }

        if jogada1 == jogada2:
            resultado = f"Empate! Ambos jogaram {jogada1}."
        elif jogada2 in regras.get(jogada1, []):
            resultado = f"Jogador 1 venceu! ({jogada1} vence {jogada2})"
        elif jogada1 in regras.get(jogada2, []):
            resultado = f"Jogador 2 venceu! ({jogada2} vence {jogada1})"
        else:
            resultado = "Jogada inválida detectada. Partida encerrada."

        jogador1.sendall(resultado.encode('utf-8'))
        jogador2.sendall(resultado.encode('utf-8'))

    except Exception as e:
        print(f"Erro durante a partida: {e}")

    finally:
        jogador1.close()
        jogador2.close()


if __name__ == "__main__":
    iniciarServidor()