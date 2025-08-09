
def Binary_Search(list,target):
    l=0
    u=len(list)-1

    while l<= u:
        mid= (l+u) // 2

        if list[mid] == target:
            return mid
        else:
            if list[mid] < target:
                l=mid +1
            else:
               u=mid -1
    return -1
    


list=[1,2,3,4,5,6,7,8,9]
target=4

sum = Binary_Search(list,target)

if sum!= -1:
    print("found at:",sum)
else:
    print("not found")