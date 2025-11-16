import numpy as np
from utils.tools import help_msg

class Aggregate:
    def __init__(self, arr):
        self.arr = np.array(arr)

    # Correlation Coefficient
    def corr_coef(self, arr2=None):
        try:
            if arr2 is None:
                return np.corrcoef(self.arr)

            nArr2 = np.array(arr2)

            if self.arr.ndim == 1 and nArr2.ndim == 1:
                return np.corrcoef(self.arr, nArr2)[0, 1]

            return np.corrcoef(self.arr, nArr2, rowvar=False)

        except Exception as e:
            return f"Error while finding Correlation Coefficient: {e}\n{help_msg('corr_coef')}"

    # Cumulative Product
    def cum_prod(self, ax=None):
        try:
            return np.cumprod(self.arr, axis=ax) if ax in (0, 1, -1, None) \
                   else (_ for _ in ()).throw(ValueError("Invalid axis. Use '0' for Column-wise."))
        except Exception as e:
            return f"Error while finding Cumulative Product: {e}\n{help_msg('cum_prod')}"

    # Cumulative Sum
    def cum_sum(self, ax=None):
        try:
            return np.cumsum(self.arr, axis=ax) if ax in (0, 1, -1, None) \
                   else (_ for _ in ()).throw(ValueError("Invalid axis. Use '0' for Column-wise."))
        except Exception as e:
            return f"Error while finding Cumulative Sum: {e}\n{help_msg('cum_sum')}"

    # Maximum
    def max(self, ax=None):
        try:
            return np.max(self.arr, axis=ax) if ax in (0, 1, -1, None) \
                   else (_ for _ in ()).throw(ValueError("Invalid axis."))
        except Exception as e:
            return f"Error while finding Maximum: {e}\n{help_msg('max')}"

    # Mean
    def mean(self, ax=None):
        try:
            return np.mean(self.arr, axis=ax) if ax in (0, 1, -1, None) \
                   else (_ for _ in ()).throw(ValueError("Invalid axis."))
        except Exception as e:
            return f"Error while finding Mean: {e}\n{help_msg('mean')}"

    # Median
    def median(self, ax=None):
        try:
            return np.median(self.arr, axis=ax) if ax in (0, 1, -1, None) \
                   else (_ for _ in ()).throw(ValueError("Invalid axis."))
        except Exception as e:
            return f"Error while finding Median: {e}\n{help_msg('median')}"

    # Minimum
    def min(self, ax=None):
        try:
            return np.min(self.arr, axis=ax) if ax in (0, 1, -1, None) \
                   else (_ for _ in ()).throw(ValueError("Invalid axis."))
        except Exception as e:
            return f"Error while finding Minimum: {e}\n{help_msg('min')}"

    # Product of Elements
    def prod(self, ax=None):
        try:
            return np.prod(self.arr, axis=ax) if ax in (0, 1, -1, None) \
                   else (_ for _ in ()).throw(ValueError("Invalid axis."))
        except Exception as e:
            return f"Error while finding Product: {e}\n{help_msg('prod')}"

    # Sum
    def sum(self, ax=None):
        try:
            return np.sum(self.arr, axis=ax) if ax in (0, 1, -1, None) \
                   else (_ for _ in ()).throw(ValueError("Invalid axis."))
        except Exception as e:
            return f"Error while finding Sum: {e}\n{help_msg('sum')}"

    # Variance
    def var(self, method, ax=None):
        if method not in (0, 1):
            raise ValueError("Invalid method. Use 0 for population, 1 for sample.")
        return self.__variance(method, ax)

    # Standard Deviation
    def std_dev(self, method, ax=None):
        if method not in (0, 1):
            raise ValueError("Invalid method. Use 0 for population, 1 for sample.")
        return self.__sd(method, ax)

    # PRIVATE: Variance
    def __variance(self, delta, ax):
        try:
            return np.var(self.arr, axis=ax, ddof=delta)
        except Exception as e:
            return f"Error while finding Variance: {e}\n{help_msg('var')}"

    # PRIVATE: Standard Deviation
    def __sd(self, delta, ax):
        try:
            return np.std(self.arr, axis=ax, ddof=delta)
        except Exception as e:
            return f"Error while finding Standard Deviation: {e}\n{help_msg('std')}"
