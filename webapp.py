import streamlit as st
from datetime import datetime
import time
import pandas as pd
import requests
import numpy as np


def moving_averages(timeframe,Shorter_sma,Longer_sma):
    bullish_crossover = ['bullish crossover', ]
    bearish_crossover = ['bearish crossover', ]
    short_sma_bullish_close = ['Close above Shorter_sma', ]
    long_sma_bullish_close = ['Close above longer_sma', ]
    short_sma_bearish_close = ['Close below shorter_sma', ]
    long_sma_bearish_close = ['Close below longer_sma', ]
    pairs = ['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT',
             'XLMUSDT',
             'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT',
             'BATUSDT',
             'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT',
             'COMPUSDT',
             'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT',
             'DOTUSDT',
             'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'YFIIUSDT', 'RUNEUSDT', 'SUSHIUSDT', 'SRMUSDT', 'BZRXUSDT',
             'EGLDUSDT', 'SOLUSDT', 'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT',
             'ENJUSDT',
             'FLMUSDT', 'TOMOUSDT', 'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT',
             'MATICUSDT',
             'OCEANUSDT', 'CVCUSDT', 'BELUSDT', 'CTKUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT']
    usdt_pairs = []
    btc_pairs = []
    nurl = 'https://www.binance.com/api/v1/ticker/allBookTickers'
    df1 = pd.DataFrame(requests.get(nurl).json())
    columns_new = df1['symbol']
    for i in columns_new:
        if i[-3:] == 'BTC':
            btc_pairs.append(i)
        elif i[-4:] == 'USDT':
            usdt_pairs.append(i)
    new_pairs = ['CAKEUSDT']
    for j in pairs:
        hour = timeframe
        burl = 'https://api.binance.com/api/v3/klines?symbol='
        interval_url = '&interval='
        limit_url = '&limit=1000'
        url = burl + j + interval_url + hour + limit_url
        df = pd.DataFrame(requests.get(url).json())
        df.rename(columns={0: 'DATE', 1: 'OPEN', 2: 'HIGH', 3: 'LOW', 4: 'CLOSE', 5: 'VOLUME', 6: 'CLOSE_TIME',
                           7: 'Quote asset volume', 8: 'Number of trades', 9: 'Taker buy base asset volume',
                           10: 'Taker buy quote asset volume', 11: 'IGNORE'}, inplace=True)
        df = df.drop(columns=['DATE', 'VOLUME', 'CLOSE_TIME', 'Quote asset volume', 'Number of trades',
                              'Taker buy base asset volume',
                              'Taker buy quote asset volume', 'IGNORE'])

        df['shorter_sma'] = df['CLOSE'].rolling(window=int(Shorter_sma)).mean()
        shorter_sma = list(df['shorter_sma'])
        df['longer_sma'] = df['CLOSE'].rolling(window=int(Longer_sma)).mean()
        longer_sma = list(df['longer_sma'])

        if shorter_sma[-3] < longer_sma[-3]:
            if shorter_sma[-2] > longer_sma[-2]:
                bullish_crossover.append(j)
        if shorter_sma[-3] > longer_sma[-3]:
            if shorter_sma[-2] < longer_sma[-2]:
                bearish_crossover.append(j)
        opened = list(df['OPEN'])
        closed = list(df['CLOSE'])
        if float(opened[-2]) < shorter_sma[-2]:
            if float(closed[-2]) > shorter_sma[-2]:
                short_sma_bullish_close.append(j)
        if float(opened[-2]) < longer_sma[-2]:
            if float(closed[-2]) > longer_sma[-2]:
                long_sma_bullish_close.append(j)
        if float(opened[-2]) > shorter_sma[-2]:
            if float(closed[-2]) < shorter_sma[-2]:
                short_sma_bearish_close.append(j)
        if float(opened[-2]) > longer_sma[-2]:
            if float(closed[-2]) < longer_sma[-2]:
                long_sma_bearish_close.append(j)

    tables = [bullish_crossover, bearish_crossover, short_sma_bullish_close, short_sma_bearish_close,
              long_sma_bullish_close, long_sma_bearish_close]
    return tables


