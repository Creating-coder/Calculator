
if __name__ == "__main__":
    print("Hello! My name is N-gon")
    print("What's is your name?")
    user = input()
    print("Hi, " + user)
    print("Do you want to ask me an addition, subtraction, multiplication, or division question?")
    operation = input()
    try:
        print("What is your base?")
        base = input()
        base = int(base)

        if operation == "addition":
            print("What do you want to add on?")
            operator = int(input())
            answer = base + operator
            print(f'{base} plus {operator} is {answer}')
        else:
            if operation == "subtraction":
                print("What do you want to take away?")
                operator = int(input())
                answer = base - operator
                print(f'{base} minus {operator} is {answer}')
            else:
                if operation == "multiplication":
                    print("What do you want to multiply it by?")
                    operator = int(input())
                    answer = base * operator
                    print(f'{base} multiplied by {operator} is {answer}')
                else:
                    if operation == "division":
                        print("What do you want to divide it by?")
                        operator = int(input())
                        answer = base / operator
                        print(f'{base} divided by {operator} is {answer}')
                    else:
                        print("There is an error with your operation. Please run the program again.")
                        exit(1)
    except Exception as e:
        print("There is an error with your decision. Please run the program again", e)
        exit(1)