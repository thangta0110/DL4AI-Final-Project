import numpy as np



def allocate_weights(num_assets):
    weights = np.ones(num_assets) / num_assets
    return weights