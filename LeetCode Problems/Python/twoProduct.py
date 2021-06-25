#brute force method

def two_product_brute(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] * nums[j] == target:
                return nums[i], nums[j]

#optimized
def two_product_opt(nums, target):
        count = []
        for x in nums:
            if x not in count:
                count.append(x)
            elif target/x in count:
                return int(target/x), x
#print(two_product_brute([1, 2, 6, 5, 3, 4], 20))
print(two_product_opt([1, 2, 6, 5, 3, 4], 20))
