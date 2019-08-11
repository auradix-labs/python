my_string = "AGARTALA"
# print(my_string)
# 1.len(str)

password = input("enter your password")
length = len(password)
if length<6:
    print("password should contain 6 charecters")
else:
    print("password is ok")