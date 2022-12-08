import fileinput
import numpy as np


def main():
    data = [x.strip() for x in fileinput.input()]
    one(data)
    two(data)


def one(data):
    total = 0
    values = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for sack in data:
        first_sack, second_sack = split_string(sack)
        total += values.index(list(set(first_sack).intersection(second_sack))[0])
    print(f"Your total for puzzle one: {total}")


def two(data):
    values = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    even_chunks = len(data) / 3
    for group in np.array_split(data, even_chunks):
        total += values.index(
            list(
                set(str(group[0])).intersection(
                    set(str(group[1])).intersection(set(str(group[2])))
                )
            )[0]
        )
    print(f"Your total for puzzle two: {total}")


def split_string(a_string):
    first_half = a_string[: (int(len(a_string) / 2))]
    second_half = a_string[(int(len(a_string) / 2)) :]
    return first_half, second_half


if __name__ == "__main__":
    main()
