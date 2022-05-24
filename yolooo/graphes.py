from collections import deque
from typing import Callable

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from random import randrange, choice


class Graph:
    __slots__ = ['__width', '__height', '__graph', '__edges']

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__graph = {i: [] for i in range(self.__width * self.__height)}
        self.__edges = {}

    def __call__(self, *args, **kwargs):
        return self.__graph

    def __getitem__(self, s: int):
        return self.__graph[s]

    def __iadd__(self, edge: tuple):
        if edge not in self:
            self.__graph[edge[0]].append(edge[1])
            self.__graph[edge[1]].append(edge[0])
            self.__edges[edge if edge[0] < edge[1] else (edge[1], edge[0])] = len(self.__edges)
        return self

    def __isub__(self, edge: tuple[int, int]):
        if edge in self:
            self.__graph[edge[0]].remove(edge[1])
            self.__graph[edge[1]].remove(edge[0])
            self.__recalc_edges()
        return self

    def __contains__(self, edge: tuple[int, int]):
        # return edge[0] in self.__graph and edge[1] in self.__graph[edge[0]]
        return (edge if edge[0] < edge[1] else (edge[1], edge[0])) in self.__edges

    def __repr__(self):
        return f"Graph[{self.__width}, {self.__height}]: {self.__graph}"

    def __recalc_edges(self):
        i = 0
        self.__edges.clear()
        for s in self.__graph:
            for v in self.__graph[s]:
                if v >= s:
                    self.__edges[(s, v)] = i
                    i += 1

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def edges(self):
        return list(self.__edges)

    def index(self, edge: tuple[int, int]):
        return self.__edges[edge if edge[0] < edge[1] else (edge[1], edge[0])]


def hsv_color(hue: int, sat: float, val: float) -> str:
    c = val * sat
    x = c * (1 - abs((hue / 60) % 2 - 1))
    m = val - c
    r, g, b = 0, 0, 0
    if 0 <= hue < 60:
        r, g, b = c, x, 0
    elif 60 <= hue < 120:
        r, g, b = x, c, 0
    elif 120 <= hue < 180:
        r, g, b = 0, c, x
    elif 180 <= hue < 240:
        r, g, b = 0, x, c
    elif 240 <= hue < 300:
        r, g, b = x, 0, c
    elif 300 <= hue < 360:
        r, g, b = c, 0, x
    return f"#{int((r + m) * 0xFF):02X}{int((g + m) * 0xFF):02X}{int((b + m) * 0xFF):02X}"


def draw(graph: Graph):
    w = graph.width()
    h = graph.height()
    position = {x + y * w: (x, y) for x in range(w) for y in range(h)}

    plt.figure(figsize=(14, 8))
    plt.axes([0, 0, 1, 1])
    plt.axis('equal')
    nx.draw(nx.Graph(graph()), pos=position, with_labels=False, node_shape='s', node_color='k', edgecolors='k',
            node_size=100, width=7, linewidths=0)
    plt.show()


def animate(graph: Graph,
            path_from: Callable[[dict[int, list[int]],
                                 int,
                                 dict[int, str],
                                 list[tuple[int, int, float]]], None]
            ):
    path_ = path(graph, path_from)
    w = graph.width()
    h = graph.height()
    position = {x + y * w: (x, y) for x in range(w) for y in range(h)}
    nx_g = nx.Graph(graph())

    fig = plt.figure(figsize=(14, 8))

    def numbering(g):
        dict_ = {}
        list_ = list(g.keys())
        for i in range(len(list_)):
            dict_[list_[i]] = i
        return dict_

    num = numbering(graph())
    colormap = ['w' for _ in graph()]
    edge_colormap = ['w' for _ in graph.edges()]

    def animate_(frame):
        nonlocal colormap, edge_colormap
        fig.clear()
        plt.axes([0, 0, 1, 1])
        plt.axis('equal')
        if frame == 0:
            colormap = ['k' for _ in graph()]
            edge_colormap = ['k' for _ in graph.edges()]
        else:
            u, v, c = path_[frame - 1]
            rgb = hsv_color(int(c) % 360, .5, 1.)
            colormap[num[v]] = rgb
            if (u, v) in graph:
                edge_colormap[graph.index((u, v))] = rgb
        nx.draw(nx_g, pos=position, with_labels=False, edgelist=graph.edges(), node_shape='s', edge_color=edge_colormap,
                node_color=colormap, edgecolors='k', node_size=100, width=7, linewidths=0)

    _ = ani.FuncAnimation(fig, animate_, frames=len(path_) + 1, interval=50, repeat=False)
    plt.show()


