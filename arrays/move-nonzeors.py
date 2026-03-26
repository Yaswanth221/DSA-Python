# Move non zeros in an array --> pattern - Two pointers
nums = [1, 0, 2, 0, 3]


def nonzero(nums):
    pos =0
    for i in range(len(nums)):
        if nums[i] !=0:
            nums[i], nums[pos] = nums[pos],nums[i]
            pos += 1
    return nums

print(nonzero(nums))