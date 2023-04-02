sentence = input()

letters_to_nums = {
    ' ': '0',
    'ZXE': '1',
    'MLG': '2',
    'WKI': '3',
    'DAQ': '4',
    'FPY': '5',
    'TBC': '6',
    'UHO': '7',
    'SJR': '8',
    'VN': '9'
}

counts = {}
for i in range(10):
    counts[f'{i}'] = 0

encrypted = ''

keys = [i for i in letters_to_nums.keys()]

for letter in sentence:
    for key in keys:
        if letter in key:
            ind = key.index(letter) + 1
            encrypted += letters_to_nums[key] * ind
            encrypted += ' '

            counts[letters_to_nums[key]] += 1


print(f'ENCRYPTED: {encrypted}')


vals = [i for i in counts.values()]
maximal_val = max(vals)

for i in counts:
    if counts[i] == maximal_val:
        print(f'MAX VALUE IN CELL: {i}')
