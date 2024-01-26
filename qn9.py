# 9. Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.




def binary_search(arr,target):
    low=0
    high=len(arr)


    # while loop to check low and high 
    while low <=high:
        mid=(low+high)//2
        # provide the mid value and does not print the decimal values
        guess=arr[mid]
        if guess==target:
            return mid
        if guess > target:
            high=mid - 1
        else:
            low=mid + 1
    return -1

# Test
arr=[2,3,4,10,40]
target=40
result=binary_search(arr,target)

if result !=-1:
    print("Element is present at index"),str(result)
else:
    print("Element is not present in the array")