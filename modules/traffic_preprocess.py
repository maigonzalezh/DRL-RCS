from copyreg import constructor


import networkx as nx

class TrafficPreprocessModule:
    def __init__(self, topology_dir):
        file = open(topology_dir, "rb")
        self.G = nx.read_edgelist(file)
        file.close()
        print(f'🏙️  Loaded topology with {self.G.number_of_nodes()} nodes and {self.G.number_of_edges()} edges.')

