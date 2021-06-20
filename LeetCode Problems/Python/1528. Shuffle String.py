def shuffle(s, indices):
    ans = []
    for x in range(len(s)):
        pos_of_letter = indices.index((x))
        ans.append(s[pos_of_letter])
    final_ans = "".join(ans)
    return final_ans




s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(shuffle(s, indices))
