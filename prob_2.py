#2  Rotate the characters in a string by a given input and have the 
#		overflow appear at the beginning
#		e.g. “MyString” rotated by 2 is “ngMyStri”.

#	Same as the first, I decided not to abstract this because of its
#		limited scope, but it could be made into a class if it was used in
#		more complicated ways in the future.

def rotate_str(input_str, rotations):
	# Takes a string, str, and rotates the characters
	# around the start
	#
	# Because strings are immutable in Python, this could be optimized
	# by changing it from a slice to two for loops, but both are constant 
	# time and slice is much more Pythonic

	# filter empty input
	if not input_str:
		print("\"\"")
		return

	# filter input thats too large
	if rotations > len(input_str):
		rotations = rotations % len(input_str)

	# calculations
	slice_point = -1*rotations
	rotated_str = input_str[slice_point:] + input_str[0:slice_point]

	# tostring
	print(rotated_str)

# Test Cases
# ------------

# MyString, 2  ==>  ngMyStri
rotate_str("MyString", 2)

# MyString, 0  ==>  MyString
rotate_str("MyString", 0)

# 0123456789, 101  ==>  9012345678
rotate_str("0123456789", 101)

# "", 5		==> ""
rotate_str("", 5)