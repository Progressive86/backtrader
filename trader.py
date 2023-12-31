import backtrader as bt
import datetime
from strategies.strategies import TestStrategy as TestStrategy
#from strategies.sma_signals import SmaCross as TestStrategy

cerebro = bt.Cerebro() #https://backtrader.com/docu/

cerebro.broker.set_cash(1000000)

# Create a Data Feed
data = bt.feeds.YahooFinanceCSVData(
    dataname="oracle.csv",
    # Do not pass values before this date
    fromdate=datetime.datetime(2000, 1, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2000, 12, 31),
    reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(bt.sizers.FixedSize, stake=1000)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
#print(cerebro.)

cerebro.plot()
