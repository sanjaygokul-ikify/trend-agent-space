from typing import List, Dict
from .types import Agent, MemoryAnchor
from .exceptions import CoreException
import logging

logger = logging.getLogger(__name__)

class Engine:
    def __init__(self, agents: List[Agent], memory_anchors: List[MemoryAnchor]):
        self.agents = agents
        self.memory_anchors = memory_anchors
        self.agent_state = {}
        self.memory_anchor_state = {}

    def start(self):
        for agent in self.agents:
            try:
                agent.start()
            except Exception as e:
                logger.error(f'Error starting agent {agent.id}: {str(e)}')
        for memory_anchor in self.memory_anchors:
            try:
                memory_anchor.start()
            except Exception as e:
                logger.error(f'Error starting memory anchor {memory_anchor.id}: {str(e)}')

    def stop(self):
        for agent in self.agents:
            try:
                agent.stop()
            except Exception as e:
                logger.error(f'Error stopping agent {agent.id}: {str(e)}')
        for memory_anchor in self.memory_anchors:
            try:
                memory_anchor.stop()
            except Exception as e:
                logger.error(f'Error stopping memory anchor {memory_anchor.id}: {str(e)}')

    def add_agent(self, agent: Agent):
        self.agents.append(agent)
        self.agent_state[agent.id] = agent.state

    def remove_agent(self, agent_id: str):
        for agent in self.agents:
            if agent.id == agent_id:
                self.agents.remove(agent)
                del self.agent_state[agent_id]
                break

    def add_memory_anchor(self, memory_anchor: MemoryAnchor):
        self.memory_anchors.append(memory_anchor)
        self.memory_anchor_state[memory_anchor.id] = memory_anchor.state

    def remove_memory_anchor(self, memory_anchor_id: str):
        for memory_anchor in self.memory_anchors:
            if memory_anchor.id == memory_anchor_id:
                self.memory_anchors.remove(memory_anchor)
                del self.memory_anchor_state[memory_anchor_id]
                break

    def update_agent_state(self, agent_id: str, state: Dict):
        if agent_id in self.agent_state:
            self.agent_state[agent_id] = state
        else:
            raise CoreException('Agent not found')

    def update_memory_anchor_state(self, memory_anchor_id: str, state: Dict):
        if memory_anchor_id in self.memory_anchor_state:
            self.memory_anchor_state[memory_anchor_id] = state
        else:
            raise CoreException('Memory anchor not found')

    def get_agent_state(self, agent_id: str) -> Dict:
        if agent_id in self.agent_state:
            return self.agent_state[agent_id]
        else:
            raise CoreException('Agent not found')

    def get_memory_anchor_state(self, memory_anchor_id: str) -> Dict:
        if memory_anchor_id in self.memory_anchor_state:
            return self.memory_anchor_state[memory_anchor_id]
        else:
            raise CoreException('Memory anchor not found')

    def conflict_resolution(self, agent_id: str, memory_anchor_id: str):
        # Implement conflict resolution logic here
        pass

    def deterministic_replay(self, agent_id: str, memory_anchor_id: str):
        # Implement deterministic replay logic here
        pass
