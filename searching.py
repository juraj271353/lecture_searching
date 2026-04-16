from pathlib import Path
import json
import time



def read_data(file_name, key):
    with open (file_name, "r", encoding= "utf-8") as f:
        data = json.load(f)

    if key in data:
        return data[key]
    else:
        return None


def linear_search(seq, number):
    count = 0
    positions = []

    start = time.perf_counter()

    for index,num in enumerate(seq):
        if num == number:
            positions.append(index)
            count += 1

    end = time.perf_counter()
    duration = end - start
    print(f"Měření trvalo {duration:.8f} s")

    return {
        "positions": positions,
        "count": count
    }


def binary_search(numbers, key):
    left_margin = numbers[0]
    right_margin = numbers[-1]
    middle = numbers[len(numbers) // 2]

    start = time.perf_counter()

    if key < middle:
        result = numbers[left_margin:middle]
    elif key > middle:
        result = numbers[middle:right_margin]

    end = time.perf_counter()
    duration = end - start
    print(f"Měření trvalo {duration:.8f} s")

    return result


import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]
times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]

plt.plot(sizes, times)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()


def pattern_search(sekvencia, vzor):


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)

    print(linear_search(unordered_numbers, 0))

    ordered_numbers = read_data("sequential.json", "ordered_numbers")
    print(binary_search(ordered_numbers, 14))

    seq = read_data("sequential.json", "ATA")
    print(pattern_search(seq, "ATA"))


if __name__ == "__main__":
    main()
