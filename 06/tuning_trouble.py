def main():
    with open("6.in") as f:
        data = f.read().strip()
    one(data)
    two(data)


def one(data):
    for char in range(len(data) - 4):
        if len(set(data[char : (char + 4)])) == 4:
            print(f"Your packet starter for puzzle one is: {char + 4}")
            break


def two(data):
    for char in range(len(data) - 14):
        if len(set(data[char : (char + 14)])) == 14:
            print(f"Your packet starter for puzzle two is: {char + 14}")
            break


if __name__ == "__main__":
    main()
