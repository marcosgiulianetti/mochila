from random import randint
from copy import deepcopy
from classes import Pilha

def SolucaoInicial(max, precos):
    tot = int(0)
    pilha = Pilha()

    lista = list(range(10))
    for i in lista:
        lista[i] = int(0)

    while(tot <= max):
        temp = randint(0,9)

        if(tot + precos[temp] <= max):
            pilha.Push(temp)
            tot += precos[temp]
        else:
            break

    # Retira os elementos da pilha e adiciona à lista
    for i in range(0, pilha.Size()):
        temp = pilha.Pop()
        lista[temp] += 1

    # Mostra quais compras foram realizadas. A quantidade de compras de cada produto
    while i < 10:
        if (lista[i] != 0):
            if (lista[i] > 1):
                print(lista[i], "compras do produto", i)
            else:
                print(lista[i], "compra do produto", i)
        i += 1

    return lista

def Sucessor(max, lista, precos):

    # A variavel tot se refere à soma dos produtos comprados
    tot = ValorCompra(lista, precos)

    # Declara a variavel melhor
    melhor = deepcopy(lista)

    # Checa se o produto foi comprado (!= 0) ou não (== 0) para gerar outra compra aleatória
    while True:
        temp = randint(0,9)
        if melhor[temp] != 0:
            break

    # Declara o valor de i para o laço while
    i = int(0)

    # Gera 10 compras aleatorias em busca de encontrar uma solução melhor
    while i < 10:
        # Variavel auxiliar que assume o mesmo valor que o array lista
        aux = deepcopy(lista)
        # "Desfaz" a compra do produto no índice temp para realizar outra compra aleatória
        aux[temp] -= 1
        # Atribui o valor da compra atual para vaux
        vaux = ValorCompra(aux, precos)

        # Enquanto o valor da nova compra for menor que o valor máximo
        while vaux <= max:
            # Gera um valor aleatório para servir como índice do array (produto do super mercado)
            temp = randint(0,9)
            # Realiza uma compra do produto no índice temp
            aux[temp] += 1
            # Faz o calculo do valor total da compra
            vaux = ValorCompra(aux, precos)

        # "Dezfaz" a compra do produto no indice temp para repetir o laço while caso necessário
        aux[temp] -= 1

        # Calcula o valor da compra em vaux (Valor auxiliar)
        vaux = ValorCompra(aux, precos)

        # Checa se o valor do auxiliar é maior que o total, para ver se a compra foi otimizada
        if vaux > tot:
            # O Total agora assume o valor de vaux, pois a compra foi otimizada
            tot = vaux
            # Existe uma configuração de compra melhor, logo minha variavel melhor recebe aux
            melhor = aux

        # Soma 1 ao laço de repetição
        i += 1

    return melhor

def ValorCompra(lista, precos):

    tot = int(0)
    i = int(0)

    while(i < 10):
        tot = (lista[i]*precos[i]) + tot

        i += 1

    return tot

def GerarPrioridade():
    lista = list(range(10))

    for i in lista:
        lista[i] = randint(1,3)

    return lista

def GerarPrecos():
    lista = list(range(10))

    for i in lista:
        lista[i] = randint(1,9)

    return lista

# Main
if __name__ == '__main__':

    prioridade = GerarPrioridade()
    precos = GerarPrecos()

    max = int(input("Informe o seu saldo: "))

    lista = SolucaoInicial(max,precos)
    print(precos,"- Precos")
    print(prioridade, "- Prioridade")
    print(lista, "- Solução inicial", "- Valor:",ValorCompra(lista,precos))
    lista = Sucessor(max, lista, precos)
    print(lista, "- Sucessor", "- Valor:",ValorCompra(lista,precos))