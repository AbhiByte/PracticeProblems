# Fall 2023 solution. O(26n) time, O(n) space.
def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    res = 0
    l = 0

    for r in range(len(s)):
        sub_string = s[l : r + 1]
        count.setdefault(s[r], 0)
        count[s[r]] += 1

        compute = len(sub_string) - count[max(count, key=count.get)]

        if compute <= k:
            res = max(res, len(sub_string))
            r += 1
        else:
            do_while = True
            while do_while:
                l += 1
                if l > len(s) - 1:
                    do_while = False
                count[s[l - 1]] -= 1
                if len(s[l : r + 1]) - count[max(count, key=count.get)] <= k:
                    do_while = False

    return res
