from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import matplotlib.pyplot as plt

# Assuming `data` is your DataFrame and 'Rate' is the column you're forecasting
data = pd.read_csv('exchange_rate_data.csv')  # Replace with your actual data source


# Here, p,d,q = 1, 1, 1, these value are from plot Acf_Pacf.py
# p is the number of lag observations included in the model (autoregressive part).
# d is the number of times the raw observations are differenced (integrated part).
# q is the size of the moving average window (moving average part).
# Fit the ARIMA model
p, d, q = 1, 1, 1
# initializing the ARIMA model with these parameters, using "Rate" column
model = ARIMA(data['Rate'], order=(p, d, q))
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())

# Forecast
# forecast for the next 30 steps(in this case days)
forecast_result = model_fit.get_forecast(steps=30)
# extracts the forecasted values(predicted future rates)
forecast = forecast_result.predicted_mean
# this extracts the standard errors of the forecasted values,
# which give an indication of the forecast's accuracy
stderr = forecast_result.se_mean
# this gets the confidence intervals for the forecasts, which show the range within which
# the true values are likely to fall
conf_int = forecast_result.conf_int()

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(data['Rate'], label='Historical')
plt.plot(pd.date_range(start=data.index[-1], periods=31, freq='D')[1:], forecast, label='Forecast')
plt.fill_between(pd.date_range(start=data.index[-1], periods=31, freq='D')[1:], conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='k', alpha=.15)
plt.legend()
plt.show()
