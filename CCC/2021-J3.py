inputs = []
condition = True
while condition:
    n = int(input())
    if n != 99999:
        inputs.append(str(n))
    else:
        inputs.append(str(n))
        condition = False
print(f"these are the inputs: {inputs}")
directions = []
steps = []
for nums in inputs:
    if nums != 99999:
        sum = str(nums)[0] + str(nums)[1]
        if int(sum) % 2 != 0:
            directions.append("left")
        elif int(sum) % 2 == 0 and int(sum) != 0:
            directions.append("right")
        else:
            directions.append(directions.pop())
        str_step = str(nums)
        steps.append(int(str_step))
print(f'the steps are {steps}')

for x, y in zip(directions, steps):
    print(x, y)
