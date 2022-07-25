import numpy as np
import queue

class ChargingStation:
    def __init__(self, label, charging_rate):
        self.label = label
        self.charging_rate = charging_rate
        self.queue = queue.Queue()
        self.request_processing = None

    def process_next_request(self):
        self.request_processing = self.queue.get()

    def add_request(self, request):
        self.queue.put(request)