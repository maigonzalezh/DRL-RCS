from modules.traffic_preprocess import TrafficPreprocessModule


class Simulator:
    def __init__(self):
        self.t = 0
        self.TPM = TrafficPreprocessModule('./topologies/santiago.edgelist')

    def step(self):
        self.t += 1

simulator = Simulator()