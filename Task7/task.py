def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

#print(help(calculate_sum))

a = calculate_sum(2,3)
print(a)
print(type(a))

def calculate_sum(*nums):
    """Calculates the sum of any numbers passed to it."""
    s = 0
    for i in nums:
        s = s + i
    return s
    

#print(help(calculate_sum))

print(calculate_sum(1,2,3,4,5,6))
