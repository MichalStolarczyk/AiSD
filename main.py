from typing import Any, Optional, Dict, List, Callable


class Vertex:
    data: Any
    index: int

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


class Edge:
    source: Vertex
    destination: Vertex

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return str(self.source) + " " + str(self.destination)


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}
        self.currentIndex = 0

    def __str__(self):
        string = ""
        for key in list(self.adjacencies.keys()):
            string += str(key) + "- "
            for y in self.adjacencies[key]:
                string += "[" + str(y.source) + " " + str(y.destination) + "]"
            string += '\n'
        return string

    def create_vertex(self, data: Any) -> Vertex:
        vertex = Vertex(data=data)
        self.adjacencies.update({vertex: []})
        vertex.index = self.currentIndex
        self.currentIndex += 1
        return vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex):
        edge = Edge(source=source, destination=destination)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex):
        self.add_directed_edge(source=source, destination=destination)
        edge = Edge(source=destination, destination=source)
        self.adjacencies[destination].append(edge)

    def add(self, source: Vertex, destination: Vertex):
            self.add_undirected_edge(source, destination)


def mutual_friends(g: Graph, f0: Any, f1: Any)->List[Any]:
    friends_f0 = []
    for key in list(g.adjacencies.keys()):
        if str(key)==f0:
            for y in g.adjacencies[key]:
                 friends_f0.append(str(y.destination))
    friends_f1 = []
    for key in list(g.adjacencies.keys()):
        if str(key) == f1:
            for y in g.adjacencies[key]:
                friends_f1.append(str(y.destination))
    lista = [set(friends_f0)&set(friends_f1)]
    return lista

g = Graph()
g.create_vertex("VI") #0
g.create_vertex("RU") #1
g.create_vertex("RA") #2
g.create_vertex("SU") #3
g.create_vertex("CO") #4
g.create_vertex("PA") #5
g.create_vertex("CH") #6
g.create_vertex("KE") #7
friends = list(g.adjacencies.keys())
g.add(friends[0], friends[1])
g.add(friends[0], friends[6])
g.add(friends[0], friends[4])
g.add(friends[0], friends[5])
g.add(friends[1], friends[2])
g.add(friends[1], friends[3])
g.add(friends[1], friends[4])
g.add(friends[4], friends[5])
g.add(friends[5], friends[7])

print(g)

print("..................")
print(mutual_friends(g, "VI", "RU"))

r = Graph()
r.create_vertex("DU") #0
r.create_vertex("CD") #1
r.create_vertex("IJ") #2
r.create_vertex("AM") #3
r.create_vertex("GD") #4
friends = list(r.adjacencies.keys())
r.add(friends[0], friends[1])
r.add(friends[0], friends[3])
r.add(friends[1], friends[2])
r.add(friends[2], friends[3])
r.add(friends[3], friends[4])

print(r)
print("..................")
print(mutual_friends(r, "DU", "IJ"))

a = Graph()
a.create_vertex("AL") #0
a.create_vertex("BW") #1
a.create_vertex("CL") #2
a.create_vertex("BG") #3
a.create_vertex("ER") #4
a.create_vertex("FJ") #5
friends = list(a.adjacencies.keys())
a.add(friends[0], friends[1])
a.add(friends[0], friends[3])
a.add(friends[0], friends[4])
a.add(friends[1], friends[2])
a.add(friends[1], friends[3])
a.add(friends[1], friends[4])
a.add(friends[1], friends[5])
a.add(friends[2], friends[4])
a.add(friends[3], friends[4])
a.add(friends[4], friends[5])
print(a)
print("..................")
print(mutual_friends(a, "AL", "BW"))