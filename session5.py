"""TSAI - EPAi-V5 Assignment 5 - Functional Parameters"""

import time
from time import perf_counter
import types

def time_it(fn, *args, repetitions= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""
    from functools import reduce
    time_taken_cache = []
    # Repetition should be positive number
    if (not isinstance(repetitions, (int))) or repetitions < 1 :
        raise ValueError("repetitions should be an integer number with value >= 1")

    # if not isinstance(fn, types.FunctionType):
    #     raise ValueError("First argument should be a function")
    
    if repetitions == 0:
        return 0

    if fn.__name__ in ('print', 'squared_power_list','polygon_area','temp_converter','speed_converter'):
        raise ValueError("time_it can't time " + fn.__name__ + " function")

    for i in range [0:repetitions]:
        start_time = perf_counter()
        fn(*args, **kwargs)
        time_taken = perf_counter() - start_time
        time_taken_cache.append(time_taken)
    sum_time = reduce(lambda x, y: x*y, time_taken_cache, 0)
    average_time = sum_time/len(time_taken_cache)
    return average_time

def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    from decimal import Decimal

    # Validations "if" block
    if not isinstance(number, (int, float, Decimal)):
        raise ValueError("number should be an integer, float or decimal number")

    if not isinstance(start, int):
        raise ValueError("start should be an integer")

    if not isinstance(end, int):
        raise ValueError("end should be an integer")

    # Return the list of number to the power of numbers from start to end
    powered_list = [pow(number,i) for i in range[start:end]]
    return powered_list


def polygon_area(length, *args, sides = 3, **kwargs):
    import math
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Validations
    if not sides < 3 or sides > 6:
        raise ValueError("3 <= sides <= 6")

    # Return area
    area = (length * sides**2) / (4 * math.tan(math.pi / length))
    return area

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations
    if not temp_given_in in ('f','c'):
        raise ValueError("temp_given_in should be 'f' or 'c'")

    # Return the converted temprature
    if temp_given_in == 'f':
        Celsius_temp = (temp_given_in - 32) * 5.0 / 9.0
        return Celsius_temp
    elif temp_given_in == 'c':
        farenheit_temp = temp_given_in * 9.0 / 5.0 + 32
        return farenheit_temp
    pass

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Validations
    if not isinstance(speed, (int, float)):
        raise TypeError("int/float string expected for speed")
    if not isinstance(dist, str):
        raise TypeError("Charcater string expected for dist")
    if not isinstance(time, str):
        raise TypeError("Charcater string expected for time")
    if not dist in ('km','m','ft','yrd'):
        raise (ValueError,"dist should be 'KM','M','FT','YRD'")
    if not time in ('MIN','MS','S','HR','DAY'):
        raise ValueError("time should be 'min','ms','s','hr', or 'day'")

    #I copied from chat GPT though :(
    # Conversion factors
    dist_factors = {
        'KM': 1,
        'M': 1000,
        'FT': 3280.84,
        'YRD': 1093.61
    }

    time_factors = {
        'MS': 3600000,
        'S': 3600,
        'MIN': 60,
        'HR': 1,
        'DAY': 1/24
    }

    # Convert speed to km/min
    speed_km_per_min = speed / 60.0

    # Convert to desired distance unit
    speed_in_dist = speed_km_per_min * dist_factors[dist]
    # Convert to desired time unit
    converted_speed = speed_in_dist / time_factors[time]
    # Return the converted speed
    return converted_speed