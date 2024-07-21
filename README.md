[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/HfhAxLC5)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15411907&assignment_repo_type=AssignmentRepo)
# EPAi v5 -  Session 5 - Functional Parameters

## Session 5 Topics

DocStrings and Annotations \
Lambda Expressions \
Lambdas and Sorting \
Function Introspection \
Callables \
Map, Filter and Zip \
Reducing Functions \
Partial Functions \ 
Operator Module \

This assigment consists of the implementation of following fuctions: 

### Time It Function
This function  gives out the average run time per call, such that its definition is:

def time_it(fn, *args, repetitons= 1, **kwargs): your code comes here.

We should be able to call it like this:

time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitons=5) \
time_it(squared_power_list, 2, start=0, end=5, repetitons=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32] \
time_it(polygon_area, 15, sides = 3, repetitons=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon \
time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100) # 100 is the base temperature given to be converted \
time_it(speed_converter, 100, dist='km', time='min', repetitons=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by the user is in kmph \

#### Code

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
    if (not isinstance(repetitions, (int))) or repetitions < 0 :
        raise ValueError("repetitions should be an integer number with value >= 0")

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
    if not isinstance(number, int):
        raise TypeError("Only integer type arguments are allowed")

    if not isinstance(start, int):
        raise TypeError("start should be an integer")

    if not isinstance(end, int):
        raise TypeError("end should be an integer")

    if (start < 0) or (end < 0) :
        raise ValueError("Value of start or end can't be negative")

    if start > end:
        raise ValueError("Value of start should be less than end")

    if number > 10:
        raise ValueError("Value of number should be less than 10")

    if(len(args) > 0):
        raise TypeError("Function takes maximum 1 positional arguments")

    if(len(kwargs) > 0):
        raise TypeError("Function takes maximum 2 keyword/named arguments")

    # Return the list of number to the power of numbers from start to end
    powered_list = [pow(number,i) for i in range(start,end)]
    return powered_list


def polygon_area(length, *args, sides = 3, **kwargs):
    import math
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""

    # Validations

    if len(args) > 0:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")

    if len(kwargs) > 0:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")

    if not isinstance(length, int):
        raise TypeError("length should be an integer")

    if not isinstance(sides, int):
        raise TypeError("sides should be an integer")

    if ((sides < 3) or (sides > 6)):
        raise ValueError("3 <= sides <= 6")

    area = 0

    match sides:
        case 3:
            area = ((length ** 2) * math.sqrt(3)) / 4

        case 4:
            area = length ** 2

        case 5:
            area = ((1/4) * math.sqrt((5*(5+(2*math.sqrt(5))))) * (length ** 2))

        case 6:
            area = (((3 * math.sqrt(3)) / 2) * (length ** 2))

    # Return area
    return area

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations

    if not isinstance(temp_given_in,str):
        raise TypeError("Charcater string expected for temp_given_in")
    if not temp_given_in in ('f','c','F','C'):
        raise ValueError("Only f or c is allowed")
    if not isinstance(temp,int):
        raise TypeError("Only integer type arguments are allowed for temp")
    if len(args) > 0:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")

    # Return the converted temprature
    if temp_given_in in ('f','F'):
        if (temp < -459.67):
            raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
        Celsius_temp = (temp - 32) * 5.0 / 9.0
        return Celsius_temp
    elif temp_given_in in ('c','C'):
        if (temp < -273.15):
            raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
        farenheit_temp = ((temp * 9.0) / 5.0) + 32
        return farenheit_temp
    pass

def speed_converter(speed, *args, dist='KM', time='MIN', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Validations
    if not isinstance(speed, (int, float)):
        raise TypeError("Speed can be int or float type only")
    if not isinstance(dist, str):
        raise TypeError("Charcater string expected for distance unit")
    if not isinstance(time, str):
        raise TypeError("Charcater string expected for time")
    if not dist in ('KM','M','FT','YRD'):
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
    if not time in ('MIN','MS','S','HR','DAY'):
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed'")
    if speed < 0:
        raise ValueError("Speed can't be negative")
    if speed > 300000:
        raise ValueError("Speed can't be greater than speed of light")
    if len(args) > 0:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs) > 0:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")

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

    # Convert to desired distance unit
    speed_in_dist = speed * dist_factors[dist]
    # Convert to desired time unit
    converted_speed = speed_in_dist / time_factors[time]
    # Return the converted speed
    return round(converted_speed)
    

