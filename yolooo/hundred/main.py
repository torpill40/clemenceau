import numpy as np
import traceback as tb
from typing import Optional, Callable
from table import Table, PlainArea, ValueArea
from ansi import ERASE_DISP, UNDERLINE, COLOR_8BIT, RESET

try:
    import pycuda.driver as cuda
    import pycuda.autoinit
    import pycuda.compiler as compiler

    __gpu_accelerator: bool = True
except ImportError:
    cuda = None
    compiler = None
    __gpu_accelerator: bool = False

if __gpu_accelerator:
    with open("hundred.cu", "r") as kernel:
        src: str = "".join(kernel.readlines())
    print(f"CUDA Kernel - hundred.cu:\n{src}")
    mod = compiler.SourceModule(src)
    __gpu_gen_binary_map = mod.get_function("gen_binary_map")
else:
    __gpu_gen_binary_map = None

layout: tuple = (
    {
        "pos": (0, 0),
        "dim": (30, 17)
    },
    {
        "pos": (29, 0),
        "dim": (71, 17)
    },
    {
        "pos": (0, 16),
        "dim": (100, 4)
    }
)


class Interface:

    def __init__(self):
        self.__content: Table = Table((1, 1))
        self.__inputs_area: ValueArea = ValueArea(layout[0]["pos"], layout[0]["dim"], 5)
        self.__inputs_area.set_style(sw='├')
        self.__right_area: PlainArea = PlainArea(layout[1]["pos"], layout[1]["dim"])
        self.__right_area.set_style(nw='┬', se='┤', sw='┴')
        self.__input_area: PlainArea = PlainArea(layout[2]["pos"], layout[2]["dim"])

        self.__content.add_area(self.__input_area)
        self.__content.add_area(self.__inputs_area)
        self.__content.add_area(self.__right_area)

    def show(self) -> None:
        print(f"{ERASE_DISP(2)}", end='')
        self.__content.draw()
        self.__content.print()

    def read_input(self, prompt: str) -> str:
        self.__input_area.set_text(prompt)
        self.__input_area.print()
        res: str = input()
        self.__input_area.set_text("")
        self.show()
        return res

    def set_text(self, text: str) -> None:
        self.__right_area.set_text(text)

    def add_value(self, value: int) -> None:
        self.__inputs_area.add_value(value)
        self.__inputs_area.clear()
        self.__inputs_area.print()

    def set_value(self, idx: int, value: int) -> None:
        self.__inputs_area.set_value(idx, value)
        self.__inputs_area.clear()
        self.__inputs_area.print()

    def delete_value(self, idx: int) -> None:
        self.__inputs_area.delete_value(idx)
        self.__inputs_area.clear()
        self.__inputs_area.print()


