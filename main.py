import csv
import statistics
import numpy as np

def load_data():
    # Extracting data
    data = list()
    with open('fns_for_model.csv', newline='\n') as csvfile:
        data = list(csv.reader(csvfile, delimiter=';'))

    # First row in data it is row names
    # Delete this row in order to convenient data analyzing
    # Remember this in parameter_names variable
    parameter_names = data[0].copy()
    del data[0]

    # Data processing
    # Transpose data in order to convenient data analyzing
    data = np.array(data, dtype=float)
    data = data.transpose()

    return data, parameter_names

def get_mean_variance(data, parameter_names, parameter_number):
    print(f'Mean     for {parameter_names[parameter_number]} = '
        f'{statistics.mean(data[parameter_number])}') 
    print(f'Variance for {parameter_names[parameter_number]} = '
        f'{statistics.stdev(data[parameter_number])}')

if __name__ == '__main__':
    data, parameter_names = load_data()

    # print mean and variance for all data parameters
    for i in range(1, 17):
        get_mean_variance(data, parameter_names, i)