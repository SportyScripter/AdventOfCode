from pydantic import BaseModel


class Game(BaseModel): # Simply class for data
    id: int = 0
    red: int = 0
    green: int = 0
    blue: int = 0


with open('Game.txt', 'r') as f: #Here you can change the name of the file
    lines = f.readlines()
# Here you can change the max values of cubes
max_red = 12
max_green = 13
max_blue = 14
separate = []
counter = 0
for i in lines:
    separate.append(i.split(";"))
list_of_obj = []
# in this loop we create objects for each game and find max values of cubes
for i in separate:
    counter += 1
    list_of_obj.append(Game(id=counter))
    for j in i:
        if j.__contains__("red"):
            temp_red = j[j.find("red") - 3: j.find("red")-1]
            if temp_red[0].isdigit() and temp_red[1].isdigit():
                temp_value = temp_red[0] + temp_red[1]
                if int(temp_value) >= list_of_obj[counter - 1].red :
                    list_of_obj[counter - 1].red = int(temp_value)
            elif temp_red[1].isdigit() and int(temp_red[1]) >= list_of_obj[counter - 1].red:
                list_of_obj[counter - 1].red = int(temp_red[1])
        if j.__contains__("green"):
            temp_green = j[j.find("green") - 3:j.find("green")-1]
            if temp_green[0].isdigit() and temp_green[1].isdigit():
                temp_value = temp_green[0] + temp_green[1]
                if int(temp_value) >= list_of_obj[counter - 1].green:
                    list_of_obj[counter - 1].green = int(temp_value)
            elif temp_green[1].isdigit() and int(temp_green[1]) >= list_of_obj[counter - 1].green:
                list_of_obj[counter - 1].green = int(temp_green[1])
        if j.__contains__("blue"):
            temp_blue = j[j.find("blue") - 3:j.find("blue")-1]
            if temp_blue[0].isdigit() and temp_blue[1].isdigit():
                temp_value = temp_blue[0] + temp_blue[1]
                if int(temp_value) >= list_of_obj[counter - 1].blue:
                    list_of_obj[counter - 1].blue = int(temp_value)
            elif temp_blue[1].isdigit() and int(temp_blue[1]) >= list_of_obj[counter - 1].blue:
                list_of_obj[counter - 1].blue = int(temp_blue[1])

sum_id = 0
for i in list_of_obj:
    if(i.green <= max_green and i.red <= max_red and i.blue <= max_blue): # Here we check if the game is playable
        print(f'id: {i.id} red: {i.red} green: {i.green} blue: {i.blue}')
        sum_id += i.id
print(f'First answer: {sum_id}') # Answer: 2563


sum_min_cubes = 0
for i in list_of_obj:
    all_cubes_in_one_game = i.red * i.green * i.blue
    sum_min_cubes += all_cubes_in_one_game
print(f'Second answer: {sum_min_cubes}')  # Answer: 70768

