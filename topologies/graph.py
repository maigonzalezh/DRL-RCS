import networkx as nx


class Graph:
    def __init__(self, G):
        self.G = G

    def get_nodes_labels(self, exclude_evcs=False):
        if exclude_evcs:
            nodes_non_evcs_labels = []
            for node in self.G.nodes():
                if "EVCS" not in node:
                    nodes_non_evcs_labels.append(node)
            return nodes_non_evcs_labels
        else:
            return self.G.nodes()

    def get_evcs_labels(self):
        evcs_labels = []
        for node in self.G.nodes():
            if "EVCS" in node:
                evcs_labels.append(node)
        return evcs_labels

    def get_total_distance(self, node_from, node_to):
        route = nx.shortest_path(self.G, node_from, node_to, weight='weight')
        route_weight_sum = 0
        for i in range(len(route)-1):
            route_weight_sum += self.G[route[i]][route[i+1]]['weight']
        return route_weight_sum
