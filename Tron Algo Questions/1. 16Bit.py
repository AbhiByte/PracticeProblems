'''Q1. Iterate through str(num) and count number of '1'.
O(n) because iterate through num once'''
def high_bits(num):
    count = 0
    for x in str(num):
        if x == '1':
            count += 1
    if count % 2 == 0:
        return "Even"
    return "Odd"

print(high_bits(10101000101))


#New solution
list_of_nums = []
def sixteenbit (x):
  nums = [int(i) for i in str(x)]

  counter = {}
  for x in nums:
    counter.setdefault(x, 0)
    counter[x] += 1
  if counter[1] % 2 != 0: return 'Odd'
  return 'Even'
print(sixteenbit(101010111))
