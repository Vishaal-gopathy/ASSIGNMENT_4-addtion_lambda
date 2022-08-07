def square_num(n):
  return n **2
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square of the elements in the list : ")
print(list(result))