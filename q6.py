import csv

def print_table(filewa):  
    with open(filewa, 'r') as file:
        rows = [row for row in csv.reader(file) if row]

    if not rows: return

    widths = [max(map(len, col)) for col in zip(*rows)]
    border = "+-" + "-+-".join("-" * w for w in widths) + "-+"

    print(border)
    print("| " + " | ".join(f"\033[95m{word:<{w}}\033[0m" for word, w in zip(rows[0], widths)) + " |")
    print(border)
    for row in rows[1:]:
        print("| " + " | ".join(f"{word:<{w}}" for word, w in zip(row, widths)) + " |")
    print(border)

print_table('file6.csv')
