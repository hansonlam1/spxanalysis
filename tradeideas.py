import datetime as dt
import pandas as pd

# test some trade ideas

def trade8020(o,h,l,c,setup,prior_h,prior_l,prior_c):
    # if the previous day was a 8020 setup long (reverse for shorts)
    # did today retest yesterdays low?
    # and did today close above the yesterdays low?
    if setup == 'long':
        if l < prior_l and c > prior_c:
            res = 'win'
        elif l < prior_l and c < prior_c:
            res = 'loss'
        elif l < prior_l and c == prior_c:
            res = 'unclear-scratch'
        else:
            res = 'no trigger'
    elif setup == 'short':
        if h > prior_h and c < prior_c:
            res = 'win'
        elif h > prior_h and c > prior_c:
            res = 'loss'
        elif h > prior_h and c == prior_c:
            res = 'unclear-scratch'
        else:
            res = 'no trigger'
    else:
        res = 'unclear'


    # if (df['nextday8020'].shift().str == 'long') & (df['Low'] < df['Low'].shift()) & (df['Close'] > df['Low'].shift()):
    #     df['trade8020'] = 'win'
    # elif (df['nextday8020'].shift() == 'long') & (df['Low'] < df['Low'].shift()) & (df['Close'] < df['Low'].shift()):
    #     df['trade8020'] = 'loss'
    # elif (df['nextday8020'].shift() == 'long') & (df['Low'] < df['Low'].shift()) & (df['Close'] == df['Low'].shift()):
    #     df['trade8020'] = 'scratch-unclear'
    # elif (df['nextday8020'].shift() == 'short') & (df['High'] > df['High'].shift()) & (df['Close'] < df['High'].shift()):
    #     df['trade8020'] = 'win'
    # elif (df['nextday8020'].shift() == 'short') & (df['High'] > df['High'].shift()) & (df['Close'] > df['High'].shift()):
    #     df['trade8020'] = 'loss'
    # elif (df['nextday8020'].shift() == 'short') & (df['High'] > df['High'].shift()) & (df['Close'] == df['High'].shift()):
    #     df['trade8020'] = 'scratch-unclear'
    # else:
    #     df['trade8020'] = 'notrade'

    return res