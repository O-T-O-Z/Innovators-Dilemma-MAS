import enum
from src.agents.company import CompanyAgent
from src.agents.company_type import CompanyType
import mesa
from src.models.market import MarketModel
from src.agents.company import CompanyAgent
from src import globals
import random
import itertools

enum
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

company_labels = [
    (0, CompanyType.EXPLOITER, "red"), 
    (0.5, CompanyType.BALANCED, "green"), 
    (0.7, CompanyType.INNOVATOR, "blue")
]

chart_labels = [{"Label": x[1].value, "Color": x[2]} for x in company_labels]

chart = mesa.visualization.ChartModule(chart_labels)

agents_per_class = 5
company_labels = list(itertools.chain(*[[c] * agents_per_class for c in company_labels]))
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



server.port = 8522 # The default
server.launch()
