import sys

jogos = []

seqJogo = 0

#Declaração da classe de Jogo com o atributo de sequencia e placar
class jogo:
    def __init__(self, seqjogo, placar):
        self.seqjogo = seqjogo
        self.placar = placar

# Método para incluir um novo Jogo na lista de jogos
def incluirplacar():
    global seqJogo
    seqJogo += 1
    placar = int(input("Informe o placar \n"))
    jogos.append(jogo(seqJogo, placar))
    menu()

#Método que realiza o cálculo de records minimos e máximos e qtd de quebra de records e exibe em tela
def mostrarplacar():
    min = 0
    max = 0
    qtdMin = 0
    qtdMax = 0
    contador = 0
    for obj in jogos:
        if contador == 0:
            min = obj.placar
            max = obj.placar
            contador += 1
        else:
            if obj.placar > max:
                max = obj.placar
                qtdMax += 1
            elif obj.placar < min:
                min = obj.placar
                qtdMin =+ 1
        print("Jogo --- Placar --- Minímo --- Máximo --- Qtd Record Minimo --- Qtd Record Máximo")
        print(str(obj.seqjogo) + " -------- " + str(obj.placar) + " ------- " + str(min) + " ------- " + str(max) + " ------------- " + str(qtdMin) + " ----------------- " + str(qtdMax))
    menu()

# Método do Menu do sistema com as opções para o usuário
def menu():
    opcao = int(input("0 - Sair, 1 - Informar Placar, 2 - Ver tabela\n"));
    if opcao == 0:
        sys.exit()
    elif opcao == 1:
        incluirplacar()
        menu()
    elif opcao == 2:
        mostrarplacar()
        menu()

if __name__ == '__main__':
    menu()
1