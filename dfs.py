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
    
    for i in grafo:
        if vertice in grafo[i]:
            grafo[i].remove(vertice)

def mostrar_grafo():
    for i in grafo:
        print(i + ": ", end="")
        for j in grafo[i]:
            print(j + ", ", end="")
        print()

def dfs(vertice_inicial):
    visitados = []
    lista = []

    lista.append(vertice_inicial)

    while len(lista) != 0:
        atual = lista.pop()
        
        visitados.append(atual)

        for j in grafo[atual]:
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

def dfs_have_loop(vertice_inicial):
    visitados = []
    lista = []

    lista.append({"vertice": vertice_inicial, "pai": None})

    while len(lista) != 0:
        atual = lista.pop()
            
        visitados.append(atual)

        for j in grafo[atual["vertice"]]:
            if not is_vertice_in_dict(j, visitados):# and not is_vertice_in_dict(j, lista):
                lista.append({"vertice": j, "pai": atual["vertice"]})
            else:
                if j != atual["pai"]:
                    return True
    
    return False

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
    add_vertice("V9")

    add_aresta("V1", "V2", True)
    add_aresta("V1", "V5", True)
    add_aresta("V2", "V4", True)
    add_aresta("V3", "V8", True)
    add_aresta("V3", "V1", True)
    add_aresta("V4", "V5", True)
    add_aresta("V5", "V6", True)
    add_aresta("V5", "V7", True)
    add_aresta("V5", "V3", True)
    add_aresta("V6", "V9", True)
    add_aresta("V7", "V8", True)
    add_aresta("V8", "V9", True)

    print("Grafo: ")
    mostrar_grafo()
    print()
    print("dfs from V1:", dfs("V1"))
    print()
    print("shortest path from V1 to V8:", bfs_shortest_path("V1", "V8"))

    # Graph with loop
    grafo = {}
    add_vertice("V1")
    add_vertice("V2")
    add_vertice("V3")
    add_vertice("V4")
    add_vertice("V5")
    add_vertice("V6")
    add_vertice("V7")
    add_vertice("V8")
    add_vertice("V9")
    
    add_aresta("V1", "V2", False)
    add_aresta("V1", "V5", False)
    add_aresta("V2", "V4", False)
    add_aresta("V3", "V8", False)
    add_aresta("V3", "V1", False)
    add_aresta("V4", "V5", False)
    add_aresta("V5", "V6", False)
    add_aresta("V5", "V7", False)
    add_aresta("V5", "V3", False)
    add_aresta("V6", "V9", False)
    add_aresta("V7", "V8", False)
    add_aresta("V8", "V9", False)

    print()
    print("Is there a loop? (using a graph that has a loop): ", dfs_have_loop("V1"))

    grafo = {}
    # Graph with loop
    add_vertice("V1")
    add_vertice("V2")
    add_vertice("V3")
    add_vertice("V4")
    add_vertice("V5")
    add_vertice("V6")
    add_vertice("V7")
    add_vertice("V8")
    add_vertice("V9")

    add_aresta("V1", "V2", False)
    add_aresta("V2", "V4", False)
    add_aresta("V4", "V5", False)
    add_aresta("V5", "V6", False)
    add_aresta("V5", "V7", False)
    add_aresta("V5", "V3", False)
    add_aresta("V6", "V9", False)
    add_aresta("V8", "V9", False)

    print()
    print("Is there a loop? (using a graph that does not has a loop): ", dfs_have_loop("V1"))