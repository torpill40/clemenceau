from collections import deque
from typing import Union

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from random import randrange


class Graph:
    __slots__ = ['__width', '__height', '__graph']

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__graph = {i: [] for i in range(self.__width * self.__height)}

    def __call__(self, *args, **kwargs):
        return self.__graph

    def __getitem__(self, item):
        return self.__graph[item]

    def __iadd__(self, edge: tuple):
        if edge[1] not in self.__graph[edge[0]]:
            self.__graph[edge[0]].append(edge[1])
            self.__graph[edge[1]].append(edge[0])
        return self

    def width(self):
        return self.__width

    def height(self):
        return self.__height


def hsv_color(hue, sat, val):
    c = val * sat
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = val - c
    r, g, b = 0, 0, 0
    if 0 <= hue < 60:
        r, g, b = c, x, 0
    elif 60 <= hue < 120:
        r, g, b = x, c, 0
    elif 120 <= hue < 180:
        r, g, b = 0, c, x
    elif 180 <= hue < 240:
        r, g, b = 0, x, c
    elif 240 <= hue < 300:
        r, g, b = x, 0, c
    elif 300 <= hue < 360:
        r, g, b = c, 0, x
    return f"#{int((r + m) * 0xFF):02X}{int((g + m) * 0xFF):02X}{int((b + m) * 0xFF):02X}"


def dessiner(graph: Graph):
    w = graph.width()
    h = graph.height()
    position = {h * x + y: (x, y) for y in range(h) for x in range(w)}
    plt.axis('equal')
    nx.draw(nx.Graph(graph()), pos=position, with_labels=False, node_shape='s', node_color='k', edgecolors='k',
            node_size=100, width=7, linewidths=0)
    plt.show()


def animer(graph: Graph, parcours):
    w = graph.width()
    h = graph.height()
    position = {h * x + y: (x, y) for y in range(h) for x in range(w)}
    nxG = nx.Graph(graph())
    E = [e for e in nxG.edges()]

    fig = plt.figure(figsize=(14, 8))

    def numerotation(G):
        dico = {}
        L = list(G.keys())
        for i in range(len(L)):
            dico[L[i]] = i
        return dico

    num = numerotation(graph())
    colmap = ['w' for _ in graph()]
    edgecolmap = ['w' for _ in E]

    def animate(frame):
        nonlocal colmap, edgecolmap
        fig.clear()
        plt.axes([0, 0, 1, 1])
        plt.axis('equal')
        if frame == 0:
            colmap = ['k' for _ in graph()]
            edgecolmap = ['k' for _ in E]
        else:
            u, v, c = parcours[frame - 1]
            hsv = hsv_color(c % 360, .5, 1.)
            colmap[num[v]] = hsv
            if (u, v) in E:
                edgecolmap[E.index((u, v))] = hsv
            elif (v, u) in E:
                edgecolmap[E.index((v, u))] = hsv
        nx.draw(nxG, pos=position, with_labels=False, node_shape='s', edge_color=edgecolmap, node_color=colmap,
                edgecolors='k', node_size=100, width=7, linewidths=0)

    _ = ani.FuncAnimation(fig, animate, frames=len(parcours) + 1, interval=50, repeat=False)
    plt.show()


def classic(graph: Graph, p, q):
    w = graph.width()
    h = graph.height()
    for y in range(h - 1):
        for x in range(w):
            if randrange(p) < q:
                graph += (h * x + y, h * x + y + 1)
    for y in range(h):
        for x in range(w - 1):
            if randrange(p) < q:
                graph += (h * x + y, h * x + y + h)
    # for i in graph():
    #     graph[i].sort()


def maze(graph: Graph, c: int = 0):
    """
    Créer un labyrinthe à partir d'un graphe modifié sur place avec un maximum de n cycles.

    :param graph: graphe modifié sur place
    :param c: nombre maximal de cycles
    """
    couleur = {v: 'w' for v in graph()}
    w = graph.width()
    h = graph.height()
    x = randrange(0, w)
    y = randrange(0, h)
    reste = [x * h + y]
    couleur[x * h + y] = 'g'
    while len(reste) > 0:
        s = reste[-1]
        y = s % h
        x = s // h
        right = y < h - 1 and couleur[x * h + y + 1] == 'w'
        left = y > 0 and couleur[x * h + y - 1] == 'w'
        up = x > 0 and couleur[x * h + y - h] == 'w'
        down = x < w - 1 and couleur[x * h + y + h] == 'w'
        if not (right or left or up or down):
            couleur[x * h + y] = 'k'
            reste.pop()
        else:
            flag = True
            while flag:
                dir_ = randrange(0, 4)
                if dir_ == 0 and right:
                    reste.append(x * h + y + 1)
                    graph += (x * h + y, x * h + y + 1)
                    couleur[x * h + y + 1] = 'g'
                    flag = False
                elif dir_ == 1 and left:
                    reste.append(x * h + y - 1)
                    graph += (x * h + y, x * h + y - 1)
                    couleur[x * h + y - 1] = 'g'
                    flag = False
                if dir_ == 2 and up:
                    reste.append(x * h + y - h)
                    graph += (x * h + y, x * h + y - h)
                    couleur[x * h + y - h] = 'g'
                    flag = False
                if dir_ == 3 and down:
                    reste.append(x * h + y + h)
                    graph += (x * h + y, x * h + y + h)
                    couleur[x * h + y + h] = 'g'
                    flag = False
    for _ in range(c):
        x = randrange(0, w - 1)
        y = randrange(0, h - 1)
        dir_ = randrange(0, 2)
        s1 = x * h + y
        s2 = s1 + dir_ * (h - 1) + 1
        if s1 in graph[s2]:
            s2 = s1 + dir_ * (1 - h) + h
        graph += (s1, s2)


def bfs(G, s, couleur, reponse):
    file = deque()
    couleur['s'] = 'g'
    file.append((s, s, 0))
    while len(file) > 0:
        u, v, teinte = file.popleft()
        if couleur[v] != 'k':
            couleur[v] = 'k'
            reponse.append((u, v, teinte))
            teinte += 0.5
            for w in G[v]:
                if couleur[w] != 'k':
                    couleur[w] = 'g'
                    file.append((v, w, teinte))


def dfs(G, s, couleur, reponse):
    pile = deque()
    couleur['s'] = 'g'
    pile.append((s, s, 0))
    while len(pile) > 0:
        u, v, teinte = pile.pop()
        if couleur[v] != 'k':
            couleur[v] = 'k'
            reponse.append((u, v, teinte))
            teinte += 0.5
            for w in G[v]:
                if couleur[w] != 'k':
                    couleur[w] = 'g'
                    pile.append((v, w, teinte))


def parcours(graph: Graph, parcours_depuis_sommet):
    couleur = {v: 'w' for v in graph()}
    reponse = []
    for s in graph():
        if couleur[s] != 'k':
            parcours_depuis_sommet(graph(), s, couleur, reponse)
    return reponse


def main():
    # G1 = Graph(15, 6)
    # maze(G1, 3)
    # dessiner(G1)
    # animer(G1, parcours(G1, bfs))
    G2 = Graph(40, 30)
    maze(G2)
    animer(G2, parcours(G2, bfs))
    # G3 = Graph(20, 10)
    # classic(G3, 5, 3)
    # dessiner(G3)
    # animer(G3, parcours(G3, bfs))


if __name__ == '__main__':
    main()
