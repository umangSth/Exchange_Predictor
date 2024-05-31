
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


    Check For Stationarity:
    Stationarity: Stationarity can be defined in precise mathematical terms, but for our purpose we mean a flat looking series, without trend, constant variance over time, a constant autocorrelation structure(is a way to measure how similar or related a series of data points are to themselves over time) over time and no periodic fluctuations (seasonality). 

    Dickey-Fuller Test: is a statistical test used to check if a time series (a sequence of data points collected or recorded at specific times) is stationary. why check for stationary status, cause it is easier to analyze and make predictions with. how it works, 

    Null Hypothesis (H0): The time series has a unit root (i.e., it is not stationary). This means that the data shows a trend, random walk, or some form of pattern that changes overtime.

        Unit root: if a time series has a unit root, it means that shocks or changes to the series have a permanment effect, and the series tends to wander or drift over time rather than returning to a long-term mean or trend. 

        Random Walk: A series with a unit root. 

    Alternative Hypothesis(H1): The times series does not have a unit root (i.e., it is stationary). This means that the statistical properties of the series, such as mean and variance are constant over time. 

        Mean: the average of all data points; a measure of central tendency.

        Variance: The average of the squared differences from the mean; a measure of how spread out the data points are.


If the data series given is not a stationary, then we apply Differencing, its a technique used in time series analysis to make a non-stationary series stationary. useful, for removing trends and simplifies analysis. 

ACF (Autocorrelation Function) and PACF (Partial Autocorrection Function) are tools used in time series analysis to understand the relationship between data points at different times. they help in identifying patterns and selecting the right models for forecasting. 

ACF: measures how a time series is related to itself at different points in time, known as "lags". In simpler terms, it helps us understand if past values in our data series influence current values and how strong that influence is. ACF calculates the correlation (a statistical measure of how two variables move in relation to each other) between the time series and its lagged version for each lag. correlation values range from -1 to 1
     1 means a perfect positive correlation (the series moves exactly together)
     -1 means a perfect negative correlation (the series moves exactly opposite)
     0 means no correlation (the series does not move together at all)


PACF (Partial Autocorrelation Function): measures the correlation between a time series and its lagged values, after removing the influence of intermediate lags. in simple terms, it helps us identify the direct relationship between a data point and its previous data points, without the influence of other data points in between. 

Similar to ACF, PACF calculates the correlation between the time series and its lagged version. however, PACF removes the effects of intermediate lags when calculating this correlation.
    example: the PACF at lag 1 measures the correlation between today's sales and yesterdays sales, excluding any influence from the sales two days ago or any other days in between. 

    


