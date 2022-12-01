import fileinput
from itertools import groupby


def main():
    max = 0
    data = [x.strip() for x in fileinput.input()]
    one(data)
    two(data)


def one(data):
    res = split_list(data=data)
    max = 0
    for list in res:
        calories = 0
        for item in list:
            if item == '':
                continue
            else:
                calories += int(item)
        if calories > max:
            max = calories
    print(f"The most calories carried by an elf is {max}")


def two(data):
    res = split_list(data=data)
    totals = []
    for list in res:
        calories = 0
        for item in list:
            if item == '':
                continue
            else:
                calories += int(item)
        totals.append(calories)
    
    final = []
    for i in range(0, 3):
        max1 = 0
        for j in range(len(totals)):
            if totals[j] > max1:
                max1 = totals[j]
        totals.remove(max1)
        final.append(max1)
    
    print(f"The top three calorie amounts add up to {sum(final)}")


def split_list(data, char=''):
    size = len(data)
    idx_list = [idx + 1 for idx, val in
            enumerate(data) if val == '']
  
    res = [data[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))]

    return res


if __name__ == "__main__":
    main()