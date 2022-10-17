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
        self.capital = random.randint(100, 10000)
        self.gamma = model.gamma
        self.max_innovate_time = 20
        # ------------------

        self.budget = self.gamma * self.capital
        self.product = Product()
        self.color = utils.sample_color_rgb_gradient_random(label[2])
        self.type = label[1]

        self.innovation_factor = label[0]
        self.exploitation_factor = 1 - self.innovation_factor
        self.total_innovation = 0
        self.t = 0
        self.n_customers = 1  # prevent immediate removal
        self.has_new_product = False
        self.candidate_product = None
        self.candidate_product_created_at = None
        self.global_t = 0

        self.data = {"Capital": [self.capital], "New Product": [False], "Type": self.type, "Color": self.color}

    def get_color(self):
        return self.color

    def __innovate(self):
        self.total_innovation += self.innovation_factor * random.random()
        # print("adding:", self.innovation_factor * random.random())
        self.t += 1.0
        innovation_cost = self.budget * self.innovation_factor
        self.capital -= innovation_cost
        self.has_new_product = False

        #print("innovation time", self.max_innovate_time, self.total_innovation)
        if self.candidate_product:
            print("candidate product exists for ", self.type)

            self.candidate_product.improve(self.exploitation_factor)

            # Switch to new product?
            if self.candidate_product.get_performance() >= self.product.get_performance():
                self.product = self.candidate_product
                self.candidate_product = None
            # Give up on candidate product?
            elif self.global_t - self.candidate_product_created_at >= 50:
                self.candidate_product = None

            #print(self.global_t, self.t, self.candidate_product)

        # Research and explore
        elif self.t >= self.max_innovate_time:
            #print("here")
            prob = self.total_innovation / self.t
            print(self.type, self.total_innovation, self.t)
            #print(prob, self.total_innovation)
            if prob >= random.random():
                #print("new product emerged", self.global_t, self.t)
                lower_bound = (self.product.pbounds[0] + self.product.pbounds[1]) / 2
                upper_bound = lower_bound + (random.random()*1.1)
                # self.product = Product((lower_bound, upper_bound))
                self.candidate_product = Product((lower_bound, upper_bound))
                self.candidate_product_created_at = self.global_t
                self.has_new_product = True
            # reset
            self.t = 0
            self.total_innovation = 0

        self.data["New Product"].append(self.has_new_product)

    def __exploit(self):
        self.product.improve(self.exploitation_factor)
        exploitation_cost = self.budget * self.exploitation_factor
        self.capital -= exploitation_cost

    def __life_check(self):
        if self.capital < 1:
            self.model.remove_company_agent(self.unique_id)
        self.n_customers = 0

    def __allocate_budget(self):
        self.budget = self.gamma * self.capital

    def step(self):
        self.__innovate()
        self.__exploit()
        self.__life_check()
        self.__allocate_budget()

        self.data["Capital"].append(self.capital)

        self.global_t += 1

    def buy(self):
        self.capital += self.product.gain_on_product
        self.n_customers += 1
