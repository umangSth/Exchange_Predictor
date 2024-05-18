import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

# Load your data
data = pd.read_csv('exchange_rate_data.csv')
data['Date'] = pd.to_datetime(data['Date'])
# set data column as index, which enables time-series related analysis
data.set_index('Date', inplace=True)

# check for stationarity
# this is used to perform the Augmented Dickey-Fuller test for stationarity
# on the 'Rate' column of the dataFrame 'data'. This test is a statistical test
# used to determine whether a given time series is stationary.
result = adfuller(data['Rate'])
# ADF Statistic is a negative number, and a more negative value indicates stronger evidence against the null
# hypothesis (data is stationary)
print('ADF Statistic:', result[0])
# The p-value is probability value, and a smaller p-value suggests stronger evidence against the null hypothesis
print('p-value:', result[1])

# If the series is not stationary, apply differencing
if result[1] > 0.05:
    # if the series is not stationary, apply differencing
    # Differencing is used to transform a non-stationary time series into a stationary one
    # by removing trends or seasonality. The result of this operation is a new series where each
    # value is the difference between the current and the previous value in the original 'Rate' column
    # the 'dropna()' method removes any 'NaN' (Not a Number) values from the resulting
    # The purpose of this line is to create a new time series, "data_diff", this series is often used to
    #  - remove trends and seasonality from the data
    #  - Make the time seriese stationary, which is a requirement for many times series models, including ARIMA
    data_diff = data['Rate'].diff().dropna()
    d = 1  # First differencing
    print('Data differenced to achieve stationarity.')
else:
    data_diff = data['Rate']
    d = 0
    print('Data is already stationary.')




# Plot ACF and PACF
# this is to plot the Autocorrection Function (ACF) and the Partial Autocorrection Function (PACF) of the
# differenced time series data. These plots help in identifying the properties of the time
#
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# create a subplots side by side(1,2) and figsize(16,adfuller 6)
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
# this plots the autocorrelation function of the differenced data (`data_diff`).
# the 'ax=axes[0]' argument specifies that the ACF plot should be drawn on the first subplot
plot_acf(data_diff, ax=axes[0])
# this function plots the partial autocorrelation function of the differenced data ('data_diff').
# the 'ax=axes[1]' argument specifies that the pACF plot should be drawn on the second subplot
plot_pacf(data_diff, ax=axes[1])
plt.show()

# Based on the plots, identify p and q
# For example, if ACF cuts off after lag 1, q=1
# If PACF cuts off after lag 1, p=1
# Replace these values based on your ACF and PACF analysis
p = 1  # Placeholder, replace with your identified p value
q = 1  # Placeholder, replace with your identified q value

# Fit the ARIMA model
# the 'order' parameter specifies the (p,d,q) parameters for the ARIMA model
# 'p' the number of lag observations included in the model (Autoregressive part)
# 'd' the number of times that the raw observations are differenced (integrated part)
# 'q' the size of the moving average window( Moving average part)
model = ARIMA(data['Rate'], order=(p, d, q))
# method esitmates the model parameters (coefficients) based on the data
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())

# Forecast
# will generate forecasts for the next 30 time steps, along with standard errors and confidence intervals
forecast, stderr, conf_int = model_fit.forecast(steps=30)

# plot the results
plt.figure(figsize=(10, 6))
plt.plot(data['Rate'], label='Historical')
plt.plot(pd.date_range(start=data.index[-1], periods=31, freq='D')[1:], forecast, label='Forecast')
plt.fill_between(pd.date_range(start=data.index[-1], periods=31, freq='D')[1:], conf_int[:, 0], conf_int[:, 1],
                 color='k', alpha=.15)
plt.legend()
plt.show()
