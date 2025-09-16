import numpy as np
from scipy.stats import norm
from scipy.optimize import fsolve
import pandas as pd

def merton_asset_value_vol(dataframe):

    df = dataframe
    # len_ = len(df.index)
    asset_vol = []
    asset_val = []

    n = np.linspace(0,len(df.index)-1,len(df.index)).astype(int)
    
    for i in n:
        
        E, D, sigma_E, r = df.iloc[i]

        T = 1
        
        def equations(vars):
            V, sigma_V = vars
            d1 = (np.log(V / D) + (r + 0.5 * sigma_V**2) * T) / (sigma_V * np.sqrt(T))
            d2 = d1 - sigma_V * np.sqrt(T)

            eq1 = V * norm.cdf(d1) - D * np.exp(-r * T) * norm.cdf(d2) - E
            eq2 = (V / E) * norm.cdf(d1) * sigma_V - sigma_E
            return (eq1, eq2)
        
        V0 = E + D   # asset value ~ equity + debt
        sigmaV0 = sigma_E * E / (E + D)  # rough guess
        V, sigma_V = fsolve(equations, (V0, sigmaV0))

        asset_vol.append(sigma_V)
        asset_val.append(V)

    df['Asset Volatility'] = asset_vol
    df['Asset Value'] = asset_val
    
    return df

df_input = pd.read_excel('Input.xlsx', index_col=0)

df_output = merton_asset_value_vol(df_input)

df_output.to_excel('Output.xlsx')
