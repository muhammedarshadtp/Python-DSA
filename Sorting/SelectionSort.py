
def selection(nums):

    n= len(nums)

    for i in range(n-1):

        min_intex=i
        for j in range(i+1,n):
            if nums[j] < nums[min_intex]:
                min_intex=j

        nums[i],nums[min_intex]=nums[min_intex],nums[i]    

    return nums     



nums=[7,9,3,1,4,5,1]

result=selection(nums)
print(result)