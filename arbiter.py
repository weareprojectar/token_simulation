class Arbiter(object):
    def __init__(self, initial_capital):
        self.INIT_CAPITAL = initial_capital
        self.fund_capital = initial_capital

    def get_init_cap(self):
        return self.INIT_CAPITAL

    def get_current_cap(self):
        return self.fund_capital

    def add_capital(self, capital):
        self.fund_capital += capital
