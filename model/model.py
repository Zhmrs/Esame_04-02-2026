import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self._role=[]
        self.artists = []
        self.id_map_artist={}

        self._nodes=[]
        self._edges=[]

        self. load_role()

    def load_role(self):
        self._role=DAO.get_authorship()

    def build_graph(self, role: str):
        self.G.clear()

        self._nodes=[]
        self.artists=DAO.get_author(role)

        self._nodes=self.artists
        for a in self.artists:
            self.id_map_artist[a.artist_id]=a
            self.G.add_node(a)

        artisti_numeri=DAO.get_connessioni()
        an={}
        for a in artisti_numeri:
            if a in self.id_map_artist:
                if a not in an:
                    an[a]=1
                else:
                    an[a]+=1

        valori=[]
        archi={}
        for x in self.id_map_artist:
            valori.append(x)

        for v in valori[:]:
            for j in valori[1:]:
                if v in an and j in an:
                    if an[v]<an[j] and v!=j:
                        archi[(self.id_map_artist[v],self.id_map_artist[j])] = abs(an[v]-an[j])

        for v,p in archi.items():
            self.G.add_edge(v[0],v[1],weight=p)

    def classifica(self):
        pass

    def num_nodes(self):
        nodi= set()
        for u in self.G.edges(data=True):
            nodi.add(u[0])
            nodi.add(u[1])
        return len(nodi)

    def num_edges(self):
        return len(self.G.edges())