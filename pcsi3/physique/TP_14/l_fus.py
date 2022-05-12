import matplotlib.pyplot as plt
import numpy as np


# Entrez la fonction de composition
def l_fusion(C, c_eau, m_eau, m_glacon, T_1, T_2, T_f):
    return ((C + m_eau * c_eau) * (T_1 - T_f) + m_glacon * c_eau * (T_2 - T_f)) / m_glacon


def main():
    # Entrez les variables
    C = ...  # kJ.K-1
    c_eau = 4.18  # kJ.kg-1.K-1
    m_eau = ...  # kg
    m_glacon = ...  # kg
    T_1 = ...  # K
    T_2 = ...  # K
    T_f = ...  # K

    # Entrez les précisions (demi intervalle de la distribution uniforme)
    Delta_C = ...  # kJ.K-1
    Delta_c_eau = ...  # kJ.kg-1.K-1
    Delta_m_eau = ...  # kg
    Delta_m_glacon = ...  # kg
    Delta_T_1 = ...  # K
    Delta_T_2 = ...  # K
    Delta_T_f = ...  # K

    # Entrez le nombre de simulation que vous voulez effectuer
    N = 100000

    # Calculs avec une distribution de probabilité uniforme
    calcul = [l_fusion(
                np.random.uniform(C - Delta_C, C + Delta_C),
                np.random.uniform(c_eau - Delta_c_eau, c_eau + Delta_c_eau),
                np.random.uniform(m_eau - Delta_m_eau, m_eau + Delta_m_eau),
                np.random.uniform(m_glacon - Delta_m_glacon, m_glacon + Delta_m_glacon),
                np.random.uniform(T_1 - Delta_T_1, T_1 + Delta_T_1),
                np.random.uniform(T_2 - Delta_T_2, T_2 + Delta_T_2),
                np.random.uniform(T_f - Delta_T_f, T_f + Delta_T_f)
    ) for _ in range(N)]
    plt.figure()
    plt.hist(calcul, bins='rice')
    plt.title(r'Résultat du tirage aléatoire de $l_{fus}$')
    plt.xlabel(r"$l_{fus} (kJ.kg^{-1})$")
    plt.show()

    # Calcul et affichage moyenne et écart type
    moy = np.mean(calcul)
    std = np.std(calcul, ddof=1)
    print("Moyenne = {:.2f} kJ.kg-1".format(moy))
    print("Ecart type = {:.2f} kJ.kg-1".format(std))


if __name__ == '__main__':
    main()
