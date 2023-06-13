import emoji
import time

def valorInvalido():
    print("Valor inválido. Digite um número inteiro positivo!")

def separaEstrofe(valor:int):
    print("\n" + "="*8)
    print(emoji.emojize(':duck:'*valor))
    print("="*8)

def slowprint(texto, atraso=0.1):
    for c in texto:
        print(c,end='',flush=True)
        time.sleep(atraso)

def validaPatinhos(contador:int, patinhos:int):
    if contador > 2: #letra normal, plural#
        separaEstrofe(contador)
        slowprint(f"""{contador} patinhos 
foram passear
Além das montanhas
Para brincar
A mamãe gritou
Quá, quá, quá, quá
Mas só {contador-1} patinhos voltaram de lá.""")
    
    elif contador == 2: #ajuste gramatical ao final#
        separaEstrofe(contador)
        slowprint(f"""{contador} patinhos 
foram passear
Além das montanhas
Para brincar
A mamãe gritou
Quá, quá, quá, quá
Mas só {contador-1} patinho voltou de lá.""")
       
    
    elif contador == 1: #ajuste gramatical em toda a estrofe#
        separaEstrofe(contador)
        slowprint(f"""{contador} patinho 
foi passear
Além das montanhas
Para brincar
A mamãe gritou
Quá, quá, quá, quá
Mas nenhum patinho voltou de lá.""")
        
    else: #resultado final quando não houverem mais patinhos#
        separaEstrofe(contador)
        slowprint(f"""A mamãe patinha foi procurar
Além das montanhas 
Na beira mar
A mamãe gritou
Quá, quá, quá, quá
E os {patinhos} voltaram de lá.""")
        separaEstrofe(patinhos)
        print("Foi um prazer cantar com você!")  
    return contador - 1
