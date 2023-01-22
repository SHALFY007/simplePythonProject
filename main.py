# Is Number even?

number = int(input('Input number: '))

def is_even(num):
    if num % 2 == 0:
        print('Number is even!')
    else:
        print('Number is not even!')

is_even(number)