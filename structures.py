class Vertex:
    Id = 0
    def __init__(self):
        self.Id = Vertex.Id
        Vertex.Id = Vertex.Id + 1
        self.neighbourhood : list[(Vertex,int)] = []
    
    def __lt__(self, v):
        return self.Id < v.Id
    
    def __eq__(self, v):
        return self.Id == v.Id
    
    def __repr__(self) -> str:
        return str(f'<{self.Id}>')

class Graph:
    def __init__(self,vertex_list):
        self.vertex : list[Vertex] = vertex_list
        self.edges : list[tuple[Vertex,Vertex]] = []

    def make_edge(self,u:Vertex,v:Vertex, w):
        u.neighbourhood.append((v,w))
        v.neighbourhood.append((u,w))
        if u.Id < v.Id:
            self.edges.append(((u,v),w))
        else:
            self.edges.append(((v,u),w))

    def __str__(self) -> str:
        lines = []
        for v in self.vertex:
            s = f'{v.Id} :'
            s = s + ', '.join([f'<{u.Id},{w}>' for u, w in v.neighbourhood])
            lines.append(s)
        return '\n'.join(lines)
    



