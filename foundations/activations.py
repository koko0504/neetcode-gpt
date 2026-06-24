import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        den=1+np.exp(-z)
        sigmoid=1/den
        result= np.round(sigmoid,5)
        return result

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        relu=np.maximum(0,z)
        return relu
