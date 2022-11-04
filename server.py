from src.agents.company import CompanyAgent
from src.agents.company_type import CompanyType
import mesa
from src.models.market import MarketModel
from src.agents.company import CompanyAgent
from src import globals

def agent_portrayal(agent):
    base_props = {
        "Filled": "true",
        "Color": agent.get_color(),
        "Layer": 0
    }
    
    if isinstance(agent, CompanyAgent):
        base_props["Shape"] = "circle"
        base_props["r"] = 0.7

        if agent.has_new_product:
            base_props["Shape"] = "rect"
            base_props["Color"] = "black"
            base_props["w"] = 0.4
            base_props["h"] = 0.4
    else:
        base_props["Shape"] = "rect"
        base_props["w"] = 1
        base_props["h"] = 1
        base_props["Layer"] = 0

    return base_props

slider = mesa.visualization.Slider("Innovation Factor", 0, 0, 100)

grid = mesa.visualization.CanvasGrid(agent_portrayal, globals.WIDTH, globals.HEIGHT, 500, 500)

company_labels = [
    (0, CompanyType.F0, "red"),
    (0.1, CompanyType.F1, "purple"),
    (0.2, CompanyType.F2, "black"),
    (0.3, CompanyType.F3, "blue"),
    (0.4, CompanyType.F4, "yellow"),
    (0.5, CompanyType.F5, "green"),
    (0.6, CompanyType.F6, "pink"),
    (0.7, CompanyType.F7, "orange"),
    (0.8, CompanyType.F8, "cyan"),
    (0.9, CompanyType.F9, "magenta"),
    (1, CompanyType.F10, "brown"),
]

chart_labels = [{"Label": x[1].value, "Color": x[2]} for x in company_labels]
chart = mesa.visualization.ChartModule(chart_labels)

model_params = {
    "title": mesa.visualization.StaticText("Parameters:"),
    **globals.sliders
}

table = {}


server = mesa.visualization.ModularServer(
    MarketModel,
    [grid, chart],
    "Market Model",
    model_params
)

server.verbose = False
server.port = 8521 # The default
server.launch()
