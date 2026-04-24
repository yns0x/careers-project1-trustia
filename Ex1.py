WIDTH = 100
blocs = {
    1: [
        {
            "name": "Clean code makes maintenance easier",
            "show": True
        }
    ],

    2: [
        {
            "name": "Testing often avoids many errors",
            "show": True
        },
        {
            "name": "This sentence must not be displayed",
            "show": False
        }
    ],

    3: [
        {
            "name": "This sentence must not be displayed",
            "show": True
        },
        {
            "name": "Good code should remain simple and clear",
            "show": False
        },
        {
            "name": "Simplicity improves code quality",
            "show": True
        },
        {
            "name": "Refactoring improves understanding",
            "show": True
        }
    ]
}

order = []

def horizontal_barrier() :
    barrier = ""
    for i in range(WIDTH):
        barrier += "-"
    barrier += "\n"
    return barrier

def add_sentence(sentence):
    row = "|"
    for i in range(WIDTH - len(sentence) - 2):
        row += " "
    return row + sentence.lower() + "|\n"

def init_order():
    if order:
        return order
    return [i for i in range(1, len(blocs) + 1)]

def main():
    sb = ""
    ord = init_order()
    for x in ord:
        sb += horizontal_barrier()
        for y in blocs[x]:
            if y["show"]:
                sb += add_sentence(y["name"])
        sb += horizontal_barrier() + "\n"
    print(sb)


if __name__ == '__main__':
    main()