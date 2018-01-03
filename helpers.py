import numpy as np
import re


def natural_sort(l): 
    """ Sort list of strings in natural order"""
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)] 
    return sorted(l, key = alphanum_key)


def batch_generator(items, batch_size=128, equal_size=False):
    """Generate batches over the input data. 
    If equal_size is True, generator will stop when left data size will be less than batch_size."""
    i = 0
    stop = batch_size if equal_size else 1

    while True:
        fs = items[i:i+batch_size]
        i += batch_size
        if len(fs) < stop:
            raise StopIteration
        yield fs
            
def norm_values(X, x_min=None, x_max=None):
    """Normalize values from zero to one"""
    x_min = x_min if x_min is not None else np.min(X)
    x_max = x_max if x_max is not None else np.max(X)
    return (X - x_min) / (x_max - x_min + 1e-18)