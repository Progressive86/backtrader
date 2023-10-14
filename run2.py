import os, sys, argparse
import pandas as pd
import backtrader as bt #other files in this directory may call "backtrader" instead of "bt"
from strategies.goldencross import GoldenCross
from strategies.BuyHold import BuyHold

#In order to run this file, run this file, trader2.py, and choose a strategy listed below. For example, "python trader2.py golden_cross"
strategies = {
    "golden_cross": GoldenCross,
    "buy_hold": BuyHold
    }

parser = argparse.ArgumentParser()
parser.add_argument("strategy", help="which strategy to run", type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print("invalid strategy, must be one of {}".format(strategies.keys()))
    sys.exit()

#"Cerebro must begin with a capital C"
cerebro = bt.Cerebro() #https://backtrader.com/docu/
cerebro.broker.setcash(1000000)

spy_prices = pd.read_csv("data/SPY_2000-June2023.csv", index_col="Date", parse_dates=True)

feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)

cerebro.addstrategy(strategies[args.strategy])

cerebro.addsizer(bt.sizers.FixedSize, stake=1000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()