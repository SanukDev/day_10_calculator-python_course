from replit import clear
from art import logo

def add(number1, number2):
    return number1 + number2
def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    return number1 / number2

funct = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    print(logo)
    numb1 = float(input("What is the first number? "))
    for key in funct:
        print(key)

    operation_symbol = input("Pick an operation from the line above")
    numb2 = float(input("What is the second number? "))

    calculation_function = funct[operation_symbol]
    answer = calculation_function(numb1,numb2)

    print(f"{numb1} {operation_symbol} {numb2} = {answer}")

    end_calculation = False
    while not end_calculation:
        res = input(f"Type 'y' to continue calculate  with  {answer} else type 'n'").lower()

        if res == "y":
            operation_symbol = input("Pick an other operation:")
            calculation_function = funct[operation_symbol]
            numb3 = int(input("what is the next number? :"))
            second_answer = calculation_function(answer, numb3)
            print(f"{answer} {operation_symbol} {numb3} = {second_answer}")
            answer = second_answer
            clear()
        elif res == "n":
            end_calculation = True
            print(f"The final result is = {second_answer}")
            calculator()

calculator()