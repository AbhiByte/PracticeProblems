def lengthOfLongestSubstring(s):
    charSet = set()
    count = 0
    l = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        count = max(count, r-l+1)
    return count
