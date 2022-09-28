from src.agents.company import CompanyAgent
import mesa
from src.models.market import MarketModel
from src.agents.company import CompanyAgent
from src import globals
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

slider = mesa.visualization.Slider("Innovation Factor", 0, 0, 100)
print("slider value", slider.value)

model_params = {
    "num_companies": 10, 
    "num_customers": 1000, 
    "width": WIDTH, 
    "height": HEIGHT,
    "title": mesa.visualization.StaticText("Parameters:"),
    **globals.sliders
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
