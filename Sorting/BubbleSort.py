

def Bubble_Sort(nums):

    n= len(nums)

    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

nums=[1,2,9,2,8,6,14,]

print(Bubble_Sort(nums))