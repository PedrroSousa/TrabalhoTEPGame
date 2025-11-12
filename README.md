# TrabalhoTEPGame

## Arquitetura Cliente-Servidor
### - O servidor deve ser capaz de gerenciar múltiplos clientes simultaneamente (mínimo de 2 clientes).
### - O servidor é o autoridade do jogo: ele valida todas as jogadas, gerencia o estado global e notifica os clientes.

## Comunicação via Sockets

### - Vai ser usado o socket TCP. Justificativa:
### - Definição de um protocolo de comunicação entre cliente e servidor, com mensagens bem definidas (ex: JOGADA|x,y, RESULTADO acertou, CHAT|mensagem).

## Funcionalidades Mínimas do Servidor

### - Aceitar conexões de clientes.
### - Gerenciar o estado do jogo (tabuleiro, placar, rodadas).
### - Processar comandos dos clientes e enviar respostas.
### - Lidar com desconexões de clientes sem travar.

ⓌⓋⓅ Ⓖⓐⓜⓔⓢ

  _      ___   _____    _____                 
 | | /| / / | / / _ \  / ___/__ ___ _  ___ ___
 | |/ |/ /| |/ / ___/ / (_ / _ `/  ' \/ -_|_-<
 |__/|__/ |___/_/     \___/\_,_/_/_/_/\__/___/
                                              

██     ██ ██    ██ ██████       ██████   █████  ███    ███ ███████ ███████ 
██     ██ ██    ██ ██   ██     ██       ██   ██ ████  ████ ██      ██      
██  █  ██ ██    ██ ██████      ██   ███ ███████ ██ ████ ██ █████   ███████ 
██ ███ ██  ██  ██  ██          ██    ██ ██   ██ ██  ██  ██ ██           ██ 
 ███ ███    ████   ██           ██████  ██   ██ ██      ██ ███████ ███████ 
                                                                           
                                                                           
  _      ___   _____       __     __ __         ___   //| __        ____              __  
 | | /| / / | / / _ \  __ / /__  / //_/__ ___  / _ \_|/||/ /  ___ _/ __/__  ___  ____/ /__
 | |/ |/ /| |/ / ___/ / // / _ \/ ,< / -_) _ \/ ___/ _ \/ /__/ _ `/\ \/ _ \/ _ \/ __/  '_/
 |__/|__/ |___/_/     \___/\___/_/|_|\__/_//_/_/   \___/____/\_,_/___/ .__/\___/\__/_/\_\ 
                                                                    /_/       
## Funcionalidades Mínimas do Cliente

### - Conectar ao servidor.
### - Enviar jogadas/comandos.
### - Receber e exibir o estado atual do jogo.
### - Interface de usuário (pode ser textual ou gráfica simples).

## Requisitos Bônus (Opcionais) uma ou mais das opções

### - Persistência de placares ou histórico de partidas.
### - Suporte a salas de jogo (múltiplas partidas simultâneas).
### - Interface gráfica (GUI) para o cliente.

## O jogo se trata de Pedra Papel Tesoura, mas adicionando Lagarto e Spock.


### esquema de funcionamento do jogo

#### Nome -> Empresa (WVP Games) -> Descrição -> Menu: comandos, regras -> salas -> gameplay, pontuação -> historico, sair da sala, jogar novamente, voltar ao menu-> 

#### observação: tratamento de erros, queda de um cliente, regras do que acontece



# Jogo: Pedra, Papel, Terousa, Lagarto e Spock.

## Regras

- ✂️ **Tesoura corta** 📄 **Papel**  
- 📄 **Papel cobre** 🪨 **Pedra**  
- 🪨 **Pedra esmaga** 🦎 **Lagarto**  
- 🦎 **Lagarto envenena** 🖖 **Spock**  
- 🖖 **Spock destrói** ✂️ **Tesoura**  
- ✂️ **Tesoura decapita** 🦎 **Lagarto**  
- 🦎 **Lagarto come** 📄 **Papel**  
- 📄 **Papel refuta** 🖖 **Spock**  
- 🖖 **Spock vaporiza** 🪨 **Pedra**  
- 🪨 **Pedra quebra** ✂️ **Tesoura**