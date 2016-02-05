operators = "+-*/"

for a in operators:
    for b in operators:
        for c in operators:
            ret = 5
            if a == "+":
                ret +=5
            if a == "-":
                ret -=5
            if a == "*":
                ret *=5
            if a == "/":
                ret /=5
            if b == "+":
                ret +=5
            if b == "-":
                ret -=5
            if b == "*":
                ret *=5
            if b == "/":
                ret /=5
            if c == "+":
                ret +=5
            if c == "-":
                ret -=5
            if c == "*":
                ret *=5
            if c == "/":
                ret /=5
            print(ret, end=" ")