def classic(graph: Graph, p: int = 1, q: int = 1):
    w = graph.width()
    h = graph.height()
    for x in range(w - 1):
        for y in range(h):
            if randrange(p) < q:
                s = x + y * w
                graph += (s, s + 1)
    for x in range(w):
        for y in range(h - 1):
            if randrange(p) < q:
                s = x + y * w
                graph += (s, s + w)
    # for i in graph():
    #     graph[i].sort()


def maze(graph: Graph, c: int = 0):
    """
    Créer un labyrinthe, à partir d'un graphe modifié sur place, avec un maximum de c cycles.

    :param graph: graphe modifié sur place
    :param c: nombre maximal de cycles
    """
    color = {v: 'w' for v in graph()}
    w = graph.width()
    h = graph.height()
    x = randrange(0, w)
    y = randrange(0, h)
    s = x + y * w
    unprocessed = [s]
    color[s] = 'g'
    while len(unprocessed) > 0:
        s = unprocessed[-1]
        x = s % w
        y = s // w
        right = x < w - 1 and color[s + 1] == 'w'
        left = x > 0 and color[s - 1] == 'w'
        up = y > 0 and color[s - w] == 'w'
        down = y < h - 1 and color[s + w] == 'w'
        if not (right or left or up or down):
            color[s] = 'k'
            unprocessed.pop()
        else:
            dirs = [1, -1, -w, w]
            dir_ = 0
            while not ((dir_ == 1 and right) or (dir_ == -1 and left) or (dir_ == -w and up) or (dir_ == w and down)):
                dirs.remove(dir_ := choice(dirs))
            u = s + dir_
            unprocessed.append(u)
            graph += (s, u)
            color[u] = 'g'
    for _ in range(c):
        x = randrange(0, w - 1)
        y = randrange(0, h - 1)
        dir_ = randrange(0, 2)
        s1 = x + y * w
        s2 = s1 + dir_ * (w - 1) + 1
        if s1 in graph[s2]:
            s2 = s1 + dir_ * (1 - w) + w
        graph += (s1, s2)


def bfs(g: dict[int, list[int]], s: int, color: dict[int, str], ans: list[tuple[int, int, float]]):
    queue = deque()
    color[s] = 'g'
    queue.append((s, s, 0))
    while len(queue) > 0:
        u, v, hue = queue.popleft()
        if color[v] != 'k':
            color[v] = 'k'
            ans.append((u, v, hue))
            hue += 0.5
            for w in g[v]:
                if color[w] != 'k':
                    color[w] = 'g'
                    queue.append((v, w, hue))


def dfs(g: dict[int, list[int]], s: int, color: dict[int, str], ans: list[tuple[int, int, float]]):
    stack = deque()
    color[s] = 'g'
    stack.append((s, s, 0))
    while len(stack) > 0:
        u, v, hue = stack.pop()
        if color[v] != 'k':
            color[v] = 'k'
            ans.append((u, v, hue))
            hue += 0.5
            for w in g[v]:
                if color[w] != 'k':
                    color[w] = 'g'
                    stack.append((v, w, hue))


def path(graph: Graph,
         path_from: Callable[[dict[int, list[int]],
                              int,
                              dict[int, str],
                              list[tuple[int, int, float]]], None]
         ) -> list[int, int, float]:
    color = {v: 'w' for v in graph()}
    ans = []
    for s in graph():
        if color[s] != 'k':
            path_from(graph(), s, color, ans)
    return ans


def main():
    # G1 = Graph(30, 20)
    # maze(G1, 15)
    # draw(G1)
    # animate(G1, bfs)
    G2 = Graph(40, 30)
    maze(G2)
    G2 -= G2.edges()[len(G2.edges()) // 4]
    # draw(G2)
    animate(G2, dfs)
    # G3 = Graph(20, 10)
    # classic(G3, 5, 3)
    # draw(G3)
    # animate(G3, bfs)


if __name__ == '__main__':
    main()
