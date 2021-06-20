def interpret(command):
    ans = []
    #'G()()(al)'

    for x in range(len(command)):
        if command[x] == "G":
            ans.append(command[x])
        if command[x] == "(" and command[x+1] == ")":
            ans.append("o")
        if command[x] == "(" and command[x+1] == "a" and command[x+3] == ")":
            ans.append("al")
    string = "".join(ans)
    return string

print(interpret("(al)G(al)()()G"))
