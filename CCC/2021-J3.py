inputs = []
condition = True
while condition:
    n = str(input())
    if int(n) != 99999:
        inputs.append(n)
    elif int(n) == 99999:
        inputs.append(n)
        condition = False

directions = []
steps = []
for nums in inputs:
    if nums != '99999':
        sum = int(nums[0]) + int(nums[1])

        if sum % 2 != 0:
            directions.append("left")
        elif sum % 2 == 0 and sum != 0:
            directions.append("right")
        else:
            directions.append(directions[-1])

        int_steps = int(nums[2] + nums[3] + nums[4])
        steps.append(int_steps)

for x, y in zip(directions, steps):
    print(x, y)
