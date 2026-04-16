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



def main():
    print(read_data("sequential.json", "unordered_numbers"))
    print(linear_search([54, 2, 18, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5], 0))


if __name__ == "__main__":
    main()
