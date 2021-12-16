
def sans_fin(n):
    if n == 1:
        return 0
    else:
        return sans_fin(n / 10)


sans_fin(105000)