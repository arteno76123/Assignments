with open('ordered_meals.txt', 'r') as f:
    counts = {
        'r': 0,
        'g': 0,
        'b': 0,
        'o': 0,
        'total': 0
    }
    for line in f:
        counts['total'] += 1
        data = line.strip().split(' ')
        counts[data[1]] += 1

    print('Total counts')
    for key in counts:
        print(f'{key}: {counts[key]}')

    print('Less than 20')
    for key in counts:
        if counts[key] < 20:
            print(f'{key}: {counts[key]}')

    print('NOTIFICATION')
    print('COOK ALL MEALS, THE KIDS ARE HUNGRY!' if all(20 < counts[key] for key in counts) else 'NAH, I AIN\'T DOIN THAT')
