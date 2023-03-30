def read_data(file):
    with open(file, 'r') as f:
        data = [line.strip().split(',') for line in f]
    return data


