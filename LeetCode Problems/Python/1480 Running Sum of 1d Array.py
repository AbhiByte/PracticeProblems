list = [3,1,2,10,1] #Expected output -> [1, 4, 9, 15]

def running(arr):
    length = len(arr)
    ans = [None]*length
    ans[0] = arr[0]
    counter = 0
    sum = 0
    for x in range(length):
        counter = x
        while counter >= 0:
            sum += arr[counter]
            counter-= 1
        counter = 0
        ans[x] = sum
        sum = 0
    return ans






