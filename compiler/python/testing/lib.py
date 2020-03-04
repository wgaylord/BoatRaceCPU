from numpy import int8, uint8, int16, uint16, int32, uint32
from numpy import ndarray as __ndarray

def array(type,size):
    return __ndarray(size,type)

