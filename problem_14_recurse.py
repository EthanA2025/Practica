def math_formula(n):
    if n == 1:
        return 1
    elif n < 1:
        return None
    else:
        if n%2 == 1:
            return n + math_formula(n + 1)
        else:
            return n + math_formula(n/2)

print(math_formula(0))
print(math_formula(1))
print(math_formula(10))
print(math_formula(15))
print(math_formula(100))
print(math_formula(101))

