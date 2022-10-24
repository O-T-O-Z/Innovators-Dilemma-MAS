from mesa import Model
import numpy as np
from typing import Tuple
from src.agents.grid_agent import GridAgent
from src.agents.company import CompanyAgent
import random 

class CustomerAgent(GridAgent):

    def __init__(self, unique_id: int, model: Model, position: Tuple):
        super().__init__(unique_id, model, position)
        self.alpha = model.alpha  # importance of the proximity for the customer
        self._supplier_company = self._choose_closest_company()

    def get_color(self):
        return self._supplier_company.get_color() if self._supplier_company else "gray"

    def _evaluate_company_proximity(self, company: CompanyAgent):
        """
		Computes the Euclidean distance from this customer to a Company.
		"""
        return 1 - np.linalg.norm(company.position - self.position) / np.sqrt(self.model.width**2 + self.model.height**2)

    def _evaluate_decision(self, company: CompanyAgent):
        """
		Gets the decision factor based on a company.
		"""
        proximity = self._evaluate_company_proximity(company)
        companies = self.model.get_companies()
        performances = np.array([c.product.performance for c in companies])
        performance_factor = (company.product.performance - performances.min()) / (performances.max() - performances.min())
        proximity_factor = self.alpha * proximity
        f = proximity_factor + performance_factor
        return f

    def _choose_closest_company(self):
        companies = self.model.get_companies()
        decisions = np.array([self._evaluate_company_proximity(c) for c in companies])
        max_i = np.argmax(decisions)
        return companies[max_i]

    def _choose_company(self):
        companies = self.model.get_companies()
        decisions = np.array([self._evaluate_decision(c) for c in companies])
        max_i = np.argmax(decisions)
        candidate_company = companies[max_i]
        if candidate_company.product.performance - self._supplier_company.product.performance >= np.random.rand():
            self._supplier_company = candidate_company


    def step(self):
        self._choose_company()
        self._supplier_company.buy()
