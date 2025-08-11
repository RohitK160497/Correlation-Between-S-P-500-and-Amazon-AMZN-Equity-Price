# 📊 Correlation Between S&P 500 (SPX) and Amazon (AMZN) Equity Price

## 📌 Overview
This project analyzes the statistical relationship between the **S&P 500 Index (SPX)** and **Amazon.com, Inc. (AMZN)** stock prices.  
The goal is to determine how closely Amazon's equity returns align with the broader market, using **correlation analysis**, **linear regression**, and **rolling correlations**.

We test the hypothesis that Amazon, as a major S&P 500 constituent, shows a **strong positive correlation** with the index.

---

## 🗂 Data Collection
- **Source:** Bloomberg Terminal (`GP` function)
- **Date Range:** May 1, 2020 – May 1, 2025
- **Tickers:**
  - `SPX Index` – S&P 500
  - `AMZN US Equity` – Amazon
- **Fields Used:** Adjusted Closing Prices

Two datasets were exported as Excel files:
- `SPX_Historical.xlsx`
- `AMZN_Historical.xlsx`

---

## 🛠 Methodology
Analysis performed in **Python** using:
- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `statsmodels`

**Steps:**
1. Load and clean SPX & AMZN historical price data.
2. Merge datasets by `Date`.
3. Calculate **daily log returns**.
4. Compute **Pearson correlation coefficient**.
5. Run **OLS regression**:
   - Estimate **β (beta)**, **α (alpha)**, and **R²**.
6. Visualize results:
   - Scatter plot with regression line
   - Time series of adjusted prices
   - **60-day rolling correlation**

---

## 📈 Results
- **Correlation (Pearson):** `0.7086` → Strong positive correlation
- **Regression Output:**
  - **Beta:** `1.4156` → AMZN is more volatile than SPX
  - **Alpha:** `-0.0004` → Statistically insignificant
  - **R²:** `0.502` → 50.2% of AMZN’s return variation explained by SPX

---

## 📊 Visualizations
- Scatter plot: SPX vs AMZN daily returns + regression line
<img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/242b4425-09a2-40ab-b558-7c16c6577fc9" />

- Time series chart: SPX & AMZN adjusted closing prices.
<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/7c747461-1d2c-4937-8a3b-c55db81862e6" />

- Rolling correlation (60-day window)
<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/607f9394-44e8-498b-84d5-e2e86c77b44b" />

  

---

## 💡 Interpretation
- AMZN’s returns are **closely tied** to SPX movements.
- **Beta > 1** indicates higher volatility relative to the market.
- Correlation fluctuates during **market stress** or **company-specific events**.
- Insignificant alpha means no consistent excess return after adjusting for market exposure.

---

## 📌 Conclusion
Amazon’s price behavior is significantly influenced by the S&P 500, with above-market volatility.  
These insights are valuable for **portfolio managers**, **traders**, and **investors** considering AMZN in a diversified portfolio.

---

