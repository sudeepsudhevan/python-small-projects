operators = {
    "AND": [lambda x, y: x and y, "∧"],
    "OR": [lambda x, y: x or y, "∨"],
    "XOR": [lambda x, y: x ^ y, "⊕ "],
    "NOT": [lambda x: not x, "¬"],
    "NAND": [lambda x, y: not (x and y), "⊼"],
    "NOR": [lambda x, y: not (x or y), "⊽"],
    "XNOR": [lambda x, y: not (x ^ y), "⊻"],
}

try_again = True

while try_again:
    oper = input("Enter the operator: ").upper()
    # Generate the truth table
    if oper in operators:
        for i in range(2):
            if oper == "NOT":
                if operators[oper][0](i) == True:
                    result = "1"
                else:
                    result = "0"
                print(f"{operators[oper][1]} {i} = {result}")
            else:
                for j in range(2):
                    if operators[oper][0](i, j) == True:
                        result = "1"
                    else:
                        result = "0"
                    print(f"{i} {operators[oper][1]} {j} = {result}")

    do_again = input(
        "Do you want check another gate if yes type y if not type anything: "
    ).lower()

    if do_again == "y":
        try_again = True
    else:
        try_again = False
