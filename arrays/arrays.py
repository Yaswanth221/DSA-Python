# To find the sum of all elements in an array
def sum_array(nums):
    total = 0

    for num in nums:
        total = total + num
    return total

# To find the greatest element in an array
def great_array(nums):
    total = nums[0]

    for num in nums:
        if num < total:
            total = num

    return total
# To find the smallest element in an array
def small_array(nums):
    total = nums[0]

    for num in nums:
        if num > total:
            total = num

    return total

def array_num(nums, target):
    count = 0

    for num in nums:
        if target == num:
            count = count + 1
    return count 

def second_largest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num
    
    second = nums[0]

    for num in nums:
        if num > second and num != largest:
            second = num
    
    return second




nums = [10, 20, 40, 30]

print(sum_array(nums))
print(great_array(nums))
print(small_array(nums))
print(array_num(nums, 10))
print(second_largest(nums))