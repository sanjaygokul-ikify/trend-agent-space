import unittest
from packages.core import Engine

class TestRuntime(unittest.TestCase):
    def test_engine_lifecycle(self):
        engine = Engine(agents=[], memory_anchors=[])
        engine.start()
        engine.stop()