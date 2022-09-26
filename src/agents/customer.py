
from mesa import Agent, Model
import numpy as np
from typing import Tuple, List
from src.agents.company import CompanyAgent
        
class CustomerAgent(Agent):

    def __init__(self, unique_id: int, model: Model, position: Tuple):
        super().__init__(unique_id, model)
        self.position = position
        self.satisfaction = 1   # start with full satisfaction
        self.rationality = 1    # i.e. Apple customers have rationality 0
        self.alpha = 1  # importance of the proximity for the customer
        self._supplier_company = None

    
    def _evaluate_company_proximity(self, company: CompanyAgent):
        """
        Computes the Euclidean distance from this customer to a Company.
        """
        return np.linalg.norm(company.position - self.position)
        

    def _evaluate_decision(self, company: CompanyAgent):
        """
        Gets the decision factor based on a company.
        """
        choice = min(self.rationality * company.performance, self.satisfaction)
        proximity = self._evaluate_company_proximity(company)
        return self.alpha * proximity + choice

    def _choose_company(self):
        companies = self.model.get_companies()
        decisions = np.array([self._evaluate_decision(c) for c in companies])
        max_i = np.argmax(decisions)
        self._supplier_company = companies[max_i]

    def step(self):
        self._choose_company()
        self._supplier_company.buy()
