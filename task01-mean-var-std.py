# Mean-Variance-Deviation Calculator
import numpy as np

def calculate(list):
    matrix = np.array(list).reshape(3,3)
    calculates = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    # calculate the mean of each column
    column_mean = np.mean(matrix, axis=0).tolist()
    calculates['mean'].append(column_mean)
    # calculate the mean of each row
    row_mean = np.mean(matrix, axis=1).tolist()
    calculates['mean'].append(row_mean)
    # calculate the mean of all elements
    mean_all = np.mean(matrix).tolist()
    calculates['mean'].append(mean_all)

    # calculate the variance of each column
    column_var = np.var ( matrix, axis=0 ).tolist ()
    calculates['variance'].append ( column_var )
    # calculate the variance of each row
    row_var = np.var ( matrix, axis=1 ).tolist ()
    calculates['variance'].append ( row_var )
    # calculate the variance of all elements
    variance_all = np.var ( matrix ).tolist ()
    calculates['variance'].append ( variance_all )

    # calculate the standard deviation of each column
    column_std = np.std ( matrix, axis=0 ).tolist ()
    calculates['standard deviation'].append ( column_std )
    # calculate the standard deviation of each row
    row_std = np.std ( matrix, axis=1 ).tolist ()
    calculates['standard deviation'].append ( row_std )
    # calculate the standard deviation of all elements
    std_all = np.std ( matrix ).tolist ()
    calculates['standard deviation'].append ( std_all )

    # calculate the maximum of each column
    column_max = np.max ( matrix, axis=0 ).tolist ()
    calculates['max'].append ( column_max )
    # calculate the maximum of each row
    row_max = np.max ( matrix, axis=1 ).tolist ()
    calculates['max'].append ( row_max )
    # calculate the maximum of all elements
    max_all = np.max ( matrix ).tolist ()
    calculates['max'].append ( max_all )

    # calculate the minimum of each column
    column_min = np.min ( matrix, axis=0 ).tolist ()
    calculates['min'].append ( column_min )
    # calculate the minimum of each row
    row_min = np.min ( matrix, axis=1 ).tolist ()
    calculates['min'].append ( row_min )
    # calculate the minimum of all elements
    min_all = np.min ( matrix ).tolist ()
    calculates['min'].append ( min_all )

    # calculate the sum of each column
    column_sum = np.sum ( matrix, axis=0 ).tolist ()
    calculates['sum'].append ( column_sum )
    # calculate the sum of each row
    row_sum = np.sum ( matrix, axis=1 ).tolist ()
    calculates['sum'].append ( row_sum )
    # calculate the sum of all elements
    sum_all = np.sum ( matrix ).tolist ()
    calculates['sum'].append ( sum_all )

    return calculates

list1 = [0,1,2,3,4,5,6,7,8]

print(calculate(list1),'\n')

for key, value in calculate(list1).items():
    print(key, ':', value)
