from packages.core import Engine
import argparse
import json

parser = argparse.ArgumentParser(description='Orchestrate agents and memory anchors')
parser.add_argument('--agents', type=str, help='JSON list of agents')
parser.add_argument('--memory-anchors', type=str, help='JSON list of memory anchors')

args = parser.parse_args()
agents = json.loads(args.agents)
memory_anchors = json.loads(args.memory_anchors)

engine = Engine(agents=[{'id': 'agent1'}], memory_anchors=[{'id': 'memory_anchor1'}])
engine.start()