# DRY : DO  NOT REPEAT YOURSELF
# 1 no args no return
def sum_no_args_no_return():
    x = 1
    y = 2
    sum = x + y
    print(sum)


# 2. no args with return
def sum_no_args_with_return():
    x = 1
    y = 2
    sum = x + y
    return sum


# 3. with args no return
def sum_with_args_no_return(a, b):
    sum = a + b
    print(sum)


# 4. with args with return
def sum_with_args_with_return(a, b):
    sum = a + b
    return sum

# take user input
a =int(input("enter value of a"))
b =int(input("enter value of b"))
sum_with_args_no_return(a,b)