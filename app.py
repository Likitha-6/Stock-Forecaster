import streamlit as st
from forecast import forecast_stock
from sentiment import get_news_sentiment
from utils import load_stock_data
import plotly.graph_objs as go

st.set_page_config(page_title="📈 Stock Forecasting App", layout="wide")
st.title("📈 Stock Forecast with Sentiment")

ticker = st.text_input("Enter stock ticker (e.g., INFY.NS)", value="TCS.NS")
api_key = st.secrets["NEWSAPI_KEY"] if "NEWSAPI_KEY" in st.secrets else st.text_input("Enter NewsAPI Key")

if st.button("Run Forecast"):
    df = load_stock_data(ticker)
    forecast, model = forecast_stock(df)
    sentiment_score = get_news_sentiment(ticker.split('.')[0], api_key)

    st.subheader("🔮 Forecast")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"], y=df["Close"], mode='lines', name='Actual'))
    fig.add_trace(go.Scatter(x=forecast["ds"], y=forecast["yhat"], mode='lines', name='Forecast'))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📰 News Sentiment Score")
    st.metric(label="Sentiment Score (avg of 10 headlines)", value=round(sentiment_score, 3))
    
    decision = "📈 BUY" if forecast["yhat"].iloc[-1] > df["Close"].iloc[-1] and sentiment_score > 0 else \
               "🔍 HOLD" if sentiment_score >= -0.1 else \
               "🔻 SELL"
    st.success(f"Investment Recommendation: **{decision}**")
