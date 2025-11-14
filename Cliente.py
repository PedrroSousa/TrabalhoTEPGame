
'''
Cliente.py - Cliente do Jogo Pedra, Papel, Tesoura, Lagarto, Spock
Conectar ao servidor via TCP
Enviar modo de jogo selecionado (online ou contra máquina)
Se for partida, enviar nickname e jogada
Gerenciar menus e interações do usuário no terminal
'''

import socket
import time
import os

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

# funcao para limpar a tela do terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# funcao para exibir o logo e a equipe
def exibirLogo():
    clear()
    print(LOGO)
    print("\nEquipe: Wesley Gabriel, Victoria Freitas, Pedro Victor\n")
    time.sleep(2)
    print("\nCarregando", end="")
    for _ in range(4):
        time.sleep(0.6)
        print(".", end="", flush=True)
    print("\n")
    clear()


# funcao para exibir a introducao do jogo com animacao de carregamento
def exibirIntro():
    print(NOMEGAME)
    print("\nCarregando", end="")
    for _ in range(4):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

# funcao para exibir o menu inicial do jogo
def exibirInicio():
    clear()
    print(NOMEGAME)
    print("\nBem-vindo ao Jogo!\n")
    print("1 - Jogar Online")
    print("2 - Jogar Contra Máquina")
    print("3 - Voltar ao Menu")
    return input("Escolha uma opção: ")

# funcao para exibir o menu principal do jogo
def exibirMenuPrincipal():
    print("==== MENU PRINCIPAL ==============================================")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")
    return input("\nEscolha uma opção: ")


# funcao para exibir as regras do jogo para o jogador no terminal
def mostrarRegras():
    exibirIntro()
    print("==== REGRAS DO JOGO ====\n")
    print('''- ✂️ Tesoura corta 📄 Papel - || - 📄 Papel cobre 🪨 Pedra
- 🪨 Pedra esmaga 🦎 Lagarto - || - 🦎 Lagarto envenena 🖖 Spock
- 🖖 Spock destrói ✂️ Tesoura - || - ✂️ Tesoura decapita 🦎 Lagarto
- 🦎 Lagarto come 📄 Papel - || - 📄 Papel refuta 🖖 Spock
- 🖖 Spock vaporiza 🪨 Pedra - || - 🪨 Pedra quebra ✂️ Tesoura\n''')
    input("Pressione Enter para voltar ao menu principal...")
    clear()
    exibirIntro()

# funcao para conectar o cliente ao servidor e gerenciar a comunicacao de entrada/saida
def conectarServidor(modo):
    HOST = 'localhost'
    PORT = 5000

    '''
    Conecta ao servidor e gerencia a comunicação.
    Envia o modo de jogo selecionado (online ou maquina)
    Recebe mensagens do servidor e exibe ao usuário
    Se for partida, envia nickname e jogada
    Aguarda respostas do servidor e exibe resultados
    '''

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORT))
        print(f'Conectado! {HOST}:{PORT}')
        mensagem = cliente.recv(1024).decode('utf-8')
        print(f'Servidor: {mensagem}')
        cliente.sendall(modo.encode('utf-8'))

        while True:
            resposta = cliente.recv(1024).decode('utf-8')
            if not resposta:
                print("Servidor encerrou a conexão.")
                break
            
            

            print(f'Servidor: {resposta}')
            if "Iniciando partida" in resposta:
                clear()
                nickname = input("Digite seu nickname: ").strip()
                cliente.sendall(nickname.encode('utf-8'))
                jogada = input("Digite sua jogada (🪨pedra, 📄papel, ✂️tesoura, 🦎lagarto, 🖖spock): ").strip().lower()
                cliente.sendall(jogada.encode('utf-8'))

    except ConnectionRefusedError:
        print('Erro de conexão com o servidor.')
        time.sleep(2)

    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(2)

# funcao principal que gerencia o fluxo do jogo no cliente e exibe os menus principais e secundarios
def main():
    exibirLogo()
    exibirIntro()

    # loop principal do jogo com menu de opcoes para o jogador
    while True:
        opcao = exibirMenuPrincipal()
        clear()
        if opcao == '1':
            escolha = exibirInicio()
            if escolha == "1":
                conectarServidor("online")
            elif escolha == "2":
                conectarServidor("maquina")
            elif escolha == "3":
                clear()
                exibirIntro()
                continue
            else:
                print("Opção inválida\n")
                time.sleep(1)

        elif opcao == '2':
            mostrarRegras()

        elif opcao == '3':
            print("Saindo do jogo...")
            time.sleep(1)
            break

        else:
            print("Opção inválida")
            time.sleep(1)

# ------------------------------------------------
if __name__ == "__main__":
    main()
