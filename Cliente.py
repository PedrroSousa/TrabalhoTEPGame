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

# function para exibir a tela de início
def exibirIntro():
    print(NOMEGAME)
    print("\nCarregando", end="")
    for _ in range(4):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
# ------------------------------------------------

def exibirInicio():
    clear()
    print(NOMEGAME)
    print("\nBem-vindo ao Jogo!\n")
    print("1 - Jogar Online")
    print("2 - Jogar Contra Máquina")
    print("3 - Voltar ao Menu")
    escolha = input("Escolha uma opção: ")
    return escolha
    time.sleep(1)

# function para exibir o menu principal do jogo
def exibirMenuPrincipal():
    print("==== MENU PRINCIPAL ==============================================")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")
    return input("\nEscolha uma opção: ")
# ------------------------------------------------

# function para exibir o menu de modos de jogo
def exibirMenuJogo():
    clear()
    print("==== MODO DE JOGO ===============================================")
    print("1 - Jogar Online")
    print("2 - Jogar Contra Máquina")
    print("3 - Voltar")
    return input("\nEscolha uma opção: ")
# ------------------------------------------------

# function para exibir as regras do jogo
def mostrarRegras():
    exibirIntro()
    print("==== REGRAS DO JOGO ====\n")
    print('''- ✂️Tesoura corta 📄Papel - || - 📄Papel cobre 🪨Pedra**\n
          - 🪨Pedra esmaga 🦎Lagarto - || - 🦎Lagarto envenena 🖖Spock\n
          - 🖖Spock destrói ✂️Tesoura - || - ✂️Tesoura decapita 🦎Lagarto\n
          - 🦎Lagarto come 📄Papel - || - 📄Papel refuta 🖖Spock\n
          - 🖖Spock vaporiza 🪨Pedra - || - 🪨Pedra quebra ✂️Tesoura\n''')
    input("Pressione Enter para voltar ao menu principal...")
    clear()
    exibirIntro()
# ------------------------------------------------

# function para limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# ------------------------------------------------

# Função principal do jogo
def main():
    exibirLogo()
    exibirIntro()
    while True:
        opcao = exibirMenuPrincipal()
        clear()
        if opcao == '1':
            escolha = exibirInicio()
            if escolha == "1":
                conectarServidor()
                print("Jogar Online - Em desenvolvimento")
            elif escolha == "2":
                print("Jogar Contra Máquina - Em desenvolvimento")
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




            
                
def conectarServidor():
    HOST = 'localhost'
    PORT = 5000

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORT))
        print(f'Conectado!{HOST}:{PORT}')

        mensagem = cliente.recv(1024).decode('utf-8')
        print(f'Servidor: {mensagem}')
        cliente.sendall('Cliente conectado!'.encode('utf-8'))
        cliente.close()
    
    except ConnectionRefusedError:
        print('Erro de conexão servidor.')
        time.sleep(2)

if __name__ == "__main__":
    main()