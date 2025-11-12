# TrabalhoTEPGame

## Arquitetura Cliente-Servidor
### ● O servidor deve ser capaz de gerenciar múltiplos clientes simultaneamente (mínimo de 2 clientes).
### ● O servidor é o autoridade do jogo: ele valida todas as jogadas, gerencia o estado global e notifica os clientes.

## Comunicação via Sockets

### ● Uso de sockets TCP ou UDP, justificando a escolha.
### ● Definição de um protocolo de comunicação entre cliente e servidor, com mensagens bem definidas (ex: JOGADA|x,y, RESULTADO acertou, CHAT|mensagem).

## Funcionalidades Mínimas do Servidor

### ● Aceitar conexões de clientes.
### ● Gerenciar o estado do jogo (tabuleiro, placar, rodadas).
### ● Processar comandos dos clientes e enviar respostas.
### ● Lidar com desconexões de clientes sem travar.

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