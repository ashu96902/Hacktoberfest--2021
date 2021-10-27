# Python Program to reverse an array
# There are many ways to reverse an array

# 1. Using List Slicing to Reverse an Array in Python
# create an array 'arr'
arr1 = [1,2,3,4,5]
print("Original array = ", arr1)

# reverse using list slicing
reverse = arr1[::-1]
print("Reversed array using list slicing = ", reverse)


# 2. Using reverse() method
arr1.reverse()
print("Reversed array using reverse() method = ", arr1)


# 3. Using reversed() method
arr2 = ['a', 'b', 'c', 'd', 'e']
print("Original array = ", arr2)
reversed = list(reversed(arr2))
print("Reversed array using reversed() method = ", reversed)
