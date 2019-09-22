# positional argument
def sum_with_positional_args(a, b):
    sum = a + b
    print(sum)


# keyword (named) argument
def sum_with_named_args(a=1, b=2):
    print("a= ", a)
    print("b=", b)
    sum = a + b
    print(sum)


# dynamic arg
def sum(*args, **kwargs):
    for arg in args:
        print(arg)
    print(kwargs)
    for key in kwargs:
        print(key, '--->', kwargs.get(key))


sum(10, 10, 20, a= 20,b=20)

