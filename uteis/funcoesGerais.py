def valorInvalido():
    print("Valor inválido. Digite um número inteiro positivo!")

def separaEstrofe():
    print("=" * 15)

def validaPatinhos(contador:int, patinhos:int):
    if contador > 2: #letra normal, plural#
        print(f"""{contador} patinhos 
foram passear
Além das montanhas
Para brincar
A mamãe gritou
Quá, quá, quá, quá
Mas só {contador-1} patinhos voltaram de lá.""")
        separaEstrofe();
    
    elif contador == 2: #ajuste gramatical ao final#
        print(f"""{contador} patinhos 
foram passear
Além das montanhas
Para brincar
A mamãe gritou
Quá, quá, quá, quá
Mas só {contador-1} patinho voltou de lá.""")
        separaEstrofe();
    
    elif contador == 1: #ajuste gramatical em toda a estrofe#
        print(f"""{contador} patinho 
foi passear
Além das montanhas
Para brincar
A mamãe gritou
Quá, quá, quá, quá
Mas nenhum patinho voltou de lá.""")
        separaEstrofe();
    
    else: #resultado final quando não houverem mais patinhos#
        print(f"""A mamãe patinha foi procurar
Além das montnhas 
Na beira mar
A mamãe gritou
Quá, quá, quá, quá
E os {patinhos} voltaram de lá.""")
        separaEstrofe();
        print("Foi um prazer cantar com você!")
        separaEstrofe();
    return contador - 1
