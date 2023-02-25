import json

INPUT_FILE = "input.csv"

# TODO реализовать конвертер из csv в json
def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as f:
        list = []
        for column, value in enumerate(f):
            i = value.strip(new_line).split(delimiter)
            if column == 0:
                first_line = i
                continue

            list.append({})

            for a, b in enumerate(first_line):
                list[-1][first_line[a]] = i[a]
    return list

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
