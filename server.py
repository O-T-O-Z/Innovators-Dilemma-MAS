from src.agents.company import CompanyAgent
import mesa
from src.models.market import MarketModel
from src.agents.company import CompanyAgent
#from test import MarketModel

WIDTH = 50
HEIGHT = 50

def agent_portrayal(agent):
    base_props = {
        "Filled": "true",
        "Layer": 0,
        "Color": agent.get_color()
    }
    
    if isinstance(agent, CompanyAgent):
        base_props["Shape"] = "circle"
        base_props["r"] = 1
    else:
        base_props["Shape"] = "rect"
        base_props["w"] = 0.2
        base_props["h"] = 0.2
    return base_props

model_params = {
    "num_companies": 10, 
    "num_customers": 1000, 
    "width": WIDTH, 
    "height": HEIGHT,
    "title": mesa.visualization.StaticText("Parameters:"),
    "proximity_df": mesa.visualization.Slider("Proximity Decision Factpr", 20, 1, 50),
    "performance_df": mesa.visualization.Slider("Performance Decision Factor", 20, 1, 50),
}

grid = mesa.visualization.CanvasGrid(agent_portrayal, WIDTH, HEIGHT, 500, 500)



server = mesa.visualization.ModularServer(
    MarketModel, 
    [grid], 
    "Market Model",
    model_params
)

server.port = 8521 # The default
server.launch()
