import numpy as np
import random 

# game_field = np.zeros((4, 4))
game_field = [
                [2, 0, 0, 0],
                [2, 0, 0, 2],
                [0, 2, 0, 2],
                [2, 2, 2, 2]
            ]

score = 0

def get_position(game_field):
    random_row = random.randint(0, len(game_field[0]) - 1)
    random_column = random.randint(0, len(game_field) - 1)
    return tuple([random_row, random_column])


def move_left_or_rigth(left, right):
    for row in enumerate(game_field): 
        if left:
            # print('left')
            for column in enumerate(row[1]):
                    if column[0]:
                        if row[1][column[0] - 1] == column[1]:
                            game_field[row[0]][column[0] - 1] += column[1]
                            game_field[row[0]][column[0]] = 0
            for item_index in range(len(row[1])):
                moved_to = 0
                for f in range(item_index):
                    if item_index:
                        if row[1][item_index - moved_to] != 0 and row[1][item_index - moved_to - 1] == 0:
                            game_field[row[0]][item_index - moved_to - 1], game_field[row[0]][item_index - moved_to] = game_field[row[0]][item_index - moved_to], game_field[row[0]][item_index - moved_to - 1]
                            moved_to += 1
                
        else:
            # print('right')
            for column in enumerate(row[1]):
                    if column[0] != len(row[1]) - 1:
                        if row[1][column[0] + 1] == column[1]:
                            game_field[row[0]][column[0] + 1] += column[1]
                            game_field[row[0]][column[0]] = 0
            for item_index in range(len(row[1])):
                moved_to = 0
                for f in range(len(row[1]) - 1 - item_index):
                    if item_index != (len(row[1]) - 1):
                        if row[1][item_index + moved_to] != 0 and row[1][item_index + moved_to + 1] == 0:
                            game_field[row[0]][item_index + moved_to + 1], game_field[row[0]][item_index + moved_to] = game_field[row[0]][item_index + moved_to], game_field[row[0]][item_index + moved_to + 1]
                            moved_to += 1
                
                            

def move_up_or_down(up, down):
    pass


def check_zeros(game_field):
    game_field
    for row in game_field:
        for column in row:
            if column == 0:
                return True
    return False

def locate_position():
    position = get_position(game_field)
    if game_field[position[0]][position[1]] == 0:
        return position
    else:
        return locate_position()

        
        
    # if 0 in position:
    #     random_and_locate_number()
    # return position
# position = get_position(game_field)
# game_field[position[0]][position[1]] = np.random.choice([2,4],1,p=[0.9,0.1])


# np.random.choice([2,4],1,p=[0.9,0.1])

def main():
    while True:
        for i in game_field:
            print(i)
        move = input('Select move(down - 5, up - 8, right - 6, left - 4 (numpad)):').strip()
        if move in ['down' ,'5', 'up', '8', 'right', '6', 'left', '4']:
            if move in ['down' ,'5']:
                print('down')
                move_up_or_down(False, True)
            elif move in ['up', '8']:
                print('up')
                move_up_or_down(True, False)
            elif move in ['right', '6']:
                move_left_or_rigth(left=False, right=True)
            elif move in ['left', '4']:
                move_left_or_rigth(left=True, right=False)
            if check_zeros(game_field):
                position = locate_position()
                game_field[position[0]][position[1]] = np.random.choice([2,4],1,p=[0.9,0.1])[0]
            else:
                print('GAME OVER')
                break
        else:
            print('Wrong move\n')
            # for i in game_field:
            #     print(i)
            break


if __name__ == '__main__':
    main()