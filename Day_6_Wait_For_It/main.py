import re

file_name = 'Race.txt'
with open(file_name,'r') as f:
  date_of_race = f.readlines()

concat_time = ''
concat_distance = ''
time = re.findall(r'\d+',date_of_race[0])
distance = re.findall(r'\d+',date_of_race[1])
for i in range(len(time)):
  concat_time += time[i]
  concat_distance += distance[i]


table_with_ways = []
ways = 0
for i in range(len(distance)):
  ways = 0
  count = 0
  for j in range(int(time[i])):
    count+=1
    time_race = int(time[i]) - count
    max_distance = time_race * count
    if max_distance > int(distance[i]):
      ways += 1
  table_with_ways.append(ways)

value = 1
for k in table_with_ways:
  value *= k

count = 0
concat_ways = 0
for j in range(int(concat_time)):
  count+=1
  time_race = int(concat_time) - count
  max_distance = time_race * count
  if max_distance > int(concat_distance):
    concat_ways += 1


print(concat_ways)
print(value)


