# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# # data = list(zip(users, ids, salary))
# data = list(enumerate(users))
# print(data)

# Python3 code to demonstrate working of
# Convert Tuples to Dictionary
# Using Dictionary Comprehension
# Note: For conversion of two tuples into a dictionary, we've to have the same length of tuples. Otherwise, we can not match all the key-value pairs

# initializing tuples
test_tup1 = ('GFG', 'is', 'best')
test_tup2 = (1, 2, 3)

# printing original tuples
print("The original key tuple is : " + str(test_tup1))
print("The original value tuple is : " + str(test_tup2))

# Using Dictionary Comprehension
# Convert Tuples to Dictionary
if len(test_tup1) == len(test_tup2):
	res = {test_tup1[i] : test_tup2[i] for i, _ in enumerate(test_tup2)}

# printing result
print("Dictionary constructed from tuples : " + str(res))
