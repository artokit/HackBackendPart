import uuid

from maps import repo
from maps.models import Dot
from maps.schemas import Coordinate, AllDots, GraphDot

c = {
    "Вход": ["1"],
    "1": ["7а-101", "Вход", "2"],
    "2": ["1", "7а-102", "3"],
    "3": ["2", "4", "7а-103", "7"],
    "4": ["3", "7а-104"],
    "7а-102": ["2"],
    "7": ["8", "10"],
    "7а-101": ["1"],
    "7а-104": [],
    "8": ["7б-113", "7", "9", "7б-114"],
    "7б-113": [],
    "7б-114": [],
    "7а-103": []
}


def bfs(graph, start, end, visited=None, flag=False):
    queue = []
    if start == end:
        return visited

    if visited is None:
        visited = [start]
    queue.append(start)

    while queue:
        v = queue.pop()
        not_in_visited = [i for i in graph[v] if i not in visited]
        if len(not_in_visited) >= 2:
            for i in not_in_visited:
                visited.append(i)
                queue.append(i)
                f = bfs(graph, i, end, visited=visited.copy(), flag=True)
                if f:
                    visited.extend(f)
                    return visited
                if not f:
                    visited.remove(i)

        else:
            for i in graph[v]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
                    if i == end:
                        return visited


def clear_bfs(d: list[str]):
    data = []
    for i in d:
        if i not in data:
            data.append(i)
    return data


async def get_all_destinations_name():
    return await repo.get_all_destinations()


async def add_dot(coordinate: Coordinate):
    if coordinate.name is None:
        coordinate.name = str(uuid.uuid4())
    await repo.add_dot(coordinate)


async def add_line(dot_name1: str, dot_name2: str):
    await repo.add_line(dot_name1, dot_name2)
    await repo.add_line(dot_name2, dot_name1)


async def get_coordinates(start: str, end: str):
    dots = await repo.get_dots()
    graph = await form_graph(dots)
    d = []

    for i in clear_bfs(bfs(graph, start, end)):
        d.extend(get_graph_coordinate(i, dots))

    return d


async def form_graph(dots):
    graph = {}
    for dot in dots:
        if dot.dots is not None:
            graph[dot.name] = dot.dots.split(";")[:-1]
        else:
            graph[dot.name] = []
    return graph


def get_graph_coordinate(graph_name: str, graph_data: list[Dot]):
    for i in graph_data:
        if i.name == graph_name:
            return i.x, i.y


async def get_all_dots() -> AllDots:
    res = await repo.get_dots()
    graph_dots = []
    for i in res:
        d = i.dots

        if d is None:
            d = []
        else:
            d = i.dots.split(";")[:-1]

        graph_dots.append(GraphDot(name=i.name, x=i.x, y=i.y, nexts=d))

    return AllDots(graph=graph_dots)
