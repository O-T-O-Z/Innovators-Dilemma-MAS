from src.agents.company import CompanyAgent
import mesa
from src.models.market import MarketModel
from src.agents.company import CompanyAgent
from src import globals
import random


def agent_portrayal(agent):
    base_props = {
        "Filled": "true",
        "Color": agent.get_color()
    }
    
    if isinstance(agent, CompanyAgent):
        base_props["Shape"] = "circle"
        base_props["r"] = 0.7
        base_props["Layer"] = agent.innovation_factor
    else:
        base_props["Shape"] = "rect"
        base_props["w"] = 1
        base_props["h"] = 1
        base_props["Layer"] = 0
    return base_props

slider = mesa.visualization.Slider("Innovation Factor", 0, 0, 100)

grid = mesa.visualization.CanvasGrid(agent_portrayal, globals.WIDTH, globals.HEIGHT, 500, 500)


def get_random_color():
    r = lambda: random.randint(0, 255)
    return "#%02X%02X%02X" % (r(), r(), r())


company_labels = [(f"Company_{x}", get_random_color()) for x in range(globals.NUM_COMPANIES)]
chart_labels = [{"Label": company_labels[i][0], "Color": company_labels[i][1]} for i in range(globals.NUM_COMPANIES)]

chart = mesa.visualization.ChartModule(chart_labels)

model_params = {
    "num_companies": globals.NUM_COMPANIES, 
    "num_customers": globals.NUM_CUSTOMERS, 
    "width": globals.WIDTH, 
    "height": globals.HEIGHT,
    "company_labels": company_labels,
    "title": mesa.visualization.StaticText("Parameters:"),
    **globals.sliders
}

server = mesa.visualization.ModularServer(
    MarketModel, 
    [grid, chart], 
    "Market Model",
    model_params
)



server.port = 8521 # The default
server.launch()
