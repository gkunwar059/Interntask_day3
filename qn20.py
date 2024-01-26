# 20. Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]


class ThreeSumZero:
    def __init__(self, nums):
        self.nums = sorted(nums)

    def find_triplets(self):
        result = []
        for i in range(len(self.nums) - 2):
            l = i + 1
            r = len(self.nums) - 1
            while l < r:
                s = self.nums[i] + self.nums[l] + self.nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append([self.nums[i], self.nums[l], self.nums[r]])
                    while l < r and self.nums[l] == self.nums[l + 1]:
                        l += 1
                    while l < r and self.nums[r] == self.nums[r - 1]:
                        r -= 1
        return result


find_three = ThreeSumZero([-25, -10, -7, -3, 2, 4, 8, 10])
print(find_three.find_triplets())


