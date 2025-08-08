
# ----------     using for loop. --------

# def Linear_Search(arr,target):

#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1


# list=[1,2,3,4,5,6,7,8]

# target=5

# sum=Linear_Search(list,target)

# if sum != -1:
#     print("fount at :",sum)
# else:
#     print("not found")


# ---------   using whileLoop   -----


def Linear_Search(arr,target):

    i=0

    while i< len(arr):
        if arr[i] == target:
            return i
        i +=1
    return -1

list=[1,2,4,5,6,3,7,8]
target=9

sum= Linear_Search(list,target)

if sum != -1:
    print("found at:",sum)
else:
    print("not found")    

