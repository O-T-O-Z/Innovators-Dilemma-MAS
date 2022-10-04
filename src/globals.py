import mesa
 
sliders = {
    "proximity_df": mesa.visualization.Slider("Proximity Decision Factor", 20, 1, 50),
    "performance_df": mesa.visualization.Slider("Performance Decision Factor", 20, 1, 50),
    "innovation_factor": mesa.visualization.Slider("Innovation Factor", 0, 0, 100)
}


NUM_COMPANIES = 15
NUM_CUSTOMERS = 385

WIDTH = 20
HEIGHT = 20