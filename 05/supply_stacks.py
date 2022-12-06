import re


def main():
    with open("5.in") as f:
        data = [x.strip() for x in f.readlines()]
    one(data)
    two(data)


def one(data):
    pattern = re.compile("[0-9]+")
    start = {
        1: ["Z", "J", "G"],
        2: ["Q", "L", "R", "P", "W", "F", "V", "C"],
        3: ["F", "P", "M", "C", "L", "G", "R"],
        4: ["L", "F", "B", "W", "P", "H", "M"],
        5: ["G", "C", "F", "S", "V", "Q"],
        6: ["W", "H", "J", "Z", "M", "Q", "T", "L"],
        7: ["H", "F", "S", "B", "V"],
        8: ["F", "J", "Z", "S"],
        9: ["M", "C", "D", "P", "F", "H", "B", "T"],
    }
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
    start = {
        1: ["Z", "J", "G"],
        2: ["Q", "L", "R", "P", "W", "F", "V", "C"],
        3: ["F", "P", "M", "C", "L", "G", "R"],
        4: ["L", "F", "B", "W", "P", "H", "M"],
        5: ["G", "C", "F", "S", "V", "Q"],
        6: ["W", "H", "J", "Z", "M", "Q", "T", "L"],
        7: ["H", "F", "S", "B", "V"],
        8: ["F", "J", "Z", "S"],
        9: ["M", "C", "D", "P", "F", "H", "B", "T"],
    }
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


if __name__ == "__main__":
    main()
