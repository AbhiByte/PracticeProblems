def strStr(haystack, needle):
        if not haystack and not needle:
            return 0
        return haystack.find(needle)
print(strStr("", ""))
