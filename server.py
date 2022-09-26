from src.agents.company import CompanyAgent
import mesa
from src.models.market import MarketModel
from src.agents.company import CompanyAgent
#from test import MarketModel

WIDTH = 10
HEIGHT = 10

def agent_portrayal(agent):
    color = None
    if isinstance(agent, CompanyAgent):
        color = "red"
    else:
        color = "green"
    return {
        "Shape": "circle",
        "Filled": "true",
        "Layer": 0,
        "r": 0.5,
        "Color": color
    }

grid = mesa.visualization.CanvasGrid(agent_portrayal, WIDTH, HEIGHT, 500, 500)
server = mesa.visualization.ModularServer(
    MarketModel, 
    [grid], 
    "Market Model", {
        "num_companies": 5, 
        "num_customers": 20, 
        "width": WIDTH, 
        "height": HEIGHT
    }
)

server.port = 8521 # The default
server.launch()
