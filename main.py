import numpy as np

from arbiter import Arbiter
from tokens import Token
from testnet import TestNet

abt = Arbiter(1000000)
init_cap = abt.get_init_cap()
print('Initial capital of Arbiter fund is: ' + str(init_cap))

t = Token(init_cap)
print('Token released, amount of token is: ' + str(t.INIT_TOKEN_NUM))

testnet = TestNet()
testnet_loop_num = 0
testnet_on = True

while testnet_on:
    if testnet_loop_num < 30:
        inc_dec_factor = 1
    else:
        if np.random.normal(0, 0.1) < 0:
            inc_dec_factor = -1
        else:
            inc_dec_factor = 1
    random_trader_num = np.random.randint(0, 100)
    for i in range(random_trader_num):
        if inc_dec_factor == 1:
            testnet.trader_joined()
        elif inc_dec_factor == -1:
            testnet.trader_left()
    bt_results = [trader.backtest_on_testnet(0, 0.1) for trader in testnet.traders]
    bt_results = np.array(bt_results)
    bt_rank = bt_results.argsort()
    top_rank_num = testnet.total_trader_count//10
    top_traders = []
    for trader_num in range(len(testnet.traders)):
        if bt_rank[trader_num] >= top_rank_num:
            top_traders.append(testnet.traders[trader_num])
    print(top_traders)
    break
    testnet_loop_num += 1
    if testnet_loop_num == 365*3: # 3 years
        testnet_on = False
