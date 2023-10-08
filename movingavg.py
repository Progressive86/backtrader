#trader.py code can be followed to incorporate this strategy into backtrader and plot the data. 

closing_price_sum = 0 

with open("data/SPY_2000-June'23.csv") as f:
    content = f.readlines()[-200:]
    for line in content:
        print(line)
        tokens = line.split(",")
        close = tokens[4]

        closing_price_sum += float(close)

print(closing_price_sum)        
    
    #content = f.readlines()
    #print(content)