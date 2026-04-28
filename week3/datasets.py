import numpy as np

def load_linear_example1():
    """
    >>> X, Y = load_linear_example1()
    >>> X[0]
    array([1, 4])
    >>> # int() でラップして、純粋な数値として評価させる
    >>> int(Y[0])
    7
    """
    X = np.array([[1, 4], [1, 8], [1, 13], [1, 17]])
    Y = np.array([7, 10, 11, 14])
    return X, Y

if __name__ == "__main__":
    import doctest
    doctest.testmod()