def EMA(timeframe,Shorter_ema,Longer_ema):
    bullish_crossover = ['bullish crossover', ]
    bearish_crossover = ['bearish crossover', ]
    short_ema_bullish_close = ['Close above Shorter_ema', ]
    long_ema_bullish_close = ['Close above longer_ema', ]
    short_ema_bearish_close = ['Close below shorter_ema', ]
    long_ema_bearish_close = ['Close below longer_ema', ]
    pairs = ['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'EOSUSDT', 'LTCUSDT', 'TRXUSDT', 'ETCUSDT', 'LINKUSDT',
             'XLMUSDT',
             'ADAUSDT', 'XMRUSDT', 'DASHUSDT', 'ZECUSDT', 'XTZUSDT', 'BNBUSDT', 'ATOMUSDT', 'ONTUSDT', 'IOTAUSDT',
             'BATUSDT',
             'VETUSDT', 'NEOUSDT', 'QTUMUSDT', 'IOSTUSDT', 'THETAUSDT', 'ALGOUSDT', 'ZILUSDT', 'KNCUSDT', 'ZRXUSDT',
             'COMPUSDT',
             'OMGUSDT', 'DOGEUSDT', 'SXPUSDT', 'KAVAUSDT', 'BANDUSDT', 'RLCUSDT', 'WAVESUSDT', 'MKRUSDT', 'SNXUSDT',
             'DOTUSDT',
             'YFIUSDT', 'BALUSDT', 'CRVUSDT', 'TRBUSDT', 'YFIIUSDT', 'RUNEUSDT', 'SUSHIUSDT', 'SRMUSDT', 'BZRXUSDT',
             'EGLDUSDT', 'SOLUSDT', 'ICXUSDT', 'STORJUSDT', 'BLZUSDT', 'UNIUSDT', 'AVAXUSDT', 'FTMUSDT', 'HNTUSDT',
             'ENJUSDT',
             'FLMUSDT', 'TOMOUSDT', 'RENUSDT', 'KSMUSDT', 'NEARUSDT', 'AAVEUSDT', 'FILUSDT', 'RSRUSDT', 'LRCUSDT',
             'MATICUSDT',
             'OCEANUSDT', 'CVCUSDT', 'BELUSDT', 'CTKUSDT', 'AXSUSDT', 'ALPHAUSDT', 'ZENUSDT', 'SKLUSDT']
    usdt_pairs = []
    btc_pairs = []
    nurl = 'https://www.binance.com/api/v1/ticker/allBookTickers'
    df1 = pd.DataFrame(requests.get(nurl).json())
    columns_new = df1['symbol']
    for i in columns_new:
        if i[-3:] == 'BTC':
            btc_pairs.append(i)
        elif i[-4:] == 'USDT':
            usdt_pairs.append(i)
    new_pairs = ['CAKEUSDT']
    for j in pairs:
        hour = timeframe
        burl = 'https://api.binance.com/api/v3/klines?symbol='
        interval_url = '&interval='
        limit_url = '&limit=1000'
        url = burl + j + interval_url + hour + limit_url
        df = pd.DataFrame(requests.get(url).json())
        df.rename(columns={0: 'DATE', 1: 'OPEN', 2: 'HIGH', 3: 'LOW', 4: 'CLOSE', 5: 'VOLUME', 6: 'CLOSE_TIME',
                           7: 'Quote asset volume', 8: 'Number of trades', 9: 'Taker buy base asset volume',
                           10: 'Taker buy quote asset volume', 11: 'IGNORE'}, inplace=True)
        df = df.drop(columns=['DATE', 'VOLUME', 'CLOSE_TIME', 'Quote asset volume', 'Number of trades',
                              'Taker buy base asset volume',
                              'Taker buy quote asset volume', 'IGNORE'])

        df['shorter_ema'] = df['CLOSE'].ewm(span=int(Shorter_ema)).mean()
        shorter_ema = list(df['shorter_ema'])
        df['longer_ema'] = df['CLOSE'].ewm(span=int(Longer_ema)).mean()
        longer_ema = list(df['longer_ema'])

        if shorter_ema[-3] < longer_ema[-3]:
            if shorter_ema[-2] > longer_ema[-2]:
                bullish_crossover.append(j)
        if shorter_ema[-3] > longer_ema[-3]:
            if shorter_ema[-2] < longer_ema[-2]:
                bearish_crossover.append(j)
        opened = list(df['OPEN'])
        closed = list(df['CLOSE'])
        if float(opened[-2]) < shorter_ema[-2]:
            if float(closed[-2]) > shorter_ema[-2]:
                short_ema_bullish_close.append(j)
        if float(opened[-2]) < longer_ema[-2]:
            if float(closed[-2]) > longer_ema[-2]:
                long_ema_bullish_close.append(j)
        if float(opened[-2]) > shorter_ema[-2]:
            if float(closed[-2]) < shorter_ema[-2]:
                short_ema_bearish_close.append(j)
        if float(opened[-2]) > longer_ema[-2]:
            if float(closed[-2]) < longer_ema[-2]:
                long_ema_bearish_close.append(j)

    tables = [bullish_crossover, bearish_crossover, short_ema_bullish_close, short_ema_bearish_close,
              long_ema_bullish_close, long_ema_bearish_close]
    return tables




rad = st.sidebar.selectbox("select",['Moving average crossover', 'EMA crossover'])

if rad == 'Moving average crossover':
    timeframe1,Shorter_sma1,Longer_sma1 = st.beta_columns(3)
    timeframe = str(timeframe1.text_input('Enter the timeframe you want to analyse:'))
    Shorter_sma = Shorter_sma1.text_input('Enter your shorter moving average:')
    Longer_sma = Longer_sma1.text_input('Enter your longer moving average:')
    try:
        st.write(st.table(moving_averages(timeframe,Shorter_sma,Longer_sma)))
    except:
        pass

if rad == 'EMA crossover':
    timeframe1, Shorter_ema1, Longer_ema1 = st.beta_columns(3)
    timeframe = str(timeframe1.text_input('Enter the timeframe you want to analyse:'))
    Shorter_ema = Shorter_ema1.text_input('Enter your shorter EMA:')
    Longer_ema = Longer_ema1.text_input('Enter your longer EMA:')
    try:
        st.write(st.table(EMA(timeframe,Shorter_ema,Longer_ema)))
    except:
        pass

