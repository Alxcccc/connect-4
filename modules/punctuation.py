from modules.logging import Connecta4Logging
from interfaces.punctuation import Punctuation

class Connect4Punctuation(Punctuation):
    
    def __init__(self, logging: Connecta4Logging):
        self.points = {"R": 0, "B": 0}
        self.logging = logging
    
    def show(self):
        print(self.points)
        
    def increment_points(self, user: str):
        if user in self.points:
            self.points[user] += 1
            return None
        self.logging.info(f"The user is not valid: {user}")
    
    def reset_point(self):
        if self.points["R"] != 0:
            self.points["R"] = 0
        elif self.points["B"] != 0:
            self.points["B"] = 0