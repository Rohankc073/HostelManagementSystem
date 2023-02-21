# #Print first 4 integers
# a=int(input('Enter Number: '))
# x=0
# y=1
# for i in range(a):
#     print(x)
#     temp=x
#     x=y
#     y=temp+y

#Recursion
def fact(num):
    """This function call itself to find the factorial of a number"""
    if num==1:
        return 1
    else:
        return (num*fact(num-1))
num=5
print('Factorial of ',num,'is:',fact(num))

# import sys
# print(sys.getrecursionlimit())


# def add():
#     print('Hello')
#     add()
# add()

# def a(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return a(n-1)+a(n-2)
# n=int(input('Any '))
# for i in range(1,n+1):
#     print(a(i))

#Homework
# #Reverse a string using recursion
# def reverse_string(s):
#     if len(s)==0:
#         return s
#     else:
#         return (s[1:])+s[0]
# print(reverse_string('anjali'))
















