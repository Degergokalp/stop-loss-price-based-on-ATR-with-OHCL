# stop-loss-price-based-on-ATR-with-OHCL
This repository contains a Python script that implements an automated stop-loss strategy for trading using the Average True Range (ATR) indicator. The strategy calculates the ATR of a given period and multiplies it by a user-defined multiplier to determine the stop-loss level for each trade.

The script reads historical price data from a CSV file and calculates the ATR and stop-loss levels for each data point. The results are stored in a new CSV file that contains the stop-loss levels and a flag indicating whether the market is in an uptrend or downtrend.

Please note that this script is for academic purposes only and should not be used for real trading. It is intended to be used as a starting point for learning about automated trading strategies and can be customized to suit individual needs. Trading involves a high level of risk, and past performance is not indicative of future results.

The script uses the Pandas library for data manipulation and provides the option to customize the ATR period and stop-loss multiplier.

Feel free to use this script and modify it to your liking, but please exercise caution and conduct thorough research before implementing any trading strategies.
