import numpy as np

from traders import Trader

class TestNet(object):
    def __init__(self):
        self.testnet_capital = 0
        self.traders = []
        self.total_trader_count = 0
        print('Testnet started...')

    def trader_joined(self):
        capital = np.random.randint(0, 10000000)
        td = Trader(capital)
        self.testnet_capital += td.capital
        self.traders.append(td)
        self.total_trader_count += 1
        print('Current traders on testnet: ' + str(self.total_trader_count))
        print('Testnet capital ammounts to: ' + str(self.testnet_capital))
        print('---------------------------------------------')

    def trader_left(self):
        leaving_trader = self.traders.pop()
        self.testnet_capital -= leaving_trader.capital
        self.total_trader_count -= 1
        print('Current traders on testnet: ' + str(self.total_trader_count))
        print('Testnet capital ammounts to: ' + str(self.testnet_capital))
        print('---------------------------------------------')
