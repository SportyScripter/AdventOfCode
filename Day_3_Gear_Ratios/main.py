import re
#method to search middle line from file
def check_sign_in_middle_line_inside_line(number,index,one_line_index):
    bool = False
    if (all_lines[one_line_index][index - 1] == '.' or all_lines[one_line_index][index - 1].isdigit()) and (all_lines[one_line_index][index + len(str(number))] == '.' or all_lines[one_line_index][index + len(str(number))].isdigit()):
        bool = False
    else:
        bool = True
        return bool
    for i in range(len(str(number))+2):
        if (all_lines[one_line_index-1][index -1 + i] == '.' or all_lines[one_line_index-1][index -1 + i].isdigit()) and (all_lines[one_line_index+1][index -1 + i] == '.' or all_lines[one_line_index+1][index -1 + i].isdigit()):
            bool = False
        else:
            return True
    return bool


def check_sign_in_middle_line_in_last_index(number,index,one_line_index):
  if all_lines[one_line_index][index-1] =='.' or all_lines[one_line_index][index-1].isdigit():
    bool = False
  else:
    bool = True
    return bool
  for i in range(len(str(number))+1):
        if (all_lines[one_line_index-1][index -1 + i] == '.' or all_lines[one_line_index-1][index -1 + i].isdigit()) and (all_lines[one_line_index+1][index -1 + i] == '.' or all_lines[one_line_index+1][index -1 + i].isdigit()):
          bool = False
        else:
          return True
  return bool



def check_sign_in_middle_line_in_first_index(number,index,one_line_index):
  if all_lines[one_line_index][index + len(str(number))] =='.' or all_lines[one_line_index][index+ len(str(number))].isdigit():
    bool = False
  else:
    bool = True
    return bool
  for i in range(len(str(number))+1):
        if (all_lines[one_line_index-1][index + i] == '.' or all_lines[one_line_index-1][index + i].isdigit())and (all_lines[one_line_index+1][index + i] == '.' or all_lines[one_line_index+1][index + i].isdigit()):
          bool = False
        else:
          return True
  return bool


# method to search first line from file:
def check_sign_in_first_line_inside_line(number,index,one_line_index):
    bool = False
    if (all_lines[one_line_index][index - 1] == '.' or all_lines[one_line_index][index - 1].isdigit()) and (all_lines[one_line_index][index + len(str(number))] == '.' or all_lines[one_line_index][index + len(str(number))].isdigit()):
        bool = False
    else:
        bool = True
        return bool
    for i in range(len(str(number))+2):
        if (all_lines[one_line_index+1][index -1 + i] == '.' or all_lines[one_line_index+1][index -1 + i].isdigit()):
            bool = False
        else:
            return True
    return bool

def check_sign_in_firs_line_in_last_index(number,index,one_line_index):
  if all_lines[one_line_index][index-1] =='.' or all_lines[one_line_index][index-1].isdigit():
    bool = False
  else:
    bool = True
    return bool
  for i in range(len(str(number))+1):
        if (all_lines[one_line_index+1][index -1 + i] == '.' or all_lines[one_line_index+1][index -1 + i].isdigit()):
          bool = False
        else:
          return True
  return bool

def check_sign_in_first_line_in_first_index(number,index,one_line_index):
  if all_lines[one_line_index][index + len(str(number))] =='.' or all_lines[one_line_index][index+ len(str(number))].isdigit():
    bool = False
  else:
    bool = True
    return bool
  for i in range(len(str(number))+1):
        if (all_lines[one_line_index+1][index + i] == '.' or all_lines[one_line_index+1][index + i].isdigit()):
          bool = False
        else:
          return True
  return bool


# method to search Last line from file:
def check_sign_in_last_line_inside_line(number,index,one_line_index):
    bool = False
    if (all_lines[one_line_index][index - 1] == '.' or all_lines[one_line_index][index - 1].isdigit()) and (all_lines[one_line_index][index + len(str(number))] == '.' or all_lines[one_line_index][index + len(str(number))].isdigit()):
        bool = False
    else:
        bool = True
        return bool
    for i in range(len(str(number))+2):
        if (all_lines[one_line_index-1][index -1 + i] == '.' or all_lines[one_line_index-1][index -1 + i].isdigit()):
            bool = False
        else:
            return True
    return bool

