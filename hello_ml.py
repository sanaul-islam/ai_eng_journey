import sys 
import pandas as pd
import numpy as np

print(f"python version: {sys.version}")
print(f"pandas version: {pd.__version__}")
print(f"numpy version: {np.__version__}")

arry = np.array([[1, 2, 3], [4, 5, 6]])
print(f"array mean: {arry.mean()}")
