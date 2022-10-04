from typing import Type, Callable
import mesa
import random
from src.agents.company import CompanyAgent

class RandomActivationByTypeFiltered(mesa.time.BaseScheduler):
    
    def get_capital(self, type) -> int:
        total_capital = 0
        count = 1
        for agent in self._agents.values():
            if  isinstance(agent, CompanyAgent) and agent.type == type:
                total_capital += agent.capital
                count += 1
        return total_capital / count