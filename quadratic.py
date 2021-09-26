import cmath

a = int(input('Enter the value: '))
b = int(input('Enter the value: '))
c = int(input('Enter the value: '))

d = (b**2)-(4*a*c)

sol1 = (-b-cmath.sqrt(b))
sol2 = (-b-cmath.sqrt(b))

print(sol1)
print(sol2)

print('The solution are {0} and {1}'.format(sol1,sol2))