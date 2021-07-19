#Q58 LeetCode
def lengthOfLastWord(s):
    #Empty strings can be treated as bool vals
    if not s.strip():
        return 0
    word_list = s.split()
    return len(word_list[-1])
