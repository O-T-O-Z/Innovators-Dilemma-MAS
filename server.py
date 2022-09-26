from src.agents.company import CompanyAgent
import mesa
from src.models.market import MarketModel
from src.agents.company import CompanyAgent
#from test import MarketModel

WIDTH = 100
HEIGHT = 100

def agent_portrayal(agent):
    base_props = {
        "Filled": "true",
        "Layer": 0,
        "Color": agent.get_color()
    }
    
    if isinstance(agent, CompanyAgent):
        base_props["Shape"] = "circle"
        base_props["r"] = 0.5
    else:
        base_props["Shape"] = "rect"
        base_props["w"] = 0.5
        base_props["h"] = 0.5
    return base_props

grid = mesa.visualization.CanvasGrid(agent_portrayal, WIDTH, HEIGHT, 500, 500)
server = mesa.visualization.ModularServer(
    MarketModel, 
    [grid], 
    "Market Model", {
        "num_companies": 10, 
        "num_customers": 1000, 
        "width": WIDTH, 
        "height": HEIGHT
    }
)

server.port = 8521 # The default
server.launch()
