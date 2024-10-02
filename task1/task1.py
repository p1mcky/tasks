import sys


def circular_array_path(n, m):
    array = list(range(1, n + 1))
    path = []
    current_position = 0

    while True:
        path.append(str(array[current_position]))
        current_position = (current_position + m - 1) % n
        if current_position == 0:
            break
    return ''.join(path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Ошибка: не указаны параметры n и m')
        sys.exit(1)
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    print(circular_array_path(n, m))
