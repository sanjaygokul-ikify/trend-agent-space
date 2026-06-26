from typing import List
from packages.core import Engine

class Orchestrator:
    def __init__(self):
        self.engine = Engine(agents=[], memory_anchors=[])