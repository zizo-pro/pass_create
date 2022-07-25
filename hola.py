# Python3 program to
# generate all passwords
# for given characters

# Recursive helper function,
# adds/removes characters
# until len is reached
def generate(arr, i, s, len):

	# base case
	if (i == 0): # when len has
				# been reached
	
		# print it out
		print(s)
		return
	
	# iterate through the array
	for j in range(0, len):

		# Create new string with
		# next character Call
		# generate again until
		# string has reached its len
		appended = s + arr[j]
		generate(arr, i - 1, appended, len)

	return

# function to generate
# all possible passwords
def crack(arr, len):

	# call for all required lengths
	for i in range(2 , 2 + 1):
		generate(arr, i, "", len)
	
# Driver Code
lettrs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','=','+','|','[',']','{','}',';',':','?','/','>',',','<','"',"'"]
len = len(lettrs)
crack(lettrs, len)

# This code is contributed by Smita.
