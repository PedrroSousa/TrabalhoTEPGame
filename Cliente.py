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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def exibirIntro():
    print(NOMEGAME)
    print("\nCarregando", end="")
    for _ in range(4):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def exibirInicio():
    clear()
    print(NOMEGAME)
    print("\nBem-vindo ao Jogo!\n")
    print("1 - Jogar Online")
    print("2 - Jogar Contra Máquina")
    print("3 - Voltar ao Menu")
    return input("Escolha uma opção: ")

def exibirMenuPrincipal():
    print("==== MENU PRINCIPAL ==============================================")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")
    return input("\nEscolha uma opção: ")

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

# ------------------------------------------------
def conectarServidor(modo):
    HOST = 'localhost'
    PORT = 5000

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
                jogada = input("Digite sua jogada (🪨pedra, 📄papel, ✂️tesoura, 🦎lagarto, 🖖spock): ").strip().lower()
                cliente.sendall(jogada.encode('utf-8'))

    except ConnectionRefusedError:
        print('Erro de conexão com o servidor.')
        time.sleep(2)

    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(2)

# ------------------------------------------------
def main():
    exibirLogo()
    exibirIntro()
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
