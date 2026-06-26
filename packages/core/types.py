from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Agent:
    id: str
    state: Dict
    def start(self):
        pass
    def stop(self):
        pass

@dataclass
class MemoryAnchor:
    id: str
    state: Dict
    def start(self):
        pass
    def stop(self):
        pass