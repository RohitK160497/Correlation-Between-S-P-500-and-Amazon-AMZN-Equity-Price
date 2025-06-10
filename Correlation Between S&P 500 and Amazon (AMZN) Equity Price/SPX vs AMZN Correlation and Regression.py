import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

# Loading Excel Files
spx = pd.read_excel("SPX_Historical.xlsx")
amzn = pd.read_excel("AMZN_Historical.xlsx")

#  Renaming columns to simplify
spx = spx[['Date', 'Close']].rename(columns={'Close': 'SPX'})
amzn = amzn[['Date', '(R1) Close']].rename(columns={'(R1) Close': 'AMZN'})

#  Converting 'Date' to datetime format
spx['Date'] = pd.to_datetime(spx['Date'])
amzn['Date'] = pd.to_datetime(amzn['Date'])

#  Merging the two datasets on Date
data = pd.merge(spx, amzn, on='Date').sort_values('Date')

# Calculating log returns
data['SPX_Return'] = np.log(data['SPX'] / data['SPX'].shift(1))
data['AMZN_Return'] = np.log(data['AMZN'] / data['AMZN'].shift(1))

# === Drop rows with NaN values (first row will have NaN return) ===
data.dropna(inplace=True)

#  Correlation
correlation = data['SPX_Return'].corr(data['AMZN_Return'])
print(f"Correlation between SPX and AMZN daily log returns: {correlation:.4f}")

# Regression Analysis
X = sm.add_constant(data['SPX_Return'])  # Adds intercept
model = sm.OLS(data['AMZN_Return'], X).fit()
print(model.summary())

# Plotting the Scatter and Regression Line
plt.figure(figsize=(10, 6))
plt.scatter(data['SPX_Return'], data['AMZN_Return'], alpha=0.5, label='Daily Returns')
plt.plot(data['SPX_Return'], model.predict(X), color='red', label='Regression Line')
plt.title('Amazon vs S&P 500 Daily Log Returns')
plt.xlabel('S&P 500 Return')
plt.ylabel('Amazon Return')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#  Time Series Plot of Adjusted Prices
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['SPX'], label='S&P 500 (SPX)', alpha=0.8)
plt.plot(data['Date'], data['AMZN'], label='Amazon (AMZN)', alpha=0.8)
plt.title('Price Time Series: SPX vs AMZN')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#  Rolling Correlation Plot ===
rolling_corr = data['SPX_Return'].rolling(window=60).corr(data['AMZN_Return'])  # 60-day rolling

plt.figure(figsize=(12, 6))
plt.plot(data['Date'], rolling_corr, color='purple')
plt.title('60-Day Rolling Correlation between SPX and AMZN Returns')
plt.xlabel('Date')
plt.ylabel('Correlation')
plt.grid(True)
plt.tight_layout()
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.show()
