import time, multiprocessing

all_data = []
def  read_info(name):
    with open(name, "r") as file:
        for line in file:
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = time.time()
    for file_name in filenames:
        read_info(file_name)

    end = time.time() - start
    print(f'{end}  - Линейный')
# ***
    all_data = []
    start = time.time()
    pool = multiprocessing.Pool()
    pool.map(read_info, filenames)
    end = time.time() - start
    print(f'{end}  - Многопроцессный')
