from src.agents.company import CompanyAgent
import mesa
from src.models.market import MarketModel
from src.agents.company import CompanyAgent
from src import globals

WIDTH = 20
HEIGHT = 20

def agent_portrayal(agent):
    base_props = {
        "Filled": "true",
        "Layer": 0,
        "Color": agent.get_color()
    }
    
    if isinstance(agent, CompanyAgent):
        base_props["Shape"] = "circle"
        base_props["r"] = 0.7
    else:
        base_props["Shape"] = "rect"
        base_props["w"] = 1
        base_props["h"] = 1
    return base_props

slider = mesa.visualization.Slider("Innovation Factor", 0, 0, 100)
print("slider value", slider.value)

model_params = {
    "num_companies": globals.NUM_COMPANIES, 
    "num_customers": globals.NUM_CUSTOMERS, 
    "width": WIDTH, 
    "height": HEIGHT,
    "title": mesa.visualization.StaticText("Parameters:"),
    **globals.sliders
}


grid = mesa.visualization.CanvasGrid(agent_portrayal, WIDTH, HEIGHT, 500, 500)


chart = mesa.visualization.ChartModule(
    [{"Label": "Label_1", "Color": "Blue"}, {"Label": "Label_2", "Color": "Green"}]
    )


server = mesa.visualization.ModularServer(
    MarketModel, 
    [grid, chart], 
    "Market Model",
    model_params
)



server.port = 8521 # The default
server.launch()
