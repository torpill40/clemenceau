from ansi import CURSOR_POS, CURSOR_POS_X, CURSOR_POS_Y, COLOR_8BIT, RESET
from abc import ABC, abstractmethod
from typing import Optional, Any


class Area(ABC):

    def __init__(self, rel_pos: tuple, dim: tuple, color: int = 220):
        self._x: int = int(rel_pos[0])
        self._y: int = int(rel_pos[1])
        self._width: int = int(dim[0])
        self._height: int = int(dim[1])
        self._color: int = color
        self.__n: str = '─'
        self.__s: str = '─'
        self.__e: str = '│'
        self.__w: str = '│'
        self.__ne: str = '┐'
        self.__nw: str = '┌'
        self.__se: str = '┘'
        self.__sw: str = '└'
        self._parent: Optional[Area] = None

    def set_style(self, **kwargs) -> None:
        if 'n' in kwargs.keys(): self.__n = kwargs['n']
        if 's' in kwargs.keys(): self.__s = kwargs['s']
        if 'e' in kwargs.keys(): self.__e = kwargs['e']
        if 'w' in kwargs.keys(): self.__w = kwargs['w']
        if 'ne' in kwargs.keys(): self.__ne = kwargs['ne']
        if 'nw' in kwargs.keys(): self.__nw = kwargs['nw']
        if 'se' in kwargs.keys(): self.__se = kwargs['se']
        if 'sw' in kwargs.keys(): self.__sw = kwargs['sw']

    def draw(self) -> None:
        x, y = self.get_abs_pos()
        top: str = f"{CURSOR_POS_X(x)}{COLOR_8BIT(self._color)}{self.__nw}{self.__n * (self._width - 2)}{self.__ne}{RESET}"
        row: str = f"{CURSOR_POS_X(x)}{COLOR_8BIT(self._color)}{self.__w}{' ' * (self._width - 2)}{self.__e}{RESET}"
        bot: str = f"{CURSOR_POS_X(x)}{COLOR_8BIT(self._color)}{self.__sw}{self.__s * (self._width - 2)}{self.__se}{RESET}"
        res: str = f"{CURSOR_POS_Y(y)}{top}\n"
        for _ in range(self._height - 2):
            res += row + '\n'
        res += bot
        print(res, end='')

    @abstractmethod
    def print(self) -> None:
        pass

    def clear(self) -> None:
        x, y = self.get_abs_pos()
        row: str = f"{CURSOR_POS_X(x + 1)}{' ' * (self._width - 2)}"
        res: str = f"{CURSOR_POS_Y(y + 1)}"
        for _ in range(self._height - 2):
            res += f"{row}\n"
        print(res, end='')

    def cursor_in(self) -> None:
        x, y = self.get_abs_pos()
        print(f"{CURSOR_POS(y + 1, x + 2)}", end='')

    def cursor_after(self) -> None:
        x, y = self.get_abs_pos()
        print(f"{CURSOR_POS(y + self._height, 0)}", end='')

    def get_rel_pos(self) -> tuple:
        return self._x, self._y

    def get_abs_pos(self) -> tuple:
        if self._parent is None:
            return self._x, self._y
        else:
            x, y = self._parent.get_abs_pos()
            return x + self._x, y + self._y

    def get_dim(self) -> tuple:
        return self._width, self._height


class PlainArea(Area):

    def __init__(self, pos: tuple, dim: tuple, text: str = "", color: int = 220):
        Area.__init__(self, pos, dim, color)
        self._text: str = text

    def print(self) -> None:
        x, y = self.get_abs_pos()
        text: str = self._text.replace('\n', f"\n{CURSOR_POS_X(x + 2)}")
        res: str = f"{CURSOR_POS_Y(y + 1)}{CURSOR_POS_X(x + 2)}{text}"
        print(res, end='')

    def set_text(self, text: str) -> None:
        self._text: str = text

    def get_text(self) -> str:
        return self._text