class App:

    def __init__(self):
        self.__interface: Interface = Interface()
        self.__numbers: list = list()
        self.__hundred: list = list()
        self.__alive: bool = False

    def start(self) -> bool:
        if self.__alive:
            return False
        self.__alive = True
        self.run()

    def stop(self, args: list) -> None:
        self.__alive = False

    def calc_and_print(self, args: list) -> None:
        if len(self.__numbers) == 0:
            return
        num: int = int(args[0]) if len(args) > 0 else 100
        terms: int = int(args[1]) if len(args) > 1 else 0
        self.calc(num, terms)
        self.hundred_nav(num, terms)

    def calc(self, num: int, terms: int) -> None:
        vec: np.ndarray = list_to_ndarray(self.__numbers)
        mat: np.ndarray = gen_binary_map(len(vec))
        res: np.ndarray = np.matmul(mat, vec).astype(np.int32)
        self.__hundred = find_summands_eq_val(num, terms, vec, res)

    def print_hundred(self, num: int, terms: int, page: int, item_per_page: int, mx_page: int) -> None:
        res: str = f"{UNDERLINE}Sommes de termes égales à {num}{f' avec {terms} termes' if terms > 0 else ''}:{RESET}\n"
        new_lines: int = 1
        for i in range(item_per_page * page, item_per_page * page + item_per_page):
            if i >= len(self.__hundred):
                new_lines = item_per_page * page + item_per_page - i + 1
                break
            calc: str = f"{self.__hundred[i][0]}"
            for j in range(1, len(self.__hundred[i])):
                calc += f" {'+' if self.__hundred[i][j] >= 0 else '-'} {abs(self.__hundred[i][j])}"
            res += f"{np.sum(self.__hundred[i])} = {calc}\n"
        nl: str = '\n' * new_lines
        res += f"{nl}" \
               f"- p [n:1]: page précédente n fois.\n" \
               f"- n [n:1]: page suivante n fois.\n" \
               f"- 'entrée': retourner à l'écran précédent.         Page {(page + 1):4d} / {(mx_page + 1):4d}"
        self.__interface.set_text(res)
        self.__interface.show()

    def hundred_nav(self, num: int, terms: int) -> None:
        item_per_page: int = layout[1]["dim"][1] - 7
        page: int = 0
        mx_page: int = (len(self.__hundred) - 1) // item_per_page
        if mx_page < 0:
            mx_page = 0
        self.print_hundred(num, terms, page, item_per_page, mx_page)
        while (in_cmd := self.__interface.read_input(f"Entrez une commande ('entrée' pour fermer):\n$ ")) != "":
            args: list = in_cmd.split()
            repeat: int = 1
            if len(args) > 1:
                repeat = int(args[1])
            plus: Callable[[int], int] = lambda n, k: n + k
            minus: Callable[[int], int] = lambda n, k: n - k
            switcher = {
                "n": plus,
                "p": minus
            }
            func: Optional[Callable[[int], int]] = switcher.get(args[0])
            if func is not None:
                page = func(page, repeat)
                if page < 0:
                    page = mx_page
                elif page > mx_page:
                    page = 0
            self.print_hundred(num, terms, page, item_per_page, mx_page)
            
    def add_values(self, args: list) -> None:
        if len(args) > 0:
            for i in args:
                value: int = int(i)
                self.__numbers.append(value)
                self.__interface.add_value(value)
        else:
            self.__interface.set_text(f"{UNDERLINE}Utilitaire d'aide:{RESET}\n"
                                      f"- Entrez les termes à ajouter un par un.\n"
                                      f"- Les valeurs seront modifiable à l'aide de la commande 's'.\n"
                                      f"- Appuyez sur 'entrée' pour retourner à l'écran précédent.")
            self.__interface.show()
            while (in_val := self.__interface.read_input(f"Entrez un nombre entier ('entrée' pour fermer):\n$ ")) != "":
                value: int = int(in_val)
                self.__numbers.append(value)
                self.__interface.add_value(value)

    def set_values(self, args: list) -> None:
        self.__interface.set_text(f"{UNDERLINE}Utilitaire d'aide:{RESET}\n"
                                  f"- Entrez l'indice du terme à modifier.\n"
                                  f"- Entrez ensuite la nouvelle valeur du terme.\n"
                                  f"- Appuyez sur 'entrée' pour retourner à l'écran précédent.")
        self.__interface.show()
        while (in_val := self.__interface.read_input(f"Entrez l'indice du terme à changer ('entrée' pour fermer):\n$ ")) != "":
            idx: int = int(in_val)
            if idx >= len(self.__numbers):
                continue
            in_val = self.__interface.read_input(f"Entrez la nouvelle valeur de [{idx}]:\n$ ")
            value: int = int(in_val)
            self.__numbers[idx] = value
            self.__interface.set_value(idx, value)

    def delete_values(self, args: list) -> None:
        if len(args) > 0:
            args.reverse()
            for i in args:
                idx: int = int(i)
                if idx >= len(self.__numbers):
                    continue
                self.__numbers.pop(idx)
                self.__interface.delete_value(idx)
        else:
            self.__interface.set_text(f"{UNDERLINE}Utilitaire d'aide:{RESET}\n"
                                      f"- Entrez l'indice du terme à supprimer.\n"
                                      f"- Appuyez sur 'entrée' pour retourner à l'écran précédent.")
            self.__interface.show()
            while (in_val := self.__interface.read_input(f"Entrez l'indice du terme à supprimer ('entrée' pour fermer):\n$ ")) != "":
                idx: int = int(in_val)
                if idx >= len(self.__numbers):
                    continue
                self.__numbers.pop(idx)
                self.__interface.delete_value(idx)

    def run(self) -> None:
        while self.__alive:
            try:
                self.__interface.set_text(f"{UNDERLINE}Liste de commandes:{RESET}\n"
                                          f"- a: ajouter des termes à la liste depuis l'utilitaire.\n"
                                          f"- a [n...]: ajouter les termes n séparés par des espaces à la\n"
                                          f"     liste.\n"
                                          f"- s: modifier des termes de la liste depuis l'utilitaire.\n"
                                          f"- r: supprimer des termes de la liste depuis l'utilitaires.\n"
                                          f"- r [n...]: supprimer les termes d'indice n séparés par des espaces\n"
                                          f"     de la liste.\n"
                                          f"- c [n:100] [m:0]: calculer et afficher les sommes de m termes\n"
                                          f"     (0 pour tous) égales à n.\n"
                                          f"- e: fermer le programme.")
                self.__interface.show()
                in_cmd = self.__interface.read_input(f"Entrez une commande:\n$ ")
                if in_cmd == "":
                    continue
                args: list = in_cmd.split()
                switcher = {
                    "a": self.add_values,
                    "s": self.set_values,
                    "r": self.delete_values,
                    "c": self.calc_and_print,
                    "e": self.stop
                }
                func: Optional[Callable] = switcher.get(args[0])
                if func is not None:
                    func(args[1:])
            except ValueError:
                self.__print_exc()
            except MemoryError:
                self.__print_exc()
        self.__interface.show()

    def __print_exc(self):
        trace: str = tb.format_exc()
        trace.replace('\n', f"{RESET}\n{COLOR_8BIT(160)}")
        msg: str = f"{UNDERLINE}Une erreur est survenue:{RESET}\n{COLOR_8BIT(160)}{trace}{RESET}"
        self.__interface.set_text(msg)
        self.__interface.show()
        self.__interface.read_input(f"Appuyez sur 'entrée' pour continuer:\n$ ")


