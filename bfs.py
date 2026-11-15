grafo = {}

def add_aresta(vertice1, vertice2, direcionado):
    grafo[vertice1].append(vertice2)
    if direcionado == False:
        grafo[vertice2].append(vertice1)

def add_vertice(vertice):
    grafo[vertice] = []

def deletar_aresta(vertice1, vertice2, direcionado):
    grafo[vertice1].remove(vertice2)
    if not direcionado:
        grafo[vertice2].remove(vertice1)

def deletar_vertice(vertice):
    grafo.pop(vertice)

def mostrar_grafo():
    for i in grafo:
        print(i + ": ", end="")
        for j in grafo[i]:
            print(j + ", ", end="")
        print()

def bfs(vertice_inicial):
    visitados = []
    lista = []

    lista.append(vertice_inicial)

    while len(lista) != 0:
        for i in lista:
            visitados.append(i)
            lista.remove(i)
            for j in grafo[i]:
                if j not in visitados and j not in lista:
                    lista.append(j)

    return visitados

def is_vertice_in_dict(vertice, lista):
    for i in lista:
        if vertice == i["vertice"]:
            return True
    return False

def bfs_shortest_path(vertice_inicial, vertice_final):
    visitados = []
    lista = []

    lista.append({"vertice": vertice_inicial, "caminho": []})

    while len(lista) != 0:
        atual = lista.pop(0)
        atual["caminho"].append(atual["vertice"])
        if atual["vertice"] == vertice_final:
            return atual["caminho"]
            
        visitados.append(atual)

        for j in grafo[atual["vertice"]]:
            if not is_vertice_in_dict(j, visitados) and not is_vertice_in_dict(j, lista):
                lista.append({"vertice": j, "caminho": atual["caminho"] + []}) #python trashiness
    return visitados

if __name__ == "__main__":
    #Guilherme Bertuccini Ribeiro RA: 2029851
    #Ana Julia Custodio           RA: 2037940
    #João Felipe                  RA: 2089420
    #Andreas Guert de Lima        RA: 2086833

    add_vertice("V1")
    add_vertice("V2")
    add_vertice("V3")
    add_vertice("V4")
    add_vertice("V5")
    add_vertice("V6")
    add_vertice("V7")
    add_vertice("V8")

    add_aresta("V1", "V2", False)
    add_aresta("V1", "V3", False)
    add_aresta("V1", "V6", False)
    add_aresta("V2", "V6", False)
    add_aresta("V2", "V3", False)
    add_aresta("V2", "V4", False)
    add_aresta("V2", "V7", False)
    add_aresta("V2", "V4", False)
    add_aresta("V6", "V7", False)
    add_aresta("V6", "V5", False)
    add_aresta("V4", "V5", False)
    add_aresta("V5", "V8", False)
    add_aresta("V8", "V7", False)

    print("Grafo: ")
    mostrar_grafo()
    print()
    print("bfs from V1:", bfs("V1"))
    print()
    print("shortest path from V1 to V8:", bfs_shortest_path("V1", "V8"))