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
