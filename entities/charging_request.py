class ChargingRequest:
    def __init__(self, node_from, node_to, request_time, delta_t, initial_soc, required_soc):
        self.node_from = node_from
        self.node_to = node_to
        self.request_time = request_time
        self.delta_t = delta_t
        self.initial_soc = initial_soc
        self.required_soc = required_soc
        