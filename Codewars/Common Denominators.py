from math import gcd
def convert_fracts(lst):
    a = []
    for tups in lst:
        a.append(tups[1])
    lcm = 1
    for i in a:
        lcm = lcm*i//gcd(lcm, i)

    ans = []
    for tups in lst:
        for x in range(1, lcm+1):
            if (x / lcm) == (tups[0] / tups[1]):
                ans.append([x, lcm])
    return ans
