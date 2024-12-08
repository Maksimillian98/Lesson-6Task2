x = int(input('vvedite naturalnoe 4islo: '))
if x <= 0:
    print('vvedeno ne naturalnoe 4islo: ')
else:
    division = 0
    for i in range(1, x):
        if x % i == 0:
            division += 1
print(division)
