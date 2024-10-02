import sys
import math


def read_circle_data(file_name):
    with open(file_name, 'r') as f:
        x, y = map(float, f.readline().split())
        r = float(f.readline())
        return x, y, r


def read_points_data(file_name):
    with open(file_name, 'r') as f:
        return [list(map(float, line.split())) for line in f]


def calculate_point_position(x, y, r, px, py):
    d = math.sqrt((px - x) ** 2 + (py - y) ** 2)
    if d == r:
        return 0
    elif d < r:
        return 1
    return 2


def main():
    if len(sys.argv) != 3:
        print('Ошибка: не указаны файлы с координатами')
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    x, y, r = read_circle_data(file1)
    points = read_points_data(file2)

    for px, py in points:
        print(calculate_point_position(x, y, r, px, py))


if __name__ == '__main__':
    main()
