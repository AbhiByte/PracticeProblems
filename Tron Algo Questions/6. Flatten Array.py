#Not my solution but it works :)
import collections

def flatten(arr):
    if isinstance(arr, collections.Iterable):
        return [a for i in arr for a in flatten(i)]
    else:
        return [arr]

print(flatten([1, 2, [[3], [4, 5], [], 6], 7, [[[8]]]]))
