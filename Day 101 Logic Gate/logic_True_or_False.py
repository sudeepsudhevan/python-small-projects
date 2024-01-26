operators = {
    "AND": [lambda x, y: x and y, "∧"],
    "OR": [lambda x, y: x or y, "∨"],
    "XOR": [lambda x, y: x ^ y, "⊕ "],
    "NOT": [lambda x: not x, "¬"],
    "NAND": [lambda x, y: not (x and y), "⊼"],
    "NOR": [lambda x, y: not (x or y), "⊽"],
    "XNOR": [lambda x, y: not (x ^ y), "⊻"],
}


change_value = {1: True, 0: False}

try_again = True

# print(operators["NOT"][0](True))

while try_again:
    oper = input("Enter the operator: ").upper()
    # Generate the truth table
    if oper in operators:
        for i in range(2):
            if oper == "NOT":
                print(
                    f"{operators[oper][1]} {change_value[i]} = {operators[oper][0](i)}"
                )
            else:
                for j in range(2):
                    print(
                        f"{change_value[i]} {operators[oper][1]} {change_value[j]} = {operators[oper][0](change_value[i], change_value[j])}"
                    )

    do_again = input(
        "Do you want check another gate if yes type y if not type anything: "
    ).lower()

    if do_again == "y":
        try_again = True
    else:
        try_again = False
