'''Q3. O(n) because check numbers up to n. Try to find better solution'''
import math
def is_it_prime(num):
    if num == 1:
        return "Not prime"
    for x in range(2, num-1):
        if num%x == 0:
            return "Not prime"
    return "Prime"
