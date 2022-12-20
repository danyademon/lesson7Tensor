import numpy as np

array3x3 = np.random.sample((3,3))

print(f'Матрица 3x3:\n {array3x3}')

array3x3 = array3x3.transpose()

print(f'Транспонированная матрица:\n {array3x3}')
