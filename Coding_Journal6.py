import math
def cos_func(x):
    #Return cos(x)
    return math.cos(x)
def sin_func(x):
    #Return sin(x)
    return math.sin(x)
n = 1000
start = 0
end = 2
step = (end - start) / (n - 1)
x_values = []
cos_values = []
sin_values = []
for i in range(n):
    x = start + i * step
    x_values.append(x)
    sin_values.append(sin_func(x))
    cos_values.append(cos_func(x))

print("   x      sin(x)    cos(x)")
for i in range(16):
    print(f"{x_values[i]:.5f} {sin_values[i]:.5f} {cos_values[i]:.5f}")
