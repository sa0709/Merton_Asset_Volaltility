# Merton_Asset_Volaltility

This project estimates **asset values and asset volatilities of firms using the Merton Model**. It uses Python and processes financial data from an Excel input file, outputting the results to another Excel file.

***

### Overview

This repository implements a quantitative finance method to solve for a company's asset value and asset volatility using the Merton structural credit risk model. It leverages numerical methods (via `fsolve`) to invert observed equity market data to estimate unobservable firm-level asset characteristics.

***

### How It Works

- Reads company financials from `Input.xlsx` (equity value, net debt, equity volatility, risk-free rate).
- For each row, solves the nonlinear equations from the Merton Model for asset value and volatility using Python and `scipy.stats` and `scipy.optimize`.
- Saves enhanced data with calculated columns to `Output.xlsx`.

***

### File Descriptions

- **Final.ipynb**: Jupyter Notebook containing all code implementation for the Merton Model estimation.
- **Input.xlsx**: Excel file listing required company financial data.
- **Output.xlsx**: Generated Excel file with appended asset values and asset volatilities for each company.

***

### Requirements

- Python 3.12+
- pandas
- scipy
- numpy
- Jupyter Notebook

***

### Usage

1. Place company data in `Input.xlsx` using the structure shown above.
2. Run `Final.ipynb` in Jupyter or as a Python script.
3. Results are written to `Output.xlsx`.

***

### Model Details

The notebook solves the following using the Merton option-pricing equations:

- $$ E = V \cdot N(d_1) - D \cdot e^{-rT}N(d_2) $$
- $$ \sigma_E = N(d_1) \frac{V}{E} \sigma_V $$
- Where:
    - $$ E $$: Market value of equity
    - $$ D $$: Net debt
    - $$ \sigma_E $$: Equity volatility
    - $$ r $$: Risk-free rate
    - $$ V $$: Asset value
    - $$ \sigma_V $$: Asset volatility
    - $$ T $$: Time horizon (set to 1 year)

Numerical methods are used to invert these equations for $$ V $$ and $$ \sigma_V $$.

***

### Contact

For questions or contributions, please raise an issue or submit a pull request.

***

**Enjoy estimating corporate asset values with the Merton Model!**
