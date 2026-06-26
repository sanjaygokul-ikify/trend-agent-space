import unittest
from packages.core import Engine, Agent, MemoryAnchor

class TestCore(unittest.TestCase):
    def test_agent_state(self):
        engine = Engine(agents=[Agent(id='agent1', state={})], memory_anchors=[])
        self.assertEqual(engine.get_agent_state('agent1'), {})
    def test_memory_anchor_state(self):
        engine = Engine(agents=[], memory_anchors=[MemoryAnchor(id='memory_anchor1', state={})])
        self.assertEqual(engine.get_memory_anchor_state('memory_anchor1'), {})