def main() -> int:
    app: App = App()
    app.start()

    return 0


def list_to_ndarray(in_list: list) -> np.ndarray:
    res = np.ndarray((len(in_list), 1)).astype(np.int32)
    for i, value in enumerate(in_list):
        res[i][0] = value
    return res


def gpu_gen_binary_map(size: int) -> np.ndarray:
    m, n = 2 ** size, size
    bx, by = 32, 32
    gx, gy = m // bx + m % bx, n // by + n % by
    b_map = np.zeros((m, n)).astype(np.int32)
    __gpu_gen_binary_map(cuda.Out(b_map), np.uint32(m), np.uint32(n), block=(bx, by, 1), grid=(gx, gy, 1))
    return b_map


def cpu_gen_binary_map(size: int) -> np.ndarray:
    b_map = np.zeros((2 ** size, size)).astype(np.int32)
    for i in range(2 ** size):
        for j in range(size):
            b_map[i][j] = (i >> j) & 1
    return b_map


def gen_binary_map(size: int) -> np.ndarray:
    return gpu_gen_binary_map(size) if __gpu_accelerator else cpu_gen_binary_map(size)


def find_summands_eq_val(val: int, terms: int, vec: np.ndarray, res: np.ndarray) -> list:
    eq = list()
    for i in np.where(res == val)[0]:
        summand = list()
        for j, value in enumerate(vec):
            if (i >> j) & 1 == 1:
                summand.append(vec[j][0])
        if terms <= 0 or len(summand) == terms:
            eq.append(tuple(summand))
    return eq


if __name__ == '__main__':
    main()
