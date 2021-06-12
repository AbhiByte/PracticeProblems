#Google kickstart, 2020 Round A Problem 1

#First line of input is number of test cases
num_cases = input()
for x in range(len(num_cases)):

    #Taking multiple inputs in same line
    N, B = [int(x) for x in input().split()]
    N_list = input().split()
    temp_ans = 0
    
    for i in range(len(N_list)):
        for j in range(len(N_list)+1):
            if i+j < B:
                temp_ans += 1
    return temp_ans
