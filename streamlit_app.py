import streamlit as st
import yfinance as yf
import pandas as pd


ticker = 'MSFT'
rf_monthly = 0.0025  


data = yf.download(ticker, period='5y', interval='1mo')


close_prices = data['Close'][ticker]


monthly_returns = close_prices.pct_change().dropna()


excess_returns = monthly_returns - rf_monthly

mean_excess_return = excess_returns.mean()
std_dev_return = monthly_returns.std()


monthly_sharpe_ratio = mean_excess_return / std_dev_return


st.subheader("Microsoft (MSFT) Sharpe Ratio")

st.metric(
    label="Monthly Sharpe Ratio",
    value=f"{monthly_sharpe_ratio:.3f}"
)



