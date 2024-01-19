number = 0
numbers = int(input())
for num in range(2,numbers):
    if numbers % num == 0:
        number = number +1
print(number)
if number == 0:
    print('p')
else:
    print('np')



