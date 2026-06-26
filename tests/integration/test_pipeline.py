import unittest
from packages.core import Engine
from packages.utils import metrics

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        engine = Engine(agents=[{'id': 'agent1'}], memory_anchors=[{'id': 'memory_anchor1'}])
        metric = metrics.Metric('pipeline')
        metric.start()
        engine.start()
        engine.stop()
        metric.stop()