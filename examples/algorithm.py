# Move all the 0's to the end of the array

def solution(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    
    return nums


array1 = [0,4,2,0,6,3,1,0,0]
array2 = [10,11,12,43,5,0,0,0,2,4,5]

print(solution(array1))
print(solution(array2))


def bubble_sort(nums):
    num_of_elements = len(nums)

    for i in range(num_of_elements -1):
        