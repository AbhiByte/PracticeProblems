# My solution. Run O(n) since at most one iteration through nums. Uses set which adds memory


class MySolution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = list(set(nums)).sort()
        if len(nums) == 0:
            return 0
        count = 1
        seq = []
        l = 0
        r = 1
        while l < len(nums) - 1:
            if nums[r] == nums[l] + 1:
                count += 1
                l += 1
                r += 1
            else:
                seq.append(count)
                count = 1
                l = r
                r += 1
        seq.append(count)
        return max(seq)


# NC Soluton. Linear time, memory. Similar to mine but uses exact value instead of index
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)  # ensures not repeat nums
        longest = 0
        for num in nums:
            # if its a start of a sequence
            if num - 1 not in nums:
                length = 1
                # while the 'next' num is there add to the length
                while num + length in nums:
                    length += 1
                # longest is the max of the curr length and the overall longest
                # from prev iterations
                longest = max(longest, length)
        return longest


if __name__ == "__main__":
    solution = Solution()

    print(solution.longestConsecutive([10, 4, 3, 99, 2, 54, 1]))  # 4
