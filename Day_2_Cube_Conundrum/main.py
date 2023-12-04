from pydantic import BaseModel


class Game(BaseModel):
    id: int = 0
    red: int = 0
    green: int = 0
    blue: int = 0


with open('Game.txt', 'r') as f:
    lines = f.readlines()

max_red = 12
max_green = 13
max_blue = 14
separate = []
counter = 0
for i in lines:
    separate.append(i.split(";"))
list_of_obj = []
test = ['Game 1: 1 red, 10 blue, 5 green', ' 11 blue, 6 green', ' 6 green', ' 1 green, 1 red, 12 blue', ' 3 blue',
        ' 3 blue, 4 green, 1 red\n']

for i in separate:
    counter += 1
    list_of_obj.append(Game(id=counter))
    for j in i:
        # j = j.replace(" ", "")
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
sum_min_cubes = 0
# for i in list_of_obj:
#     if(i.green <= max_green and i.red <= max_red and i.blue <= max_blue):
#         print(f'id: {i.id} red: {i.red} green: {i.green} blue: {i.blue}')
#         sum_id += i.id
# print(sum_id)
for i in list_of_obj:
    all_cubes_in_one_game = i.red * i.green * i.blue
    sum_min_cubes += all_cubes_in_one_game
print(sum_min_cubes)

