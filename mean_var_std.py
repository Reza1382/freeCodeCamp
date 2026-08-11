import numpy as np


def calculate(list: list):
    if len(list) == 9:
        # convert the list into a numpy array and reshape it to 3x3 shape
        numpy_array = np.array(list)
        main_array = numpy_array.reshape(3, 3)

        # calculating the mean of rows, columns and the matrix
        axis0_mean = [float(x) for x in np.mean(main_array, axis=0)]
        axis1_mean = [float(x) for x in np.mean(main_array, axis=1)]
        mean = [
            axis0_mean,
            axis1_mean,
            float(np.mean(main_array)),
        ]

        # calculating the variance of rows, columns and the matrix
        axis0_var = [float(x) for x in np.var(main_array, axis=0)]
        axis1_var = [float(x) for x in np.var(main_array, axis=1)]
        variance = [
            axis0_var,
            axis1_var,
            float(np.var(main_array)),
        ]

        # calculating the standard deviation of rows, columns and the matrix
        axis0_std = [float(x) for x in np.std(main_array, axis=0)]
        axis1_std = [float(x) for x in np.std(main_array, axis=1)]
        standard_deviation = [
            axis0_std,
            axis1_std,
            float(np.std(main_array)),
        ]

        # calculating the maximum of rows, columns and the matrix
        axis0_max = [float(x) for x in np.max(main_array, axis=0)]
        axis1_max = [float(x) for x in np.max(main_array, axis=1)]
        maximum = [
            axis0_max,
            axis1_max,
            float(np.max(main_array)),
        ]

        # calculating the minimum of rows, columns and the matrix
        axis0_min = [float(x) for x in np.min(main_array, axis=0)]
        axis1_min = [float(x) for x in np.min(main_array, axis=1)]
        minimum = [
            axis0_min,
            axis1_min,
            float(np.min(main_array)),
        ]

        # calculating the sum of rows, columns and the matrix
        axis0_sum = [float(x) for x in np.sum(main_array, axis=0)]
        axis1_sum = [float(x) for x in np.sum(main_array, axis=1)]
        value_sum = [
            axis0_sum,
            axis1_sum,
            float(np.sum(main_array)),
        ]

        calculations = {
            "mean": mean,
            "variance": variance,
            "standard deviation": standard_deviation,
            "max": maximum,
            "min": minimum,
            "sum": value_sum,
        }

        return calculations

    else:
        # print("List must contain nine numbers.", list)
        raise ValueError("List must contain nine numbers.", list)
