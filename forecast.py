
from prophet import Prophet
import pandas as pd

def forecast_stock(df, days=30):
    df_prophet = df.reset_index()[["Date", "Close"]]
    df_prophet.columns = ["ds", "y"]

    model = Prophet(daily_seasonality=True)
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    return forecast, model
