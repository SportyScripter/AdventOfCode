import re

file_name = 'scheme.txt'
all_lines = open(file_name, mode="r").readlines()
# all_lines = []
# all_lines.append('567.....897.......839..........651.399.............236...............................343...986...........308............................765.')
# all_lines.append('.......*...............*404......*............134.....953..508=.....................*....*..........325*..........744......392..............')
# all_lines.append('123................342.........&.551+.................302...............286.....931....&.....649..$.............575................185...987')
table_with_numbers_to_add = []
table_with_numbers_to_substract = []
for one_line_index in range(len(all_lines)):
    numbers = re.findall(r'\d+', all_lines[one_line_index])
    for number in numbers:
        dot = ''
        index = all_lines[one_line_index].index(number)
        #First line
        if one_line_index == 0:
            ##First index
            if index == 0:
                for i in range(len(str(number)) + 1):
                    dot += '.'
                if all_lines[one_line_index][index + len(str(number))] == '.' and all_lines[one_line_index + 1][index:index + 1 + len(str(number))] == dot:
                    table_with_numbers_to_substract.append(int(number))
                else:
                    table_with_numbers_to_add.append(int(number))
            ## Last index
            elif index == len(all_lines[one_line_index]) - len(str(number)):  # when index is last
                for i in range(len(str(number)) + 1):
                    dot += '.'
                if all_lines[one_line_index][index - 1] == '.' and all_lines[one_line_index + 1][index - 1:index + len(str(number))] == dot:
                    table_with_numbers_to_substract.append(int(number))
                else:
                    table_with_numbers_to_add.append(int(number))
            ## Middle index
            else:
                for i in range(len(str(number)) + 2):
                    dot += '.'
                if all_lines[one_line_index][index + len(str(number))] == '.' and all_lines[one_line_index][index - 1] == '.' and all_lines[one_line_index + 1][index - 1:index + 1 + len(str(number))] == dot:
                    table_with_numbers_to_substract.append(int(number))
                else:
                    table_with_numbers_to_add.append(int(number))
        #Last line
        elif one_line_index == len(all_lines) - 1:
            #First index
            if index == 0:
                for i in range(len(str(number)) + 1):
                    dot += '.'
                if all_lines[one_line_index][index + len(str(number))] == '.' and all_lines[one_line_index - 1][index:index + 1 + len(str(number))] == dot:
                    table_with_numbers_to_substract.append(int(number))
                else:
                    table_with_numbers_to_add.append(int(number))
            #Last index
            elif index == len(all_lines[one_line_index])  - len(str(number)):
                for i in range(len(str(number)) + 1):
                    dot += '.'
                if all_lines[one_line_index][index - 1] == '.' and all_lines[one_line_index - 1][index - 1:index + len(str(number))] == dot:
                    table_with_numbers_to_substract.append(int(number))
                else:
                    table_with_numbers_to_add.append(int(number))
            #Middle index
            else:
                for i in range(len(str(number)) + 2):
                    dot += '.'
                if all_lines[one_line_index][index + len(str(number))] == '.' and all_lines[one_line_index][index - 1] == '.' and all_lines[one_line_index - 1][index - 1:index + 1 + len(str(number))] == dot:
                    table_with_numbers_to_substract.append(int(number))
                else:
                    table_with_numbers_to_add.append(int(number))
        #Middle line
        else:
            #First index
            if index == 0:
                for i in range(len(str(number))+1):
                    dot += '.'
                if all_lines[one_line_index][index + len(str(number))] == '.' and all_lines[one_line_index - 1][index:index  + 1+  len(str(number))] == dot and all_lines[one_line_index + 1][index:index + 1 + len(str(number))] == dot:
                    table_with_numbers_to_substract.append(int(number))
                else:
                    table_with_numbers_to_add.append(int(number))
            #Last index
            elif index == len(all_lines[one_line_index]) - len(str(number)):
                for i in range(len(str(number))+1):
                    dot += '.'
                if all_lines[one_line_index][index - 1] == '.' and all_lines[one_line_index - 1][index - 1:index + len(str(number))] == dot and all_lines[one_line_index + 1][index - 1:index + len(str(number))] == dot:
                    table_with_numbers_to_substract.append(int(number))
                else:
                    table_with_numbers_to_add.append(int(number))
            #Middle index
            else:
                for i in range(len(str(number)) + 2):
                    dot += '.'
                if all_lines[one_line_index][index + len(str(number))] == '.' and all_lines[one_line_index][index - 1] == '.' and all_lines[one_line_index - 1][index - 1:index+ len(str(number))+1] == dot and all_lines[one_line_index + 1][index - 1:index + len(str(number))+1] == dot:
                    table_with_numbers_to_substract.append(int(number))
                else:
                    table_with_numbers_to_add.append(int(number))

Sum_of_value = 0
for i in table_with_numbers_to_add:
    Sum_of_value += i
print(Sum_of_value)


