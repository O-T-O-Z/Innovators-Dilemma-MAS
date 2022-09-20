import mesa
from mesa import Model
from .agents.company import CompanyAgent

class MarketModel(Model):
    """A model with some number of agents."""

    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        self.spawn_agents()

    def spawn_agents(self):
        for i in range(self.num_agents):
            a = CompanyAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        self.datacollector = mesa.DataCollector(
            model_reporters={}, agent_reporters={"Wealth": "wealth"}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()