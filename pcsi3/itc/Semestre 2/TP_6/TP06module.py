import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from random import randrange

def dessiner(G):
    position = None
    if G in [G1,G2,G3]:
        position = nx.circular_layout(G)
    elif G in [G4,G5]:
        n=4
        pos1={n*y+x:(x,y) for x in range(n) for y in range(n)}
        pos2={n*y+x+n*n:(x+n+1,y) for x in range(n) for y in range(n)}
        position={**pos1,**pos2}
    elif G in [G6]:
        n = 9
        pos1 = {n * y + x: (x, y) for x in range(n) for y in range(n)}
        pos2 = {n * y + x + n * n: (x + n + 1, y) for x in range(n) for y in range(n)}
        position = {**pos1, **pos2}
    plt.axis('equal')
    nxG=nx.Graph(G)
    nx.draw(nxG, pos=position, with_labels=True, node_color='white', edgecolors='black', node_size=400)
    plt.show()

def creerG1():
    a,b,c,d,e,f = 'a', 'b', 'c', 'd', 'e', 'f'
    return {a:[b,f], b:[a,c], c:[b,d,e,f], d:[c,e], e:[c,d,f], f:[a,c,e]}
G1 = creerG1()

def creerG2():
    a,b,c,d,e,f = 'g', 'h', 'i', 'j', 'k', 'l'
    return {a:[b,f], b:[a], c:[d,f], d:[c,e], e:[d], f:[a,c]}
G2 = creerG2()

G3 = {**G1, **G2}

def creerG(n,p,q):
    dico = {i:[] for i in range(2*n*n)}
    for x in range(n-1):
        for y in range(n):
            if randrange(p) < q:
                dico[n*y+x].append(n*y+x+1)
                dico[n*y+x+1].append(n*y+x)
    for x in range(n):
        for y in range(n-1):
            if randrange(p) < q:
                dico[n*y+x].append(n*y+x+n)
                dico[n*y+x+n].append(n*y+x)
    for x in range(n-1):
        for y in range(n):
            if randrange(p) < q:
                dico[n*y+x+n*n].append(n*y+x+1+n*n)
                dico[n*y+x+1+n*n].append(n*y+x+n*n)
    for x in range(n):
        for y in range(n-1):
            if randrange(p) < q:
                dico[n*y+x+n*n].append(n*y+x+n+n*n)
                dico[n*y+x+n+n*n].append(n*y+x+n*n)
    for i in dico:
        dico[i].sort()
    return dico
G4 = creerG(4,1,1)

G5 = creerG(4,3,2)

G6 = creerG(9,5,3)

def animer(G,parcours):
    fig = plt.figure()
    plt.axis('equal')
    nxG=nx.Graph(G)

    position = None
    if G in [G1,G2,G3]:
        position = nx.circular_layout(G)
    elif G in [G4,G5]:
        n=4
        pos1={n*y+x:(x,y) for x in range(n) for y in range(n)}
        pos2={n*y+x+n*n:(x+n+1,y) for x in range(n) for y in range(n)}
        position={**pos1,**pos2}
    elif G in [G6]:
        n=9
        pos1={n*y+x:(x,y) for x in range(n) for y in range(n)}
        pos2={n*y+x+n*n:(x+n+1,y) for x in range(n) for y in range(n)}
        position={**pos1,**pos2}

    def numerotation(G):
        dico = {}
        L = list(G.keys())
        for i in range(len(L)):
            dico[L[i]] = i
        return dico

    num = numerotation(G)
    colmap=['white' for v in G]

    def animate(frame):
        nonlocal colmap,position
        fig.clear()
        plt.axis('equal')
        if frame == 0:
            colmap=['white' for v in G]
        else:
            colmap[num[parcours[frame-1]]] = 'black'
        nx.draw(nxG, pos=position, with_labels=True, node_color=colmap, edgecolors='black', node_size=400)
    anime = ani.FuncAnimation(fig, animate, frames=len(parcours)+1, interval=300, repeat=False)
    plt.show()

