def get_y(m, b, x):
    """Returns y-coordinate for given slope, intercept, and x-coordinate"""
    return m*x + b

def calculate_error(m, b, cs):
    """Returns error between the actual x, y coordinates and the y-coordinate given by estimate linear function y = mx + b"""
    x_point, y_point = cs
    error = abs(get_y(m, b, x_point) - y_point)
   
    return error
  
def calculate_all_error(m, b, points):
    """Returns the sum of all the errors for a given linear function y = mx + b and a list of x-coordinates"""
    return sum(calculate_error(m, b, point) for point in points)


def best_fit(possible_ms, possible_bs, datapoints):
    """Returns the slope, intercept and sum of errors of the best fit line given a set of test data points"""
    smallest_error = float("inf")
    best_m = 0
    best_b = 0

    for m in possible_ms:
        for b in possible_bs:
            all_error = calculate_all_error(m, b, datapoints)
            if all_error < smallest_error:
                best_m = m
                best_b = b
                smallest_error = all_error

    return best_m, best_b, smallest_error