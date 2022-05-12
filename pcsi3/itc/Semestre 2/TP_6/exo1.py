from TP06module import *
from collections import deque

# dessiner(G4)


def bfs(G, s, couleur, reponse):
    file = deque()
    couleur['s'] = 'gris'
    file.append(s)
    while len(file) > 0:
        v = file.popleft()
        if couleur[v] != 'noir':
            couleur[v] = 'noir'
            reponse.append(v)
            for w in G[v]:
                if couleur[w] != 'noir':
                    couleur[w] = 'gris'
                    file.append(w)


# couleur = {v: 'blanc' for v in G3}
# reponse = []
# bfs(G3, 'a', couleur, reponse)
# if reponse == ['a', 'b', 'f', 'c', 'e', 'd']:
#     print('fonction bfs validée')


def parcours(G, parcours_depuis_sommet):
    couleur = {v: 'blanc' for v in G}
    reponse = []
    for s in G:
        if couleur[s] != 'noir':
            parcours_depuis_sommet(G, s, couleur, reponse)
    return reponse


# if parcours(G3, bfs) == ['a', 'b', 'f', 'c', 'e', 'd',
# 'g', 'h', 'l', 'i', 'j', 'k']:
#     print('fonction parcours validée')


# animer(G4, parcours(G4, bfs))
# animer(G5, parcours(G5, bfs))


def dfs(G, s, couleur, reponse):
    pile = []
    couleur['s'] = 'gris'
    pile.append(s)
    while len(pile) > 0:
        v = pile.pop()
        if couleur[v] != 'noir':
            couleur[v] = 'noir'
            reponse.append(v)
            for w in G[v]:
                if couleur[w] != 'noir':
                    couleur[w] = 'gris'
                    pile.append(w)


# if parcours(G3, dfs) == ['a', 'f', 'e', 'd', 'c', 'b',
# 'g', 'l', 'i', 'j', 'k', 'h']:
#     print('fonction dfs validée')

# animer(G4, parcours(G4, dfs))


def dfs_rec(G, s, couleur, reponse):
    couleur[s] = 'noir'
    reponse.append(s)
    for w in G[s]:
        if couleur[w] != 'noir':
            dfs_rec(G, w, couleur, reponse)


# if parcours(G3, dfs_rec) == ['a', 'b', 'c', 'd', 'e', 'f',
# 'g', 'h', 'l', 'i', 'j', 'k']:
#     print('fonction dfs_rec validée')

# animer(G4, parcours(G4, dfs_rec))


def est_connexe(G):
    couleur = {v: 'blanc' for v in G}
    reponse = []
    for s in G:
        if couleur[s] != 'noir':
            bfs(G, s, couleur, reponse)
            break
    for s in G:
        if couleur[s] != 'noir':
            return False
    return True


# assert est_connexe(G1)
# assert est_connexe(G2)
# assert not est_connexe(G3)
# assert not est_connexe(G4)
# print('fonction est_connexe validée')


def possede_un_cycle(G):
    def bfs_cycle(G, s, couleur, reponse):
        file = deque()
        couleur['s'] = 'gris'
        file.append(s)
        while len(file) > 0:
            v = file.popleft()
            if couleur[v] != 'noir':
                couleur[v] = 'noir'
                for w in G[v]:
                    if couleur[w] == 'gris':
                        reponse.append(True)
                    if couleur[w] == 'blanc':
                        couleur[w] = 'gris'
                        file.append(w)

    return len(parcours(G, bfs_cycle)) > 0


# assert possede_un_cycle(G1)
# assert not possede_un_cycle(G2)
# assert possede_un_cycle(G3)
# assert possede_un_cycle(G4)
# print('fonction possède_un_cycle validée')


def comp_connexes(G):
    def bfs_connexe(G, s, compteur, couleur, reponse):
        file = deque()
        couleur['s'] = 'gris'
        file.append(s)
        while len(file) > 0:
            v = file.popleft()
            if couleur[v] != 'noir':
                couleur[v] = 'noir'
                reponse[v] = compteur
                for w in G[v]:
                    if couleur[w] != 'noir':
                        couleur[w] = 'gris'
                        file.append(w)

    def parcours_connexe(G, parcours_depuis_sommet):
        reponse = {v: 0 for v in G}
        couleur = {v: 'blanc' for v in G}
        compteur = 1
        for s in G:
            if couleur[s] != 'noir':
                parcours_depuis_sommet(G, s, compteur, couleur, reponse)
                compteur += 1
        return reponse

    return parcours_connexe(G, bfs_connexe)


# assert comp_connexes(G3) == {'a': 1, 'b': 1, 'f': 1, 'c': 1, 'e': 1, 'd': 1,
# 'g': 2, 'h': 2, 'l': 2, 'i': 2, 'j': 2, 'k': 2}
# print('fonction comp_connexes validée')


def est_accessible_depuis(G, s1, s2):
    comp = comp_connexes(G)
    return comp[s1] == comp[s2]


# assert est_accessible_depuis(G1, 'a', 'b')
# assert est_accessible_depuis(G3, 'c', 'd')
# assert not est_accessible_depuis(G3,'d', 'i')
# assert est_accessible_depuis(G4, 5, 12)
# assert not est_accessible_depuis(G4, 8, 20)
# print('fonction est_accessible_depuis validée')


animer(G6, parcours(G6, bfs))
