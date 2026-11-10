import yfinance as yf
import streamlit as st
import yfinance as yf
# Fetches 5 years of AAPL data and prints the final overall average closing price.
st.title("AAPL 5-Year Average Stock Price")
# Fetch 5 years of historical data for AAPL
data = yf.Ticker("AAPL").history(period="5y")
if not data.empty:
 overall_average = data['Close'].mean()
 st.metric(label="5-Year Average Price", value=f"${overall_average:.2f}")
else:
 st.error("No data found for AAPL.")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
#df = pd.read_csv("msft.csv")



# Set up the 3 tabs on the Dashboard
#tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart"])

# Tab 1: Raw Data
#with tabs[0]:
 #   st.subheader(f"Raw Data for MSFT")
 #   st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
#with tabs[1]:
 #   st.subheader(f"Closing Price for MSFT")
 #   st.line_chart(df['Close'])

# Tab 3: Volume Chart
#with tabs[2]:
 #   st.subheader(f"Volume for MSFT")
 #   st.bar_chart(df['Volume'])
