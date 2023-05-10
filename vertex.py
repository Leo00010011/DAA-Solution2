
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

def make_edge(a:Vertex,b:Vertex,weight:int):
    a.neighbourhood.append((b,weight))
    b.neighbourhood.append((a,weight))