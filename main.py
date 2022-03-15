VERTICAL_COORDINATS = ('0', '1', '2')
EMPTY_CHAR = '_'
count = 0
field = [
    [EMPTY_CHAR for x in range(3)] for y in range(3)
]

def show_field(field):
    print(' ', '0', '1', '2')
    for y, v in enumerate(VERTICAL_COORDINATS):
        print(v, ' '.join(field[y]))

def get_user_position(field):
    real_x, real_y = 0, 0
    while True:
        coordinats = input('input coordinats:').lower().strip(' ')
        y, x = tuple(coordinats)
        if int(x) not in (0, 1, 2) or y not in VERTICAL_COORDINATS:
            print('Not valid coordinats')
            continue
        real_x, real_y = int(x), VERTICAL_COORDINATS.index(y)
        if field[real_y][real_x] == EMPTY_CHAR:
            break
        else:
            print('Position not empty')
    return real_x, real_y

def is_win(char, field):
    for y in range(3):
        if (
                (field[y][0] == field[y][1] == field[y][2] == char) or
                (field[0][y] == field[1][y] == field[2][y] == char)):
            return True
    if (
            (field[0][0] == field[1][1] == field[2][2] == char) or
            (field[0][2] == field[1][1] == field[2][0] == char)):
        return True
    return False

while True:
    show_field(field)
    count += 1
    if count % 2 != 0:
        user_char = 'x'
        player = 'Player1'
    else:
        user_char = 'o'
        player = 'Player2'
    x, y = get_user_position(field)
    field[y][x] = user_char
    if is_win(user_char, field):
        print(player, 'Win!')
        break
    elif count == 9:
        print('is draw')
        break

show_field(field)
