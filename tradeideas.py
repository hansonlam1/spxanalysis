import datetime as dt
import pandas as pd

# test some trade ideas

def trade8020(df):
    # if the previous day was a 8020 setup long (reverse for shorts)
    # did today retest yesterdays low?
    # and did today close above the yesterdays low?
    If df['nextday8020'].shift() = 'long' and df['low'] < df['low'].shift() and df['close'] > df['low'].shift():
        df['trade8020'] = 'win'
    elif df['nextday8020'].shift() = 'long' and df['low'] < df['low'].shift() and df['close'] < df['low'].shift():
        df['trade8020'] = 'loss'
    elif df['nextday8020'].shift() = 'long' and df['low'] < df['low'].shift() and df['close'] = df['low'].shift():
        df['trade8020'] = 'scratch-unclear'
    elif df['nextday8020'].shift() = 'long' and df['low'] >= df['low'].shift():
        df['trade8020'] = 'notrade'
    elif df['nextday8020'].shift() = 'short' and df['high'] > df['high'].shift() and df['close'] < df['high'].shift():
        df['trade8020'] = 'win'
    elif df['nextday8020'].shift() = 'short' and df['high'] > df['high'].shift() and df['close'] > df['high'].shift():
        df['trade8020'] = 'loss'
    elif df['nextday8020'].shift() = 'short' and df['high'] > df['high'].shift() and df['close'] = df['high'].shift():
        df['trade8020'] = 'scratch-unclear'
    else:
        df['trade8020'] = 'notrade'

    return df