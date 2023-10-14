#this file is a simplier version of "run2.py"
import os, sys, argparse
import backtrader as bt
import pandas as pd
from strategies.goldencross import GoldenCross
from strategies.macd import MACD

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

spy_prices = pd.read_csv('data/SPY_2000-June23.csv', index_col='Date', parse_dates=True)

feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)

cerebro.addstrategy(GoldenCross)
cerebro.addstrategy(MACD)

cerebro.run()
cerebro.plot()

#print(len(self))
#print(self.order)
#print(self.position)