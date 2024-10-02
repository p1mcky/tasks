import json
import sys


def load_json(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


def merge_values(data, values):
    if isinstance(data, dict):
        for key, value in list(data.items()):
            if key == 'id':
                data['value'] = values.get(value, '')
            elif isinstance(value, (dict, list)):
                data[key] = merge_values(value, values)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            data[i] = merge_values(item, values)
    return data


def main():
    if len(sys.argv) != 4:
        print('Ошибка: не указаны файлы')
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]
    values = load_json(file1)['values']
    values_dict = {item['id']: item['value'] for item in values}
    tests = load_json(file2)['tests']
    report = merge_values(tests, values_dict)

    with open(file3, 'w') as f:
        json.dump({'tests': report}, f, indent=2)


if __name__ == '__main__':
    main()
