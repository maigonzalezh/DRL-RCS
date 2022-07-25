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

    def get_total_time(self, node_from, node_to):
        route = nx.shortest_path(self.G, node_from, node_to, weight='weight')
        route_weight_sum = 0
        for i in range(len(route)-1):
            route_weight_sum += self.G[route[i]][route[i+1]]['weight']
        return route_weight_sum
