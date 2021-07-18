def high_bits(num):
    count = 0
    for x in str(num):
        if x == '1':
            count += 1
    if count % 2 == 0:
        return "Even"
    return "Odd"

print(high_bits(10101000101))
