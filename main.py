import datetime
import os
import pandas as pd
import calculations as calc


PATH = './data/amzn/'

columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume','Adjustment']
df = pd.DataFrame(columns=columns)

for csvfile in os.listdir(PATH):
    if csvfile.endswith('.csv'):
        t = pd.read_csv(PATH+csvfile)
        df = df.append(t, sort=True)

df.drop_duplicates(subset=columns, keep='first', inplace=True)

# convert date column and sort
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by=['Date'], inplace=True, ascending=True)

# calcs
df['daydirection'] = df.apply(lambda x: calc.daydir(x['Open'], x['Close']),
    axis=1)
df['dayrange'] = df.apply(lambda x: calc.dayrange(x['High'],
    x['Low']),axis=1)
df['nextday8020'] = df.apply(lambda x: calc.nextday8020(x['Open'],
    x['High'], x['Low'],x['Close']),axis=1)
df = calc.opengap(df)
df = calc.smaclose(df, 10, 3)
#df = calc.simpletrend(df, 50)

# ----------------------------------------------------------------------
# analyze the dataframe however you see fit here
# ----------------------------------------------------------------------
# how often do gaps fill for different sized gaps
# break down the fill scenarios
# is a SMA oscillator useful
# how many up and down days in a row occur
#df = df[(df['gapclosed'] == True) & (df['opengap_perc'] < 0.5)]
#df = df[(df['opengap_perc'] < -0.3) | (df['opengap_perc'] > 0.3)]
df.head(60)
table = pd.pivot_table(df, index=['nextday8020'], aggfunc='count')
table
 
#hist = df['opengap_perc'].plot(kind='hist',bins=50,figsize=(12,6))
#hist.plot()
#plt.show()