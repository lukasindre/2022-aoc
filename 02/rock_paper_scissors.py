import fileinput


def main():
    one()
    two()


def one():
    total_score = 0
    data = [x.strip().split(" ") for x in fileinput.input()]
    for round in data:
        opponent = round[0]
        you = round[1]
        score = scores()[you]
        if (
            (opponent == "A" and you == "Y")
            or (opponent == "B" and you == "Z")
            or (opponent == "C" and you == "X")
        ):
            score += 6
        elif (
            (opponent == "A" and you == "X")
            or (opponent == "B" and you == "Y")
            or (opponent == "C" and you == "Z")
        ):
            score += 3

        total_score += score

    print(f"Your total score for puzzle one: {total_score}")


def two():
    total_score = 0
    data = [x.strip().split(" ") for x in fileinput.input()]
    for round in data:
        opponent = round[0]
        outcome = round[1]
        score = 0
        if outcome == "X":
            if opponent == "A":
                score += 3
            elif opponent == "B":
                score += 1
            elif opponent == "C":
                score += 2
        elif outcome == "Y":
            score += 3
            if opponent == "A":
                score += 1
            elif opponent == "B":
                score += 2
            elif opponent == "C":
                score += 3
        elif outcome == "Z":
            score += 6
            if opponent == "A":
                score += 2
            elif opponent == "B":
                score += 3
            elif opponent == "C":
                score += 1
        total_score += score

    print(f"Your total score for puzzle two: {total_score}")


def scores():
    return {"X": 1, "Y": 2, "Z": 3}


if __name__ == "__main__":
    main()
