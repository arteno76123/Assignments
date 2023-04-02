table = 'ZXEMLGWKIDAQFPYTBCUHOSJRVN'
numbers = '0123456789'
coding = {}
coding[' '] = '0'
coded = ''
counting = []
auto = input('automatic test? y/n\n')

if auto == 'y':
    text = 'CREATING WITH PYTHON'
else:
    text = input('Text to be encoded\nUppercase only\n')

n = 0
c = 1
for i in range(len(table)):
    coding[table[i]] = numbers[n+1]*c
    if c < 3:
        c += 1
    else:
        c = 1
        n += 1

for letter in text:
    coded += f'{coding[letter]} '

for number in numbers:
    counting.append(coded.count(number))

maxed = []
for i in range(len(counting)):
    if counting[i] == max(counting):
        maxed.append(i)

print(coded)
print(maxed)
