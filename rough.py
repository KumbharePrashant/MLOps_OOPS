from oops_proj import chatbook

user2 = chatbook()
print(user2.id) # to test static method

# encasulation
# print(user2.__dob) ## this will wont work
print(user2._chatbook__dob) ## to access hidden attribute we want to use this format.(obj._classname__attributename)
user2._chatbook__example() ## to access hidden method

## getter and setter
print(user2.get_dob())
user2.set_dob("13-12-2011")
print(user2.get_dob())

## static method
user3 = chatbook()
print(user3.id)

chatbook.set_id(20)
user4 = chatbook()
print(user4.id)
user5 = chatbook()
print(user5.id)