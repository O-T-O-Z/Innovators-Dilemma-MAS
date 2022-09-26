import mesa
from src.models.market import MarketModel

def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}

    return portrayal

grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(
    MarketModel, [grid], "Market Model", {"num_companies": 5, "num_customers": 20, "width": 10, "height": 10}
)
server.port = 8521 # The default
server.launch()
