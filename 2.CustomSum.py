"""
Summing n numbers without using the inbuilt sum function, argument will be passed as comma separated values.
"""
import math
from statistics import mean
def mysum(*args):
    total = 0
    for item in args:
        total = total + item
    mean_res = mean(args)
    return total,mean_res


def mysum_num_char_mixed(*args):
    """
    values like 4,5,6, 'a',":" should be handled.
    :param args:
    :return:
    """
    res = sum(filter(lambda x : isinstance(x,int), args))
    return res
if __name__ == '__main__':
    print("Calling main!")
    res = mysum(4,5,6)
    print(f"sum is {res[0]}")
    print(f"mean is {res[1]}")
    print(mysum_num_char_mixed(1,2,3,'a',":",1,10))
