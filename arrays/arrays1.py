#reverse the array
def reverse_array(nums):
    result = []

    for i in range(len(nums)-1, -1, -1):
        result.append(nums[i])
    
    return result

nums = [10,20,30,40]


print(reverse_array(nums))


# Check if array is sorted

def is_sorted(nums):

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

nums = [10,20,30,40]

# Remove duplicates

def remove_duplicates(numss):
    result = []

    for num in numss:
        if num not in result:
            result.append(num)
    return result

numss = [10,20,20,30,40,50,50,60]

print(remove_duplicates(numss))