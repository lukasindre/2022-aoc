def main():
    with open("4.in") as f:
        data = [x.strip().split(',') for x in f.readlines()]
    one(data)
    two(data)


def one(data):
    total = 0
    for pair in data:
        first = int_elf_assignments(0, pair)
        second = int_elf_assignments(1, pair)
        if set(range(first[0][0], first[0][1] + 1)
               ).issubset(set(range(second[0][0], second[0][1] + 1))):
            total += 1
        elif set(range(second[0][0], second[0][1] + 1)).issubset(set(range(first[0][0], first[0][1] + 1))):
            total += 1

    print(f"Your total for puzzle one: {total}")


def two(data):
    total = 0
    for pair in data:
        first = int_elf_assignments(0, pair)
        second = int_elf_assignments(1, pair)
        if len(set(range(first[0][0],
                         first[0][1] + 1)).intersection(set(range(second[0][0],
                                                                  second[0][1] + 1)))) > 0:
            total += 1

    print(f"Your total for puzzle two: {total}")


def int_elf_assignments(elf_number, pair):
    return [
        [int(x) for x in pair[elf_number].split('-')]
    ]


if __name__ == "__main__":
    main()
