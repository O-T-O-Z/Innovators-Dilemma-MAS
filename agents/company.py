from mesa import Agent, Model

class CompanyAgent(Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id: int, model: Model):
        super().__init__(unique_id, model)
        self.wealth = 1
        self.cost_per_step = 1
        self.product_rev_per_step = 2

    # Next actions based on the model context
    def step(self):
        pass

