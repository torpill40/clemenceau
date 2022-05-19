from collections import deque
from typing import Union

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from random import randrange


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


def dessiner(G):
    w, h = G['dim']
    position = {w * x + y: (x, y) for y in range(w) for x in range(h)}
    plt.axis('equal')
    nx.draw(nx.Graph(G['G']), pos=position, with_labels=False, node_shape='s', node_color='w', edgecolors='k', node_size=100)
    plt.show()


def animer(G, parcours):
    fig = plt.figure()
    plt.axis('equal')
    graph = G['G']
    nxG = nx.Graph(graph)
    w, h = G['dim']
    position = {w * x + y: (x, y) for y in range(w) for x in range(h)}

    def numerotation(G):
        dico = {}
        L = list(G.keys())
        for i in range(len(L)):
            dico[L[i]] = i
        return dico

    num = numerotation(graph)
    colmap = ['w' for _ in graph]

    def animate(frame):
        nonlocal colmap
        fig.clear()
        plt.axis('equal')
        if frame == 0:
            colmap = ['w' for _ in graph]
        else:
            colmap[num[parcours[frame - 1][0]]] = hsv_color(parcours[frame - 1][1] % 360, .5, 1.)
        nx.draw(nxG, pos=position, with_labels=False, node_shape='s', node_color=colmap, edgecolors='k', node_size=100)

    _ = ani.FuncAnimation(fig, animate, frames=len(parcours) + 1, interval=50, repeat=False)
    plt.show()


def creerG(w, h, p, q):
    dico = {i: [] for i in range(h * w)}
    for y in range(h - 1):
        for x in range(w):
            if randrange(p) < q:
                dico[h * x + y].append(h * x + y + 1)
                dico[h * x + y + 1].append(h * x + y)
    for y in range(h):
        for x in range(w - 1):
            if randrange(p) < q:
                dico[h * x + y].append(h * x + y + h)
                dico[h * x + y + h].append(h * x + y)
    for i in dico:
        dico[i].sort()
    return {'dim': (h, w), 'G': dico}


def maze(w: int, h: int, c: int = 0) -> dict[str, Union[tuple[int, int], dict[int, list[int]]]]:
    """
    Créer un labyrinthe à h lignes et w colonnes avec un maximum de n cycles.

    :param w: largeur du labyrinthe
    :param h: hauteur du labyrinthe
    :param c: nombre maximal de cycles
    :return: graphe du labyrinthe
    """
    dico = {i: [] for i in range(w * h)}
    couleur = {v: 'w' for v in range(w * h)}
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
                    dico[x * h + y].append(x * h + y + 1)
                    dico[x * h + y + 1].append(x * h + y)
                    couleur[x * h + y + 1] = 'g'
                    flag = False
                elif dir_ == 1 and left:
                    reste.append(x * h + y - 1)
                    dico[x * h + y].append(x * h + y - 1)
                    dico[x * h + y - 1].append(x * h + y)
                    couleur[x * h + y - 1] = 'g'
                    flag = False
                if dir_ == 2 and up:
                    reste.append(x * h + y - h)
                    dico[x * h + y].append(x * h + y - h)
                    dico[x * h + y - h].append(x * h + y)
                    couleur[x * h + y - h] = 'g'
                    flag = False
                if dir_ == 3 and down:
                    reste.append(x * h + y + h)
                    dico[x * h + y].append(x * h + y + h)
                    dico[x * h + y + h].append(x * h + y)
                    couleur[x * h + y + h] = 'g'
                    flag = False
    for _ in range(c):
        x = randrange(0, w - 1)
        y = randrange(0, h - 1)
        dir_ = randrange(0, 2)
        s1 = x * h + y
        s2 = s1 + dir_ * (h - 1) + 1
        if s1 in dico[s2]:
            s2 = s1 + dir_ * (1 - h) + h
        if s1 not in dico[s2]:
            dico[s1].append(s2)
            dico[s2].append(s1)
    return {'dim': (h, w), 'G': dico}


def bfs(G, s, couleur, reponse):
    file = deque()
    couleur['s'] = 'g'
    file.append((s, 0))
    while len(file) > 0:
        v, teinte = file.popleft()
        if couleur[v] != 'k':
            couleur[v] = 'k'
            reponse.append((v, teinte))
            teinte += 1
            for w in G[v]:
                if couleur[w] != 'k':
                    couleur[w] = 'g'
                    file.append((w, teinte))


def dfs(G, s, couleur, reponse):
    pile = deque()
    couleur['s'] = 'g'
    pile.append((s, 0))
    while len(pile) > 0:
        v, teinte = pile.pop()
        if couleur[v] != 'k':
            couleur[v] = 'k'
            reponse.append((v, teinte))
            teinte += 1
            for w in G[v]:
                if couleur[w] != 'k':
                    couleur[w] = 'g'
                    pile.append((w, teinte))


def parcours(G, parcours_depuis_sommet):
    couleur = {v: 'w' for v in G}
    reponse = []
    for s in G:
        if couleur[s] != 'k':
            parcours_depuis_sommet(G, s, couleur, reponse)
    return reponse


def main():
    G1 = creerG(15, 6, 5, 3)
    G2 = maze(60, 30)
    G3 = maze(60, 30, 50)
    # dessiner(G3)
    animer(G3, parcours(G3['G'], bfs))


if __name__ == '__main__':
    main()
