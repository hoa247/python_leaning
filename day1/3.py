n = 20
strEvens = ''
strOdds = ''
for i in range(n):
    if i % 2 == 0:
        strEvens += str(i) + ', '
    else:
        strOdds += str(i) + ', '

print('Even numbers: ' + strEvens.strip(', '))
print('Odd numbers: ' + strOdds.strip(', '))
