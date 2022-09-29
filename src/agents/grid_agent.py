from typing import Tuple
from mesa import Agent, Model
import numpy as np

class GridAgent(Agent):

    def __init__(self, unique_id: int, model: Model, position: Tuple):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.model = model
        self.position = np.array(position)

    def get_position(self):
        return tuple(self.position)

    def get_id(self):
        return self.unique_id

