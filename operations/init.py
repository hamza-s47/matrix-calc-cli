import numpy as np
from utils.tools import help_msg

class Init:
    
    # Ones
    def ones(self, row, col=None, dt=None):
        try:
            if dt in ("float", "decimal"):
                dtype=np.float64
            elif dt in ("integer", None):
                dtype=np.int8
            else:
                raise ValueError("Use 'decimal' or 'float' to get values in decimal (float)")
            
            shape = (row, col) if col is not None else (row,)
            return np.ones(shape, dtype=dtype)
        except Exception as e:
            return(f"Error while initializing Ones:{e} \n{help_msg('ones')}")
        
    # Constants
    def constants(self, n, row, col=None, dt=None):
        try:
            if dt in ("float", "decimal"):
                dtype=np.float64
            elif dt in ("integer", None):
                dtype=np.int64
            else:
                raise ValueError("Use 'decimal' or 'float' to get values in decimal (float)")
            
            shape = (row, col,) if col is not None else (row,)
            return np.full(shape,n,dtype=dtype)
        except Exception as e:
            return(f"Error while initializing Constants of {n}:{e} \n{help_msg('constants')}")
    
    # Eye Matrix
    def eye_matrix(self, n, m=None, k=0, dt=None):
        try:
            if dt in ("float", "decimal"):
                dtype = np.float64
            elif dt is None:
                dtype = np.int64
            else:
                raise ValueError("Use 'decimal' or 'float' to get values in decimal (float)")
            return np.eye(N=n, M=m, k=k, dtype=dtype)
    
        except Exception as e:
            return f"Error while initializing Eye Matrix of shape ({n} x {m}): {e} \n{help_msg('eye')}"

        
    # Identity Matrix
    # def idty_matrix(self, n, dt=None):
    #     try:
    #         if dt in ("float", "decimal"):
    #             dtype=np.float64
    #         elif dt in ("integer", None):
    #             dtype=np.int8
    #         else:
    #             raise ValueError("Use 'decimal' or 'float' to get values in decimal (float)")
            
    #         return np.identity(n, dtype=dtype)
    #     except Exception as e:
    #         return(f"Error while initializing Identity Matrix of shape {n}: {e}")
        
    # Linspace
    def linspace(self, start, stop, step=None, dt=None):
        try:
            if dt in ("float", "decimal", None):
                dtype=np.float64
            elif dt in ("integer", "int"):
                dtype=np.int64
            else:
                raise ValueError("Use 'decimal' or 'float' to get values in decimal (float)")
            
            if step is None:
                return np.linspace(start, step)
            else:
                return np.linspace(start, stop, step)
        except Exception as e:
            return(f"Error while initializing Linspace array: {e} \n{help_msg('linspace')}")
        
    # Random
    def random(self, row, col, dt, low, high):
        try:
            shape = (row, col) if col is not None else (row,)
            if dt in ("float", "decimal"):
                return np.random.random(shape).astype(np.float64)
            elif dt in ("integer", "int", None):
                return np.random.randint(low, high, size=shape, dtype=np.int64)
            else:
                raise ValueError("Use 'decimal' or 'float' to get values in decimal (float)")
            
        except Exception as e:
            return(f"Error while initializing Random array: {e} \n{help_msg('random')}")
        
    # Range
    def arr_range(self, start, stop=None, step=1, dt=None):
        try:
            if dt in ("float", "decimal"):
                dtype=np.float64
            elif dt in ("integer", None):
                dtype=np.int64
            else:
                raise ValueError("Use 'decimal' or 'float' to get values in decimal (float)")
            
            if stop is None:
                return np.arange(0, start, step)
            else:
                return np.arange(start, stop, step)
        except Exception as e:
            return(f"Error while initializing Range array: {e} \n{help_msg('arr_range')}")
        
    # Zeros
    def zeros(self, row, col=None, dt=None):
        try:
            if dt in ("float", "decimal"):
                dtype=np.float64
            elif dt in ("integer", None):
                dtype=np.int8
            else:
                raise ValueError("Use 'decimal' or 'float' to get values in decimal (float)")
            
            shape = (row, col) if col is not None else (row,)
            return np.zeros(shape, dtype=dtype)
        except Exception as e:
            return(f"Error while initializing Zeroes: {e} \n{help_msg('zeros')}")