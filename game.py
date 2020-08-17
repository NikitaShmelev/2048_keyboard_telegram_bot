import numpy as np
import random 

# game_field = np.zeros((4, 4))
game_field = [
                [2, 4, 6, 7],
                [6, 0, 0, 7],
                [6, 5, 2, 8],
                [6, 7, 8, 9]
            ]

score = 0

def get_position(game_field):
    random_row = random.randint(0, len(game_field[0]) - 1)
    random_column = random.randint(0, len(game_field) - 1)
    return tuple([random_row, random_column])


def move_left_or_rigth(left, right):
    global score
    for row in enumerate(game_field): 
        if left:
            # print('left')
            for item_index in range(len(row[1])):
                moved_to = 0
                for f in range(item_index):
                    if item_index:
                        if row[1][item_index - moved_to] != 0 and row[1][item_index - moved_to - 1] == 0:
                            game_field[row[0]][item_index - moved_to - 1], game_field[row[0]][item_index - moved_to] = game_field[row[0]][item_index - moved_to], game_field[row[0]][item_index - moved_to - 1]
                            moved_to += 1
            for column in enumerate(row[1]):
                    if column[0]:
                        if row[1][column[0] - 1] == column[1]:
                            game_field[row[0]][column[0] - 1] += column[1]
                            score += game_field[row[0]][column[0] - 1]
                            game_field[row[0]][column[0]] = 0
            
                
        else:
            # print('right')
            for item_index in range(len(row[1])):
                moved_to = 0
                for f in range(len(row[1]) - 1 - item_index):
                    if item_index != (len(row[1]) - 1):
                        if row[1][item_index + moved_to] != 0 and row[1][item_index + moved_to + 1] == 0:
                            game_field[row[0]][item_index + moved_to + 1], game_field[row[0]][item_index + moved_to] = game_field[row[0]][item_index + moved_to], game_field[row[0]][item_index + moved_to + 1]
                            moved_to += 1
            for column in enumerate(row[1]):
                    if column[0] != len(row[1]) - 1:
                        if row[1][column[0] + 1] == column[1]:
                            game_field[row[0]][column[0] + 1] += column[1]
                        
                            score += game_field[row[0]][column[0] + 1]
                            game_field[row[0]][column[0]] = 0
            
                
                            

def move_up_or_down(up, down):
    def move_items():
        for row in enumerate(game_field):
            if row[0] != len(game_field) - 1:
                for item in enumerate(row[1]):
                    if game_field[row[0]][item[0]] == game_field[row[0] + 1][item[0]]:
                        game_field[row[0] + 1][item[0]] += game_field[row[0]][item[0]]
                        global score
                        score += game_field[row[0] + 1][item[0]]
                        game_field[row[0]][item[0]] = 0
                    if game_field[row[0]][item[0]] != 0 and game_field[row[0] + 1][item[0]] == 0:
                        game_field[row[0] + 1][item[0]] = game_field[row[0]][item[0]]
                        game_field[row[0]][item[0]] = 0
    if down:
        move_items()
    else:
        game_field.reverse()
        move_items()
        game_field.reverse()

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


def check_move(move):
    if move in ['right', '6', 'left', '4']:
        for row in game_field:
            for item in enumerate(row):
                if item[1] == 0:
                    return True
                if item[0] + 1 < len(row):
                    if row[item[0]] == row[item[0] + 1]:
                        return True
        else:
            return False
    elif move in ['down' ,'5', 'up', '8']:
        for row in game_field:
            for item in enumerate(row):
                if item[1] == 0:
                    return True
                if row[0] + 1 < len(game_field):
                    if game_field[row[0]] == game_field[row[0] + 1]:
                        return True
        else:
            return False
    else:
        return False

def main():
    
    while True:
        if check_zeros(game_field):
            position = locate_position()
            game_field[position[0]][position[1]] = np.random.choice([2,4],1,p=[0.9,0.1])[0]
        # else:
        #     print('GAME OVER')
        for i in game_field:
            print(i)
        print(f'Score: {score}')
        move = input('Select move(down - 5, up - 8, right - 6, left - 4 (numpad), end):').strip()

        if check_move(move):
            if move in ['down' ,'5']:
                move_up_or_down(False, True)
            elif move in ['up', '8']:
                move_up_or_down(True, False)
            elif move in ['right', '6']:
                move_left_or_rigth(left=False, right=True)
            elif move in ['left', '4']:
                move_left_or_rigth(left=True, right=False)
            
        elif move == 'end':
            break
        else:
            print('Wrong move\n')


if __name__ == '__main__':
    main()