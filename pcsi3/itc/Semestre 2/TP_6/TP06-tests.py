
# Test question 1
couleur = {v:'blanc' for v in G3}
reponse = []
bfs(G3, 'a', couleur, reponse)
if reponse == ['a', 'b', 'f', 'c', 'e', 'd']:
    print('fonction bfs validée')

# Test question 2
if parcours(G3, bfs) == ['a', 'b', 'f', 'c', 'e', 'd',
'g', 'h', 'l', 'i', 'j', 'k']:
    print('fonction parcours validée')

# Test question 4
if parcours(G3, dfs) == ['a', 'f', 'e', 'd', 'c', 'b',
'g', 'l', 'i', 'j', 'k', 'h']:
    print('fonction dfs validée')

# Test question 5
if parcours(G3, dfs_rec) == ['a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'l', 'i', 'j', 'k']:
    print('fonction dfs_rec validée')

# Test question 6
assert est_connexe(G1)
assert est_connexe(G2)
assert not est_connexe(G3)
assert not est_connexe(G4)
print('fonction est_connexe validée')

# Test question 7
assert possède_un_cycle(G1)
assert not possède_un_cycle(G2)
assert possède_un_cycle(G3)
assert possède_un_cycle(G4)
print('fonction possède_un_cycle validée')

# Test question 8
assert comp_connexes(G3) == {'a': 1, 'b': 1, 'f': 1, 'c': 1, 'e': 1, 'd': 1,
'g': 2, 'h': 2, 'l': 2, 'i': 2, 'j': 2, 'k': 2}
print('fonction comp_connexes validée')

# Test question 9
assert est_accessible_depuis(G1, 'a', 'b')
assert est_accessible_depuis(G3, 'c', 'd')
assert not est_accessible_depuis(G3,'d', 'i')
assert est_accessible_depuis(G4, 5, 12)
assert not est_accessible_depuis(G4, 8, 20)
print('fonction est_accessible_depuis validée')
