from mesa import Model
import random
from src.agents.grid_agent import GridAgent
from src.entities.product import Product
from typing import Tuple
from src import utils


class CompanyAgent(GridAgent):

    def __init__(self, unique_id: int, model: Model, position: Tuple, label: Tuple):
        super().__init__(unique_id, model, position)

        # --- PARAMETERS ---
        self.capital = random.randint(100, 200)
        self.gamma = model.gamma
        self.max_patience = model.max_patience
        # ------------------

        self.innovation_time = 20
        self.product = Product(innovation_time=self.innovation_time)
        self.color = utils.sample_color_rgb_gradient_random(label[2])
        self.type = label[1]

        self.innovation_factor = label[0]
        self.exploitation_factor = 1 - self.innovation_factor
        self.total_innovation = 0
        self.n_customers = 1  # prevent immediate removal
        self.has_new_product = False
        self.candidate_product = None
        self.candidate_product_created_at = None
        self.global_t = 0
        self.budget = self.gamma * self.capital

        self.data = {"Capital": [self.capital], "New Product": [False], "Type": self.type, "Color": self.color}

    def get_color(self):
        return self.color

    def __innovate(self):
        self.total_innovation += self.innovation_factor * random.random()

        if self.candidate_product:
            self.candidate_product.improve(self.exploitation_factor)

            # Switch to new product?
            if self.candidate_product.get_performance() >= self.product.get_performance():
                self.product = self.candidate_product
                self.candidate_product = None
            # Give up on candidate product?
            elif self.global_t - self.candidate_product_created_at >= self.max_patience:
                # print("lost patience")
                self.candidate_product = None
        # Research and explore
        else:
            if random.random() <= self.innovation_factor * (self.global_t % self.innovation_time) / self.innovation_time:
                # print("New product introduced", self.global_t)
                lower_bound = (self.product.pbounds[0] + self.product.pbounds[1]) / 2
                perf_interval = self.product.pbounds[1] - self.product.pbounds[0]
                upper_bound = lower_bound + (random.random()*perf_interval)
                self.candidate_product = Product((lower_bound, upper_bound), innovation_time=self.innovation_factor)
                self.candidate_product_created_at = self.global_t
                self.has_new_product = True
            # reset
            self.t = 0

        self.data["New Product"].append(self.has_new_product)

    def __exploit(self):
        self.product.improve(self.exploitation_factor)

    def __life_check(self):
        if self.capital < 1:
            self.model.remove_company_agent(self.unique_id)
        self.n_customers = 0

    def __allocate_budget(self):
        self.budget = self.gamma * self.capital
        self.capital -= self.budget

    def step(self):
        self.__life_check()
        self.__allocate_budget()
        self.__innovate()
        self.__exploit()

        self.data["Capital"].append(self.capital)

        self.global_t += 1

    def buy(self):
        self.capital += self.product.gain_on_product
        self.n_customers += 1
