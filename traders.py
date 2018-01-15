import numpy as np

class Trader(object):
    def __init__(self, capital):
        self.capital = capital
        self.tokens = 0

    def backtest_on_testnet(self, mean_ret, std_ret):
        result = np.random.normal(mean_ret, std_ret)
        return result

    def add_tokens(self, token_count):
        self.tokens += token_count
