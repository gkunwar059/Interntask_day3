

# 20. Write a Python function  to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

class SumTriple:
    
    def sum_triplets(self,arr):
        # sum of 3 number will be here
        result=[]
        n=len(arr)

        sum_value=32
        arr.sort()


        # for loop here 
        for i in range(n-2):
            left,right=i+1,n-1
            
            while left < right:
                current_sum= arr[i]+arr[left]+arr[right]
                if current_sum==sum_value:
                    result.append([arr[i],arr[left],arr[right]])
                    left +=1
                    # right -=1
                elif current_sum <sum_value:
                    left+=1
                else:
                    right-=1

        return result       

cls=SumTriple()
input_array=[25, 5, 3, 2, 4, 1, 1,6,8, 10]
output_triplelets=cls.sum_triplets(input_array)
print("input array:",input_array)
print("output:",output_triplelets)     