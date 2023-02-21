# a=[1,2,3]
# try:
#     print(a[1])
#     print((a[3]))
# except:
#     print('An error occured')


# a=10
# b=0
# try:
#     d=a/b
#     print(d)
#     print('Inside Try')
# except ZeroDivisionError:
#     print('Division by zero not allowed')
# else:
#     print('Unside Else')

# try:
#     a=int(input('Enter a:'))
#     b=int(input('Enter b:'))
#     c=a/b;
#     print(c)
# except:
#     print('cant divide by zero ')
# else:
#     print('Hi I am else block ')

# a=10
# b=0
# try:
#     d=a/b
#     print(d)
#     print('Inside try')
# except ZeroDivisionError:
#     print('Division by zero not allowed')
# else:
#     print('Inside Else')
# finally:
#     print('Inside Finally')

# class BalanceException(Exception):
#     pass
# def checkbalance():
#     money=10000
#     withdraw=int(input('enter amount u wan to withdraw '))
#     try:
#         balance=money-withdraw
#         if (balance<2000):
#             raise BalanceException('Insufficient Balance')
#         print(balance)
#     except BalanceException as be:
#         print(be)
# checkbalance()

# x='hello'
# if not type(x) is int:
#     raise TypeError('Only integers are allowed')


print('Use of assert statement')
number=int(input('Enter a number :'))
assert(number>=0),'OOPS.....Negative number'
print('Number is positive ')