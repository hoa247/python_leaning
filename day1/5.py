number = 234
total = 0
# for i in list(str(number)):
#     total += int(i)
while number != 0 :
    total += number % 10
    number = int(number / 10)
print(total)
