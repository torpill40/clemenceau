
file = open("ListePCSI3.txt", 'r')
lines = file.readlines()
file.close()

size = len(lines)

n = int(input("Entrez le numéro de l'étudiant: "))
if 0 < n <= size:
    msg = ""
    if n != 1:
        msg += lines[n - 2] + " - "
    msg += lines[n - 1]
    if n != size:
        msg += " - " + lines[n]
    print(msg.replace('\n', ''))
else:
    print("Numéro impossible")


