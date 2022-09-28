
class BasicStrategy:

    def __init__(self, company, innovation_factor=0.2, rd_quality=1) -> None:
        self.company = company
        self.innovation_factor = innovation_factor
        self.rd_quality = rd_quality
        self.total_innovation = 0
        self.t = 0

    def innovate(self):
        self.total_innovation += self.innovation_factor * self.rd_quality
        self.t += 1
    
    def execute(self):
        self.innovate()
        self.total_innovation /= self.t
        pass