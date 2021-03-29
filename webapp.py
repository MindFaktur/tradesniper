import streamlit as st
from datetime import datetime
import time
import pandas as pd
import requests
import numpy as np
import functions



rad = st.sidebar.selectbox("select",['Moving average crossover', 'EMA crossover'])

if rad == 'Moving average crossover':
    timeframe1,Shorter_sma1,Longer_sma1 = st.beta_columns(3)
    timeframe = str(timeframe1.text_input('Enter the timeframe you want to analyse:'))
    Shorter_sma = Shorter_sma1.text_input('Enter your shorter moving average:')
    Longer_sma = Longer_sma1.text_input('Enter your longer moving average:')
    try:
        st.write(st.table(functions.moving_averages(timeframe,Shorter_sma,Longer_sma)))
    except:
        pass

if rad == 'EMA crossover':
    timeframe1, Shorter_ema1, Longer_ema1 = st.beta_columns(3)
    timeframe = str(timeframe1.text_input('Enter the timeframe you want to analyse:'))
    Shorter_ema = Shorter_ema1.text_input('Enter your shorter EMA:')
    Longer_ema = Longer_ema1.text_input('Enter your longer EMA:')
    try:
        st.write(st.table(functions.EMA(timeframe,Shorter_ema,Longer_ema)))
    except:
        pass

