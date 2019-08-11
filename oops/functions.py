#DRY - Do Not Repeat Yourself

#arguments
def sum(*args):
    sum = 0
    for number in args:
        sum = sum + number
    print(sum)

# sum(1,2,5,5,6,7,8,12,12,34,67)


def KWARGS(**kwargs):
    print(kwargs)
    print(kwargs['a'])
    print(kwargs.get('a'))


KWARGS(a=4,b=5,c=67)