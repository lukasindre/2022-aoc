import re


def main():
    with open("5.in") as f:
        data = [x.strip() for x in f.readlines()]
    one(data)
    two(data)


def one(data):
    pattern = re.compile("[0-9]+")
    start = parse_start()
    for instruction in data[10:]:
        nums = pattern.findall(instruction)
        amount = int(nums[0])
        source = int(nums[1])
        target = int(nums[2])
        while amount > 0:
            label = start[source].pop()
            start[target].append(label)
            amount -= 1

    letters = ""
    for stack in start:
        letters += start[stack][-1]

    print(f"Your answer for puzzle one: {letters}")


def two(data):
    pattern = re.compile("[0-9]+")
    start = parse_start()
    for instruction in data[10:]:
        nums = pattern.findall(instruction)
        amount = int(nums[0])
        source = int(nums[1])
        target = int(nums[2])
        start[target].extend(start[source][-(amount):])
        for i in range(amount):
            start[source].pop()

    letters = ""
    for stack in start:
        letters += start[stack][-1]

    print(f"Your answer for puzzle two: {letters}")


def parse_start():
    with open("5.in") as f:
        data = f.read()
    numbers = data.split("\n\n")[0].split("\n")[-1]
    labels = data.split("\n\n")[0].split("\n")[:-1]
    num_cols = {}
    start_crates = {}
    for i in range(len(numbers)):
        if numbers[i] != " ":
            num_cols[i] = int(numbers[i])
    for i in range(1, len(num_cols) + 1):
        start_crates[i] = []
    pattern = re.compile("[A-Z]")
    for row in labels:
        for match in pattern.finditer(row):
            start_crates[num_cols[match.start()]].append(match.group())
    for k in start_crates:
        start_crates[k].reverse()
    return start_crates


if __name__ == "__main__":
    main()
