
ESC = '\u001B'
CSI = ESC + '['
SAVE_POS = CSI + 's'
REST_POS = CSI + 'u'
RESET = CSI + "0m"
UNDERLINE = CSI + "4m"


def CURSOR_UP(n: int) -> str:
    return f"{CSI}{n}A"


def CURSOR_DOWN(n: int) -> str:
    return f"{CSI}{n}B"


def CURSOR_FORWARD(n: int) -> str:
    return f"{CSI}{n}C"


def CURSOR_BACK(n: int) -> str:
    return f"{CSI}{n}D"


def CURSOR_POS_X(n: int) -> str:
    return f"{CSI}{n}G"


def CURSOR_POS_Y(n: int) -> str:
    return f"{CSI}{n};1H"


def CURSOR_POS(n: int, m: int) -> str:
    return f"{CSI}{n};{m}H"


def ERASE_DISP(n: int) -> str:
    return f"{CSI}{n}J"


def ERASE_LINE(n: int) -> str:
    return f"{CSI}{n}K"


def COLOR_8BIT(color: int) -> str:
    return f"{CSI}38;5;{color}m"


def COLOR_24BIT(color: int) -> str:
    return f"{CSI}38;2;{(color >> 16) & 0xFF};{(color >> 8) & 0xFF};{color & 0xFF}m"
