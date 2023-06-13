from uteis.funcoesGerais import valorInvalido, validaPatinhos

print("Vamos cantar!")

patinhos: int = -1  # Forçar o número a entrar na repetição de teste de código#

while patinhos <= 0:  # função tentativa iniciada com números negativos#
    try:
        patinhos = int(input("Escolha a quantidade de patinhos que foram passear: "))
        if patinhos <= 0:
            valorInvalido()
    except ValueError:  # em caso de valor não permitido, como string, é exibida uma mensagem de erro e ele retorna a pedir a
         # inserção do valor#
        patinhos = -1
        valorInvalido()
    except:
        print("Erro desconhecido.")

contador = patinhos

while contador >= 0:  # estrutura de loop criada para reproduzir a música#
    contador = validaPatinhos(contador, patinhos)
