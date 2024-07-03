'''
Construir uma máquina de Turing decisora capaz de reconhecer palavras perten centes à linguagem
x#y, em que x e y são números denotados na linguagem unária com símbolos.
I. A máquina, além de reconhecer as palavras da linguagem especificada, deve imprimir, ao final
da entrada, o resultado de x mod y e a palavra “ACEITA’. Quando não for possível, deve escrever
apenas a palavra “REJEITA”.
Comece a resolver o projeto construindo esta máquina de Turing no JFLAP. O passo seguinte
é converter esta máquina de Turing para a linguagem de programação Python, considerando uma
string como entrada e produzindo uma string na saída, com a impressão da saída na fita e mais a
palavra “ACEITA” ou “REJEITA”, indicando o estado final da máquina.
Considerando a fidelidade ao simular máquinas de Turing, não faça uso de tipos numéricos na sua
linguagem de programação. Aqueles que procederem diferente desta especificação terão pontuação
cortada pela metade. Lembre-se que o objetivo é fazer uma máquina de Turing para o problema em
questão.
'''
# Ana Beatriz Maciel Nunes        Matrícula: 2312030085
# Fernando Luiz Da Silva Freire   Matrícula: 2315310007

def entrada():
    return input()

def saida(resultado):
    print(resultado)

def manipular_fita(fita):
    # Estados
    q0 = "q0"
    q1 = "q1"
    q2 = "q2"
    q3 = "q3"
    qf = "qf"  # Estado de aceitação
    qr = "qr"  # Estado de rejeição

    # Símbolos da fita
    i = "I"
    espaco = " "
    sharp = "#"
    fim_fita = "\0"

    fita_trabalho = list(fita) + [fim_fita]
    posicao_cabecote = 0
    estado_atual = q0
    # Contadores para x e y
    contador_x = 0
    contador_y = 0

    while True:
        # Símbolo lido na fita
        simbolo_lido = fita_trabalho[posicao_cabecote]

        # Transições
        if estado_atual == q0:
            if simbolo_lido == i:
                posicao_cabecote += 1
                contador_x += 1
            elif simbolo_lido == sharp:
                posicao_cabecote += 1
                estado_atual = q2
            else:
                estado_atual = qr
        elif estado_atual == q2:
            if simbolo_lido == i:
                posicao_cabecote += 1
                contador_y += 1
                estado_atual = q3
            else:
                estado_atual = qr
        elif estado_atual == q3:
            if simbolo_lido == i:
                posicao_cabecote += 1
                contador_y += 1
            elif simbolo_lido == fim_fita:
                estado_atual = qf
            else:
                estado_atual = qr

        if estado_atual == qr or estado_atual == qf:
            break

    if estado_atual == qf and contador_y > 0:
        valor_mod = contador_x % contador_y
        return f"{fita}={i * valor_mod} ACEITA"
    elif estado_atual == qr:
        return f"{fita} REJEITA"
    else:
        return "Erro: estado final inválido"

def maquina_turing():
    fita = entrada()
    resultado = manipular_fita(fita)
    saida(resultado)

if __name__ == "__main__":
    maquina_turing()
