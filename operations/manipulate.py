import numpy as np
from utils.tools import help_msg

class Manipulate:
    def __init__(self, arr):
        self.arr=np.array(arr)
        
    def flatten(self):
        try:
            return self.arr.flatten()
        except Exception as e:
            return f"Error while Flattening: {e} \n{help_msg('flatten')}"
        
    def ravel(self):
        try:
            return self.arr.ravel()
        except Exception as e:
            return f"Error while Raveling: {e} \n{help_msg('ravel')}"
        
    def sorting(self, ax):
        try:
            if ax in (1, -1, 0):
                return np.sort(self.arr, axis=ax)
            elif ax is None:
                return (np.sort(self.arr))
            else:
                raise ValueError("Invalid axis value, use '0' for Column-wise")
        except Exception as e:
            return f"Error while Sorting: {e} \n{help_msg('sort')}"
        
    def transpose(self):
        try:
            return self.arr.T
        except Exception as e:
            return f"Error while Transposing: {e} \n{help_msg('transpose')}"