def read_info(file):
    with open(file, 'r') as f:
        data = [line.strip().split(',') for line in f]
    return data


def sort_by_area(data):
    sorted_data = sorted(data, key=lambda x: int(x[1]))
    return sorted_data

