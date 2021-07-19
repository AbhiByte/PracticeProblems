def longest(word1, word2):
    ans = []
    for x, y in zip(word1, word2):
        if x == y:
            ans.append(x)
    print(ans)

longest('cabana', 'banana')
