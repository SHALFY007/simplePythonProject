# Is Number even?

array = [3,6,10,15,18,24,29,35]
correct = []
max = 0
def is_even(nums):
    global max
    for i in nums:
        if i % 6 == 0:
            correct.append(i)
            if i > max:
                max = i
    return max

is_even(array)
print(correct)
print(max)