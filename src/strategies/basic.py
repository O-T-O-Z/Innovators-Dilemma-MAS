
# Instructs the company how to proceed to the next step
class BasicStrategy:

    def __init__(self, company, innovation_factor=0.2, rd_quality=1) -> None:
        self.company = company
        self.innovation_factor = innovation_factor
        self.exploitation_factor = 1 - innovation_factor
        self.rd_quality = rd_quality
        self.total_innovation = 0
        self.t = 0

    def advance_innovation(self):
        self.total_innovation += self.innovation_factor * self.rd_quality
        self.total_innovation /= self.t

    def execute(self):
        self.advance_innovation()
