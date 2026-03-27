
# 1
x = lambda a, b: 0 if a == b else 1

res = x(4,5)
print(res)

# 2
x = lambda a:a if a % 3 == 0 else a

res = x(5)
print(res)

# 3
x = lambda a: "ok" if a % 2 == 0 and a % 3 == 0 else "no"

res = x(4)
print(res)

# 4
x = lambda a: "zero" if a == 0 else "not zero"

res = x(0)
print(res)

# 5
x = lambda a: "range" if a in range(1, 11) else "out"

res = x(6)
print(res)

# 6

x = lambda a, b: True if a + b > 50 else a

res = x(9,56)
print(res)

# 7
x = lambda a: "good" if a % 2 == 0 and a > 0 else "bad"

res = x(4)
print(res)

# 8
x = lambda a: a*a if a % 4 else a ** 3

res = x(8)
print(res)

# 9
x = lambda a: a if a < 10 == a else a

res = x(4)
print(res)
