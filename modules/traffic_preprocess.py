import networkx as nx

MAXIMUM_VELOCITY = 40  # km/h (chequear unidad de medida)


class TrafficPreprocessModule:
    def __init__(self, G):
        self.G = G

    def get_traffic_network(self):
        G_weighted = nx.Graph(self.G)
        for edge in self.G.edges():
            time_weight = self.G[edge[0]][edge[1]]['weight']/MAXIMUM_VELOCITY
            G_weighted.add_edge(
                edge[0], edge[1], weight=time_weight)
        return G_weighted
