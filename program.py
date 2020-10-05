# my_list = []

# MY INITIAL ATTEMPT
# my_list[0] = int(input("Enter a number: "))
# my_list[1] = int(input("Enter a number: "))
# my_list[2] = int(input("Enter a number: "))
# my_list[3] = int(input("Enter a number: "))

###############################################################################

# MY SECOND ATTEMPT
my_list = []

# Program prompts user to enter a number
user_input = int(input("Enter a number of elements: "))

# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
# Loops iterates until it reaches range
for i in range(0, user_input):
    num = int(input())

    my_list.append(num) # adding the element

# Outputs result
print("User input list: ", my_list)