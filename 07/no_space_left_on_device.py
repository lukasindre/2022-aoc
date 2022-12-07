from pprint import pprint as p


def main():
    with open("7.in") as f:
        data = [x.strip() for x in f.read().split("\n")]
    one(data)


def one(data):
    location = []
    file_structure = {}
    for line in data:
        args = line.split(" ")
        if args[0] == "$":
            if args[1] == "cd":
                # if changing to root, reset working dir to root
                if args[2] == "/":
                    location = ["/"]
                # if going up one, remove last working dir from list
                elif args[2] == "..":
                    location.pop()
                # else, add wherever you're going to the list
                else:
                    location.append(args[2])
        else:
            if not file_structure.get(location[-1], False):
                file_structure.update({location[-1]: []})
                file_structure[location[-1]].append(line)
            else:
                file_structure[location[-1]].append(line)


if __name__ == "__main__":
    main()