def check_sign_in_last_line_in_last_index(number,index,one_line_index):
  if all_lines[one_line_index][index-1] =='.' or all_lines[one_line_index][index-1].isdigit():
    bool = False
  else:
    bool = True
    return bool
  for i in range(len(str(number))+1):
        if (all_lines[one_line_index-1][index -1 + i] == '.' or all_lines[one_line_index-1][index -1 + i].isdigit()):
          bool = False
        else:
          return True
  return bool

def check_sign_in_last_line_in_first_index(number,index,one_line_index):
  if all_lines[one_line_index][index + len(str(number))] =='.' or all_lines[one_line_index][index+ len(str(number))].isdigit():
    bool = False
  else:
    bool = True
    return bool
  for i in range(len(str(number))+1):
        if (all_lines[one_line_index-1][index + i] == '.' or all_lines[one_line_index-1][index + i].isdigit()):
          bool = False
        else:
          return True
  return bool
def find_index_of_number(temp_string,number,j):
  number = str(number)
  for i in range(j,len(temp_string)):
    if temp_string[i:i+len(number)] == number:
      if i == 0 and temp_string[i+len(number)].isdigit() == False:
        return i
      elif i == len(temp_string) - len(number):
        if temp_string[i-1].isdigit() == False:
          return i
      elif temp_string[i-1].isdigit() == False and temp_string[i+len(number)].isdigit() == False:
        return i
      else:
        i+=1
file_name = 'scheme.txt'
with open('scheme.txt', 'r') as f: #Here you can change the name of the file
    all_lines = f.readlines()
table_with_numbers_to_add = []
table_with_numbers_to_substract = []
for one_line_index in range(len(all_lines)):
    all_lines[one_line_index] = all_lines[one_line_index].strip().strip('\n')
    numbers = re.findall(r'\d+', all_lines[one_line_index])
    j=0
    for number in numbers:
        dot = ''
        index = find_index_of_number(all_lines[one_line_index],number,j)
        j = index
        #First line
        if one_line_index == 0:
            ##First index
            if index == 0:
              if check_sign_in_first_line_in_first_index(number,index,one_line_index):
                table_with_numbers_to_add.append(number)
              else:
                table_with_numbers_to_substract.append(number)

            ## Last index
            elif index == len(all_lines[one_line_index]) - len(str(number)):  # when index is last
              if check_sign_in_firs_line_in_last_index(number,index,one_line_index):
                table_with_numbers_to_add.append(number)
              else:
                table_with_numbers_to_substract.append(number)

            ## Middle index
            else:
              if check_sign_in_first_line_inside_line(number,index,one_line_index):
                table_with_numbers_to_add.append(number)
              else:
                table_with_numbers_to_substract.append(number)

        #Last line
        elif one_line_index == len(all_lines) - 1:
            #First index
            if index == 0:
              if check_sign_in_last_line_in_first_index(number,index,one_line_index):
                table_with_numbers_to_add.append(number)
              else:
                table_with_numbers_to_substract.append(number)

            #Last index
            elif index == len(all_lines[one_line_index])  - len(str(number)):
              if check_sign_in_last_line_in_last_index(number,index,one_line_index):
                table_with_numbers_to_add.append(number)
              else:
                table_with_numbers_to_substract.append(number)

            #Middle index
            else:
              if check_sign_in_last_line_inside_line(number,index,one_line_index):
                table_with_numbers_to_add.append(number)
              else:
                table_with_numbers_to_substract.append(number)

        #Middle line
        else:
            #First index
            if index == 0:
              if check_sign_in_middle_line_in_first_index(number,index,one_line_index):
                table_with_numbers_to_add.append(number)
              else:
                table_with_numbers_to_substract.append(number)

            #Last index
            elif index == len(all_lines[one_line_index]) - len(number): #tu ma trafiac 3
              if check_sign_in_middle_line_in_last_index(number,index,one_line_index):
                table_with_numbers_to_add.append(number)
              else:
                table_with_numbers_to_substract.append(number)

            #Middle index
            else:
              if check_sign_in_middle_line_inside_line(number,index,one_line_index):
                table_with_numbers_to_add.append(number)
              else:
                table_with_numbers_to_substract.append(number)


Sum_of_value = 0
for i in table_with_numbers_to_add:
    Sum_of_value += int(i)
print(Sum_of_value)
#answer = 556057
#answser to part two = 82824352



