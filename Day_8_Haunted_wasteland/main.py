file_name = 'road.txt'
with open(file_name, 'r') as f:
    schema = f.readlines(1)
    road = f.readlines()


def find_word():
    index = 1
    count = 0
    word = 'AAA'
    while True:
        if word == 'ZZZ':
            print(count)
            break
        else:
            for j in range(len(road)):
                if road[j][0:3] == word:
                    index = j
            for i in range(len(schema[0])-1):
                if schema[0][i] == 'R':
                    word = road[index][12:15]
                    count += 1
                elif schema[0][i] == 'L':
                    count += 1
                    word = road[index][7:10]


find_word()
