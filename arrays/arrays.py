
def sum_array(nums):
    total = 0

    for num in nums:
        total = total + num
    return total

def great_array(nums):
    total = nums[0]

    for num in nums:
        if num < total:
            total = num

    return total

def small_array(nums):
    total = nums[0]

    for num in nums:
        if num > total:
            total = num

    return total

nums = [10, 20, 40, 30]

print(sum_array(nums))
print(great_array(nums))
print(small_array(nums))