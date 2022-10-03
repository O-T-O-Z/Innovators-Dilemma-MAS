from typing import Type, Callable
import mesa
import random


class RandomActivationByTypeFiltered(mesa.time.BaseScheduler):
    
    def get_capital(self, agent) -> int:
        return agent.capital