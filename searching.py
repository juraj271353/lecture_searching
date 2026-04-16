from pathlib import Path
import json



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

    for index,num in enumerate(seq):
        if num == number:
            positions.append(index)
            count += 1

    return {
        "positions": positions,
        "count": count
    }


def binary_search(numbers, key):
    left_margin = numbers[0]
    right_margin = numbers[-1]
    middle = numbers[len(numbers) // 2]

    if key < middle:
        return numbers[left_margin:middle]
    elif key > middle:
        return numbers[middle:right_margin]





def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    print(unordered_numbers)

    print(linear_search(unordered_numbers, 0))

    ordered_numbers = read_data("sequential.json", "ordered_numbers")
    print(binary_search(ordered_numbers, 14))


if __name__ == "__main__":
    main()
