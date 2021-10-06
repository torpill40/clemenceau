

def f_Appartient(x: float, arr: list) -> bool:
    for i in arr:
        if i == x:
            return True
    return False


def f_Position(x: float, arr: list) -> list:
    res = []
    for i in range(len(arr)):
        if arr[i] == x:
            res += [i]
    return res
