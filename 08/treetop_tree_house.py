def main():
    with open("8.in") as f:
        data = f.read().split("\n")
    one(data)


def one(data):
    visible_trees = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            tree = Tree(
                tree_size=int(data[i][j]),
                tree_column_number=j,
                tree_row_number=i,
                data=data,
            )
            tree.check_column()
            tree.check_row()
            if tree.visibility > 0:
                visible_trees += 1
    print(f"Visible trees for puzzle one: {visible_trees}")


class Tree:
    def __init__(self, tree_size, tree_column_number, tree_row_number, data):
        self.tree_size = tree_size
        self.tree_column_number = tree_column_number
        self.data = data
        self.visibility = 0
        self.tree_row_number = tree_row_number

    def check_row(self):
        row_ints = [int(x) for x in self.data[self.tree_row_number]]
        if (
            self.tree_column_number == 0
            or self.tree_column_number == len(self.data[self.tree_row_number]) - 1
        ):
            self.visibility += 1
        else:
            left_row = row_ints[: self.tree_column_number]
            right_row = row_ints[self.tree_column_number + 1 :]
            if self.tree_size > max(left_row) or self.tree_size > max(right_row):
                self.visibility += 1

    def check_column(self):
        columns_ints = []
        for row in self.data:
            columns_ints.append(row[self.tree_column_number])
        if self.tree_row_number == 0 or self.tree_row_number == len(self.data) - 1:
            self.visibility += 1
        else:
            top_column = columns_ints[: self.tree_row_number]
            bottom_column = columns_ints[self.tree_row_number + 1 :]
            if int(self.tree_size) > int(max(top_column)) or int(self.tree_size) > int(
                max(bottom_column)
            ):
                self.visibility += 1


if __name__ == "__main__":
    main()
