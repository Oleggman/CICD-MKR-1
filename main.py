def read_info(file):
    with open(file, 'r') as f:
        data = [line.strip().split(',') for line in f]
    return data


def get_sort(data, el):
    return sorted(data, key=lambda x: int(x[2]))


def sort_by_area(data):
    sorted_data = get_sort(data, 1)
    return sorted_data


def sort_by_population(data):
    sorted_data = get_sort(data, 2)
    return sorted_data


def print_info(data):
    for row in data:
        print(row)


def main():
    data = read_info('file.txt')

    sorted_by_area = sort_by_area(data)
    print('Sort by area:')
    print_info(sorted_by_area)

    sorted_by_population = sort_by_population(data)
    print('Sort by population:')
    print_info(sorted_by_population)


if __name__ == "__main__":
    main()
