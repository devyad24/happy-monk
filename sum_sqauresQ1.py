import multiprocessing

def calculate_sum_of_squares(chunk):
    return sum(x ** 2 for x in chunk)

def split_into_chunks(input, chunk_size):
    for i in range(0, len(input), chunk_size):
        yield input[i:i + chunk_size]


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num_processes = 4
    chunk_size = len(numbers)

    chunks = list(split_into_chunks(numbers, chunk_size))

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(calculate_sum_of_squares, chunks)

    total_sum_of_squares = sum(results)

    print("Sum of sqaures", total_sum_of_squares)

if __name__ == "__main__":
    main()