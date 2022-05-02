
def nombre_amis(amis, membre):
    return len(amis[membre])


# amis = {}
# amis['Joe'] = ['Emmanuel', 'Boris']
# amis['Emmanuel'] = ['Joe', 'Xi']
# amis['Vladimir'] = ['Xi']
# amis['Boris'] = ['Joe']
# amis['Kim'] = ['Xi']
# amis['Xi'] = []
# print(nombre_amis(amis, 'Emmanuel'))


def est_ami(amis, membre1, membre2):
    return membre2 in amis[membre1]


# amis = {}
# amis['Joe'] = ['Emmanuel', 'Boris']
# amis['Emmanuel'] = ['Joe', 'Xi']
# amis['Vladimir'] = ['Xi']
# amis['Boris']=['Joe']
# amis['Kim'] = ['Xi']
# amis['Xi'] = []
# print(est_ami(amis, 'Kim', 'Xi'))
# print(est_ami(amis, 'Kim', 'Emmanuel'))
# print(est_ami(amis, 'Emmanuel', 'Xi'))


def transpose(amis):
    dico = {membre: [] for membre in amis}
    for membre in amis:
        for ami in amis[membre]:
            dico[ami] += [membre]
    return dico


# amis = {}
# amis['Joe'] = ['Emmanuel', 'Boris']
# amis['Emmanuel'] = ['Joe', 'Xi']
# amis['Vladimir'] = ['Xi']
# amis['Boris']=['Joe']
# amis['Kim'] = ['Xi']
# amis['Xi'] = []
# print(transpose(amis))


def est_ami_dami(amis, membre1, membre2):
    for ami in amis[membre1]:
        if est_ami(amis, ami, membre2):
            return True
    return False


# amis = {}
# amis['Joe'] = ['Emmanuel', 'Boris']
# amis['Emmanuel'] = ['Joe', 'Xi']
# amis['Vladimir'] = ['Xi']
# amis['Boris'] = ['Joe']
# amis['Kim'] = ['Xi']
# amis['Xi'] = []
# print(est_ami_dami(amis, 'Joe', 'Boris'))
# print(est_ami_dami(amis, 'Joe', 'Xi'))
