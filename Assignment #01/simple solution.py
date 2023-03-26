with open('ordered_meals.txt') as source:
  file = source.readlines()
  length = len(file)
  print(f'{length} students ordered a meal')
  
  green_count = 0
  red_count = 0
  blue_count = 0
  orange_count = 0

  for line in file:
    if 'g'in line:
      green_count += 1
    elif 'r'in line:
      red_count += 1
    elif 'b'in line:
      blue_count += 1
    elif 'o'in line:
      orange_count += 1

  print(f'{green_count} green ordered meals')
  print(f'{red_count} red ordered meals')
  print(f'{blue_count} blue ordered meals')
  print(f'{orange_count} orange ordered meals')

  if green_count < 20:
    print('green meal is ordered less than 20 times')
  elif red_count < 20:
    print('red meal is ordered less than 20 times')
  elif blue_count < 20:
    print('blue meal is ordered less than 20 times')
  elif orange_count < 20:
    print('orange meal is ordered less than 20 times')
  else:
    print('enough meals were ordered')