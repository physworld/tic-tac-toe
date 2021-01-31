# Сохраняем данные в матрицу
matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
is_possible = True
is_winner = False
# Счетчик для цикла
counter = 1


# Печатаем поле
def print_field(numbers):
    print('---------')
    print('|', numbers[0][0], numbers[0][1], numbers[0][2], '|')
    print('|', numbers[1][0], numbers[1][1], numbers[1][2], '|')
    print('|', numbers[2][0], numbers[2][1], numbers[2][2], '|')
    print('---------')


# Проверяем является ли координата числом
def is_coordinates_valid(data):
    while not data[0].isnumeric() or not data[1].isnumeric():
        print('You should enter numbers!')
        data = input('Enter the coordinates: ')  # Если нет, просим повторного ввода
        data = data.split(' ')

    # Проверяем является ли координата числом от 1 до 3
    while ('123'.find(data[0]) == -1) or ('123'.find(data[1]) == -1):
        print('Coordinates should be from 1 to 3!')
        data = input('Enter the coordinates: ')  # Если нет, просим повторного ввода
        data = data.split(' ')

    # Проверяем занято ли выбранное поле
    while matrix[int(data[0]) - 1][int(data[1]) - 1] != '_':
        print('This cell is occupied! Choose another one!')
        data = input('Enter the coordinates: ')  # Если нет, просим повторного ввода
        data = data.split(' ')
    return data


# Печатаем поле
print_field(matrix)

while not is_winner:
    # Берем координаты поля у игрока
    coordinates = input('Enter the coordinates: ')
    coordinates = coordinates.split(' ')
    # Выбираем какой символ писать в зависимости от порядка хода
    symbol = ''
    if counter % 2 == 1:
        symbol = symbol.replace(symbol, 'X')
    else:
        symbol = symbol.replace(symbol, 'O')
    # Проверяем координату на правильность
    coordinates = is_coordinates_valid(coordinates)
    # Если все условия выполнены - ставим на выбранное поле X и перерисовываем поле
    matrix[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = matrix[int(coordinates[0]) - 1][
        int(coordinates[1]) - 1].replace('_', symbol)
    # Меняем очередность хода
    counter += 1
    # Печатаем поле
    print_field(matrix)

    # Просматриваем все горизонтали вертикали и диагонали и ищем победителя
    if is_possible:
        if (matrix[0][0] == matrix[1][1] == matrix[2][2] == 'X') or (matrix[0][2] == matrix[1][1] == matrix[2][0] == 'X'):
            print('X wins')
            is_winner = True
        elif (matrix[0][0] == matrix[1][1] == matrix[2][2] == 'O') or (matrix[0][2] == matrix[1][1] == matrix[2][0] == 'O'):
            print('O wins')
            is_winner = True
        else:
            for x in range(3):
                if matrix[x][0] == matrix[x][1] == matrix[x][2] == 'X':
                    print('X wins')
                    is_winner = True
                    break
                elif matrix[x][0] == matrix[x][1] == matrix[x][2] == 'O':
                    print('O wins')
                    is_winner = True
                    break
                elif matrix[0][x] == matrix[1][x] == matrix[2][x] == 'X':
                    print('X wins')
                    is_winner = True
                    break
                elif matrix[0][x] == matrix[1][x] == matrix[2][x] == 'O':
                    print('O wins')
                    is_winner = True
                    break
    # Если ситуация возможна но нет победителя и есть пустые клетки - игра не закончена
    if not is_winner and is_possible:
        if '_' in matrix[0] or '_' in matrix[1] or '_' in matrix[2]:
            continue
        else:
            print('Draw')  # Если же пустых клеток нет - ничья
            break



