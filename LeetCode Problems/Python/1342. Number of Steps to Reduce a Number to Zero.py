def numberOfSteps(num, counter = 0):
    if num == 0:
        return counter
    elif num % 2 == 0:
        return numberOfSteps(num/2, counter+1)
    else:
        return numberOfSteps(num-1, counter+1)


print(numberOfSteps(150))
