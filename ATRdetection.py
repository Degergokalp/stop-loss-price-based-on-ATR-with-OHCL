import pandas as pd


data = pd.read_csv('data.csv')


def calculate_atr(data, period=20):
    
    data['True Range'] = data['high'] - data['low']
    
    
    data['ATR'] = data['True Range']
    atr_sum = data['ATR'].rolling(window=period).sum()
    data.loc[period, 'ATR'] = atr_sum.iloc[period] / period
  
    for i in range(period+1, len(data)):
        true_range = max(
            data.loc[i, 'high'] - data.loc[i, 'low'],
            abs(data.loc[i, 'high'] - data.loc[i-1, 'close']),
            abs(data.loc[i, 'low'] - data.loc[i-1, 'close'])
        )
        data.loc[i, 'True Range'] = true_range
        data.loc[i, 'ATR'] = ((period-1)*data.loc[i-1, 'ATR'] + true_range) / period
    
    return data


def calculate_stop_loss(data, atr_period=20, multiplier=2):
    data = calculate_atr(data, atr_period) # ATR hesapla
    min_val = data.iloc[0]['close']
    max_val = data.iloc[0]['close']
    trendUp = True
    stop_loss = [None] * len(data)
    trend = [trendUp]  # new list to store trend values
    
    for i in range(1, len(data)):
        if trendUp:
            stop_loss[i] = data.iloc[i-1]['close'] - multiplier*data.iloc[i-1]['ATR']
            if data.iloc[i]['low'] < stop_loss[i]:
                trendUp = False
                max_val = data.iloc[i]['high']
                stop_loss[i] = max_val
                min_val = data.iloc[i]['low']
        else:
            stop_loss[i] = data.iloc[i-1]['close'] + multiplier*data.iloc[i-1]['ATR']
            if data.iloc[i]['high'] > stop_loss[i]:
                trendUp = True
                min_val = data.iloc[i]['low']
                stop_loss[i] = min_val
                max_val = data.iloc[i]['high']
        if data.iloc[i]['high'] > max_val:
            max_val = data.iloc[i]['high']
        if data.iloc[i]['low'] < min_val:
            min_val = data.iloc[i]['low']
        
        trend.append(trendUp)  # append current trend value to list

    data['Stop Loss'] = stop_loss
    data['Trend'] = trend  # add trend list as new column
    
    data.to_csv('final.csv', index=False, columns=['Stop Loss', 'Trend'])
    
    return stop_loss

calculate_stop_loss(data)