import numpy as np

class LinearRegression:
    x = None
    theta = None
    y = None
    
    def fit(self, x, y):
      """
      >>> import regression
      >>> import datasets
      >>> X, Y = datasets.load_linear_example1()
      >>> import importlib
      >>> model = regression.LinearRegression()
      >>> model.fit(X,Y)
      >>> model.theta
      array([5.30412371, 0.49484536])
      """
      temp = np.linalg.inv(np.dot(x.T, x))
      self.theta = np.dot(np.dot(temp,x.T),y)
      
    def predict(self, x):
        pass
      
    def score(self, x, y):
        pass
      
      
      
if __name__ == "__main__":
  import doctest
  doctest.testmod()