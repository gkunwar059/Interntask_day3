

# # 20. Write a Python function  to find the three elements that sum to zero
# # from a list of n real numbers.
# # Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# # Output : [[-10, 2, 8], [-7, -3, 10]]



# def find_three_elements(arr):
#     result = []
#     n = len(arr)

#     sum_final=34
#     # Sort the array
#     arr.sort()

#     for i in range(n - 2):
#         left, right = i + 1, n - 1

#         while left < right:
#             current_sum = arr[i] + arr[left] + arr[right]

#             if current_sum == sum_final:
#                 result.append([arr[i], arr[left], arr[right]])
#                 left += 1
#                 right -= 1
#             elif current_sum < sum_final:
#                 left += 1
#             else:
#                 right -= 1

#     return result

# # Example usage
# input_array = [25, 5, 3, 2, 4,1, 8, 10]
# output = find_three_elements(input_array)
# print("Input array:", input_array)
# print("Output:", output)
