import classes as c

in_str = input("Enter website url: ")
print("You entered: ", in_str)
#
# print(c.simpe_get(in_str))

c.find_tag(c.simpe_get(in_str))
print('end')
