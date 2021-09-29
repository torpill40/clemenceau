n = int(input("Taille du carré: "))
chr_a = input("Entrer le premier caractère: ")
chr_b = input("Entrer le second caractère: ")

for i in range(n ** 2):
    print(chr_a if i % 2 == (n + 1) * (i // n) % 2 else chr_b, end=('' if i % n < n - 1 else '\n'))
