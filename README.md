# Trabalho TEP – Jogo Multiplayer
  _      ___   _____    _____                 
 | | /| / / | / / _ \  / ___/__ ___ _  ___ ___
 | |/ |/ /| |/ / ___/ / (_ / _ `/  ' \/ -_|_-<
 |__/|__/ |___/_/     \___/\_,_/_/_/_/\__/___/
### **Equipe:** Pedro Victor, Victoria Freitas, Wesley Gabriel

## Regras - Jogo: Pedra, Papel, Terousa, Lagarto e Spock ---------------------------------------------------------------------------
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


## Requisitos

- Python 3.x

## Executar

- Para executar o user deve iniciar o servidor com o comando "python Servidor.py" (deve estar no mesmo diretorio do arquivo) usando o terminal
- Fazer a conexão com o Cliente ao Servidor usando o comando "python Cliente.py" (deve estar no mesmo diretorio do arquivo) usando o terminal
- O HOST do Cliente deve estar com o ip da maquina que roda o Servidor e não necessariamente deve estar na mesma maquina, mas na mesma rede

## Funcionamento

- O servidor fica esperando a conexão dos clientes, o cliente ao conectar ao servidor fica esperando jogadores para iniciar uma partida que precisa de dois jogadores
- Pode se conectar multiplos clientes, eles são movidos para uma fila que espera uma partida acabar para criar outra com os jogadores na lista de espera
- cada cliente é colocado em uma thread separada para não interromper ou bloquear as conexões


# Requisitos do Trabalho ----------------------------------------------------------------------------------------------------------

## Arquitetura Cliente-Servidor
- O servidor deve ser capaz de gerenciar múltiplos clientes simultaneamente (mínimo de 2 clientes).
- O servidor é o autoridade do jogo: ele valida todas as jogadas, gerencia o estado global e notifica os clientes.

## Comunicação via Sockets

- Vai ser usado o socket TCP. Justificativa:
- Definição de um protocolo de comunicação entre cliente e servidor, com mensagens bem definidas (ex: JOGADA|x,y, RESULTADO acertou, CHAT|mensagem).

## Funcionalidades Mínimas do Servidor

- Aceitar conexões de clientes.
- Gerenciar o estado do jogo (tabuleiro, placar, rodadas).
- Processar comandos dos clientes e enviar respostas.
- Lidar com desconexões de clientes sem travar.

## Funcionalidades Mínimas do Cliente

- Conectar ao servidor.
- Enviar jogadas/comandos.
- Receber e exibir o estado atual do jogo.
- Interface de usuário (pode ser textual ou gráfica simples).

## Requisitos Bônus (Opcionais) uma ou mais das opções

- Persistência de placares ou histórico de partidas.
- Suporte a salas de jogo (múltiplas partidas simultâneas).
- Interface gráfica (GUI) para o cliente.

### esquema de funcionamento do jogo
- WVP Games, Equipe -> Nome do Jogo -> Menu: jogar, regras, sair -> Online, Maquina, voltar -> gameplay: Digitar NickName e jogada -> historico, sair da sala, jogar novamente, voltar ao menu-> 


