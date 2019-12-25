from math import log, sqrt, exp
from scipy.stats import norm

def call_option_pricer(spot, strike, maturity, r, vol):
    
    d1 = (log(spot/strike) + (r + 0.5 * vol *vol) * maturity) / vol / sqrt(maturity)
    d2 = d1 - vol * sqrt(maturity)
    
    price = spot * norm.cdf(d1) - strike * exp(-r*maturity) * norm.cdf(d2)
    print(price)

aa = call_option_pricer(1500, 1600, 0.2745, 0.03, 0.25)