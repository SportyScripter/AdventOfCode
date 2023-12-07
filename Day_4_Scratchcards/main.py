import re

file_name = 'cards.txt'
with open(file_name, 'r') as f:
    games = f.readlines()
date = []
games_date = []
for i in range(len(games) - 1):
    games[i] = games[i].strip('\n')
    date.append(games[i].split(':'))
    games_date.append(date[i][1].split('|'))

result = 0
scratch_table = []
counter = 0
for a in range(len(games_date) + 1):
    scratch_table.append(1)

for j in games_date:
    count = 0
    copied = 0
    winning_numbers = re.findall(r'\d+', j[0])
    numbers_to_check = re.findall(r'\d+', j[1])
    matching_value = 0
    for k in winning_numbers:
        if k in numbers_to_check:
            matching_value += 1
            if count == 0:
                count += 1
            else:
                count *= 2
    if matching_value > 0:
        for l in range(1, matching_value + 1):
            scratch_table[counter + l] += scratch_table[counter]
    counter += 1
    result += count

print(f'Part one: {result}')
print(f'Part two: {sum(scratch_table)}')

