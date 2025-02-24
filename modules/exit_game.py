from interfaces.strategy import Strategy

class ExitGame(Strategy):
    
    def do_algorithm(self):
        input("Thanks for play (Press enter)")
        exit()