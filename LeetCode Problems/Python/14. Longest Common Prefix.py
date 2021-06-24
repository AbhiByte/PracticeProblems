#To finish

lst = ['hello', 'hell', 'hehe']

ans = []
for item in lst:
    new_item = list(item)
    ans.append(new_item)
print(ans)


for i in ans:
    for j in ans[i]:
