import mesa
from mesa import Model
from src.agents.company import CompanyAgent


class MarketModel(Model):
    """A model with some number of agents."""

    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        self.spawn_agents()

    def spawn_agents(self):
        for id in range(self.num_agents):
            
            while True:
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                if not self.grid[x][y]:
                    break
            
            agent = CompanyAgent(id, self, x, y)
            
            self.schedule.add(agent)
            self.grid.place_agent(agent, agent.position)

        self.datacollector = mesa.DataCollector(
            model_reporters={}, agent_reporters={}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()