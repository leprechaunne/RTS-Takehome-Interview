#1 	Print the number of integers in an array that are above the given input
#		and the number that are below, 
# 		e.g. for the array [1, 5, 2, 1, 10] with input 6, print “above: 1, below: 4”.

# I decided not to make this solution class oriented, but if this function became
# 		more used or complicated, it could be abstracted into a class with a function 
#		for calculation and a to-string functions

# **Due to wording of problem, nums equal to target are ignored

def calc_above_below(nums, target):
		# Takes in array of integers, nums, and return
		# the number of targets that are above and below
		# Return int above, int below
		above = below = 0

		for num in nums:
			if num > target:
				above += 1
			elif num < target:
				below += 1

		# comment to hide extra print for debugging
		print("\n", nums, ", target: ", target, sep="")
		print("above: ", above, ", below: ",below, sep="")


# Test Cases 
# ------------

#[1,5,2,1,10], target: 6 	==>	1,4
calc_above_below([1,5,2,1,10], 6)

# [0,1,2,3,4,5,6,7,8,9,10], target: 5	==>	5,5
calc_above_below([0,1,2,3,4,5,6,7,8,9,10], 5)

# [1,1,1,1,1], target: 2	==>	0,5
calc_above_below([1,1,1,1,1], 2)

# [], target: 5		==> 0,0
calc_above_below([], 5)