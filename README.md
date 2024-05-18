
As, I have two account, one in USD and CAD, I want to make something to predict when to do the exchange, so I can make some side money. 
I will be using ChatGPT, other stuffs, as go. 

Lets start,

This is Note for me:

ARIMA Model: Its a popular statistical method for time series forecasting, using three components: autoregression(AR), Differencing (I for integrated), and moving average(MA).

-> AutoRegressive Part: it is a statistical technique used in time-series analysis that assumes that the current value of a time series is a function of its past value. This component captures the relationship between an observation and a number of lagged observations(previous values). represented by 'p'.

-> Integrated(I) part: This component involves differencing the time series data to make it stationary ( removing trends and seasonality). Represented by 'd'

-> Moving Average (MA): This component captures the relationship between an observation and residual error from a moving average model applied to lagged observations. represented by 'q'.

 --> Observation: refers to an individual data point in the time series. 
 --> Residual Error, simply, residual, is the difference between the actual obeserved value and the value predicted by the model. 

Steps to Implement ARIMA:
    ---> Check for Stationarity
    ---> Differencing
    ---> Identify AR and MA Terms
    ---> Fit the ARIMA Model
    ---> Forecasting

