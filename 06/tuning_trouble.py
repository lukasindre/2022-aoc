def main():
    with open("6.in") as f:
        data = f.read().strip()
    find_starter(data, 4, "one")
    find_starter(data, 14, "two")


def find_starter(data, char_num, puzzle):
    for char in range(len(data) - char_num):
        if len(set(data[char : (char + char_num)])) == char_num:
            print(f"Your packet starter for puzzle {puzzle} is: {char + char_num}")
            break


if __name__ == "__main__":
    main()
