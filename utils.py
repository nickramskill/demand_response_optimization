import pandas as pd
import numpy as np
import os

def read_data() -> pd.DataFrame:
    
    filepath = os.path.join('data', '20250301_ercot_price_data.csv')

    try:
        data = pd.read_csv(filepath)
        hub_data = data[data.settlement_point == 'HB_HOUSTON']
        price_data = np.array(hub_data.spp)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    return price_data