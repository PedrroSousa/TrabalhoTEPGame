
""" ------------------------------------------------
Servidor.py para o jogo Pedra, Papel, Tesoura, Lagarto e Spock.

Funções:
- Criar conexões TCP com clientes
- Lida com dois modos: Online ou Contra a Máquina (não implementado)
- O servidor coloca jogadores em fila de espera para partidas online
- Gerencia a partida e envia o resultado
------------------------------------------------"""

import socket
import threading

HOST = '0.0.0.0'
PORT = 5000

# Lista para armazenar clientes online esperando por partida -- recebe múltiplas conexões
clientesOnline = []
# lock para sincronização de threads
lock = threading.Lock()

# Função para gerenciar cada cliente conectado -- Threaded para cada cliente
def gerenciarCliente(conexao, endereco):
    print(f'Conectado: {endereco}')
    conexao.sendall('Você conectou ao servidor ⓌⓋⓅ Ⓖⓐⓜⓔⓢ!'.encode('utf-8'))
    
    """
    Lida com um cliente conectado.
    - Parte responsavel pela comunicação inicial com o cliente
    - Recebe modo de jogo (online ou maquina)
    - Se online: coloca cliente na fila e cria uma partida quando houver 2 jogadores
    """

    try:
        # Recebe o modo de jogo do cliente
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

# Criando o socket do servidor e ligando ao host e a porta | Usando modelo TCP
def iniciarServidor():

    """
    Inicia o Servidor TCp e espera por conexões de clientes.
    Cria uma thread para cada cliente conectado para gerenciar a comunicação.
    """
    
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

    """
    Gerencia a partida os jogadores online.
    Recebe nickname e jogada
    Envia animação das jogadas
    Aplica as regras do jogo e determina o vencedor
    Envia o resultado final aos jogadores
    """

    artes = {
        'pedra': '🪨',
        'papel': '📄',
        'tesoura': '✂️',
        'lagarto': '🦎',
        'spock': '🖖'
    }

    try:

        # parte do codigo que comunica com os jogadores o ciclo do jogo e resultados
        jogador1.sendall('Iniciando partida! Você é o Jogador 1.'.encode('utf-8'))
        jogador2.sendall('Iniciando partida! Você é o Jogador 2.'.encode('utf-8'))

        nickName = jogador1.recv(1024).decode('utf-8').strip()
        jogada1 = jogador1.recv(1024).decode('utf-8').strip().lower()

        jogador2.sendall("Aguardando jogador 1...".encode('utf-8'))

        nickName2 = jogador2.recv(1024).decode('utf-8').strip()
        jogada2 = jogador2.recv(1024).decode('utf-8').strip().lower()

        art1 = artes.get(jogada1, '?')
        art2 = artes.get(jogada2, '?')

        print(f"Jogador 1: {jogada1} | Jogador 2: {jogada2}")

        # imprimi os ascii / emojis das jogadas para ambos os jogadores ou ? se inválido
        art1 = artes.get(jogada1, '?')
        art2 = artes.get(jogada2, '?')

        dueloInfo = f"Voce {art1} VS {art2} {nickName2}\n"
        dueloInfo2 = f"{nickName} {art1} VS {art2} Voce\n"
        jogador1.sendall(dueloInfo.encode('utf-8'))
        jogador2.sendall(dueloInfo2.encode('utf-8'))

        # codigo que invoca as regras do jogo para determinar o vencedor
        regras = {
            "tesoura": ["papel", "lagarto"],
            "papel": ["pedra", "spock"],
            "pedra": ["tesoura", "lagarto"],
            "lagarto": ["spock", "papel"],
            "spock": ["tesoura", "pedra"]
        }

        # comparacao de ifs para determinar o vencedor ou empate
        if jogada1 == jogada2:
            resultado = f"Empate! Ambos jogaram {jogada1}."
        elif jogada2 in regras.get(jogada1, []):
            resultado = f"Jogador 1 venceu! ({jogada1} vence {jogada2})"
        elif jogada1 in regras.get(jogada2, []):
            resultado = f"Jogador 2 venceu! ({jogada2} vence {jogada1})"
        else:
            resultado = "Jogada inválida. Partida encerrada."

        jogador1.sendall(resultado.encode('utf-8'))
        jogador2.sendall(resultado.encode('utf-8'))

    except Exception as e:
        print(f"Erro durante a partida: {e}")

    # finaliza as conexões dos jogadores apos a partida
    finally:
        jogador1.close()
        jogador2.close()


if __name__ == "__main__":
    iniciarServidor()