class TextArea(PlainArea):

    def __init__(self, pos: tuple, dim: tuple, text: str = "", color: int = 220):
        PlainArea.__init__(self, pos, dim, text, color)

    def print(self) -> None:
        x, y = self.get_abs_pos()
        width: int = 0
        words: list = self._text.split()
        text: str = f"{CURSOR_POS_X(x + 2)}"
        for word in words:
            width += (len(word) + 1)
            if width >= self._width - 3:
                width = len(word)
                text += f"\n{CURSOR_POS_X(x + 2)}{word}"
                if width < self._width - 3:
                    text += " "
            else:
                text += f"{word} "
        res: str = f"{CURSOR_POS_Y(y + 1)}{text}"
        print(res, end='')


class ListArea(Area):

    def __init__(self, pos: tuple, dim: tuple, style: str = '-', color: int = 220):
        Area.__init__(self, pos, dim, color)
        self.__style: str = style
        self.__items: list = list()

    def print(self) -> None:
        x, y = self.get_abs_pos()
        text: str = ""
        for item in self.__items:
            text += f"{CURSOR_POS_X(x + 2)}{self.__style} {item}\n"
        res: str = f"{CURSOR_POS_Y(y + 1)}{text}"
        print(res, end='')

    def add_item(self, item: str) -> None:
        self.__items.append(item)

    def remove_item(self, n: int) -> None:
        self.__items.pop(n)


class ValueArea(Area):

    def __init__(self, pos: tuple, dim: tuple, max_len_value: int = 10, color: int = 220):
        Area.__init__(self, pos, dim, color)
        self.__max_len_value: int = max_len_value
        self.__values: list = list()

    def print(self) -> None:
        x, y = self.get_abs_pos()
        lines: list = [f"{CURSOR_POS_X(x + 2)}"] * (self._height - 2)
        for i, value in enumerate(self.__values):
            lines[i % (self._height - 2)] += f"{COLOR_8BIT(self._color)}[{i}]:{RESET}{' ' * (4 - len(str(i)))}{value}"
            if i + self._height - 2 < len(self.__values):
                lines[i % (self._height - 2)] += ' ' * (self.__max_len_value - len(str(value)))
        text: str = "\n".join(lines)
        res: str = f"{CURSOR_POS_Y(y + 1)}{text}"
        print(res, end='')

    def add_value(self, value: Any) -> None:
        self.__values.append(value)

    def set_value(self, n: int, value: Any) -> None:
        self.__values[n] = value

    def delete_value(self, n: int) -> None:
        self.__values.pop(n)


class KWValueArea(Area):

    def __init__(self, pos: tuple, dim: tuple, max_len_key: int = 4, max_len_value: int = 10, color: int = 220):
        Area.__init__(self, pos, dim, color)
        self.__max_len_key: int = max_len_key
        self.__max_len_value: int = max_len_value
        self.__values: dict = dict()

    def print(self) -> None:
        x, y = self.get_abs_pos()
        lines: list = [f"{CURSOR_POS_X(x + 2)}"] * (self._height - 2)
        for i, (key, value) in enumerate(self.__values.items()):
            lines[i % (self._height - 2)] += f"{COLOR_8BIT(self._color)}[{key}]:{RESET}{' ' * (self.__max_len_key - len(str(key)))}{value}"
            if i + self._height - 2 < len(self.__values):
                lines[i % (self._height - 2)] += ' ' * (self.__max_len_value - len(str(value)))
        text: str = "\n".join(lines)
        res: str = f"{CURSOR_POS_Y(y + 1)}{text}"
        print(res, end='')

    def set_value(self, key: Any, value: Any) -> None:
        self.__values[key] = value

    def delete_value(self, key: Any) -> None:
        self.__values.pop(key)


class Table(Area):

    def __init__(self, pos: tuple, dim: tuple = (0, 0), color: int = 220):
        Area.__init__(self, pos, dim, color=color)
        self.__areas: list = list()

    def draw(self) -> None:
        Area.draw(self)
        for area in self.__areas:
            area.draw()
        self.cursor_after()

    def print(self) -> None:
        for area in self.__areas:
            area.print()
        self.cursor_after()

    def add_area(self, area: Area) -> None:
        if area._parent is not None: return
        self.__areas.append(area)
        area._parent = self
        if area._x + area._width > self._width:
            self._width = area._x + area._width
        if area._y + area._height > self._height:
            self._height = area._y + area._height

    def increase_dim(self, dw: int = 1, dh: int = 1) -> None:
        self._width += dw
        self._height += dh
