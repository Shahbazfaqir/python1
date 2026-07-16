def greeting():
    print("welcome to the python world")
greeting()

## now add two number

def add_numbers(a,b):
    sum_result = a+b
    diff_result = a-b
    prod_result = a*b
    print("the sum of two numbers is:", sum_result)
    print("the difference of two numbers is:", diff_result)
    print("the product of two numbers is:", prod_result)


add_numbers(5, 10)

## Function with return statement

def add2num(a,b):
    return a+b

result = add2num(10, 20)
print("The sum of two numbers is:", result)

## pass statement in function

def my_function():
    pass

def my_function2():
    pass
