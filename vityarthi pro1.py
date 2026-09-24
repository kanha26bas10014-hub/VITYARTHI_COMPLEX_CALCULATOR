# COMPLEX CALCULATOR
def add(number):
    return sum(number)

def sub(number):
    if not number:
        return 0
    result=number[0]
    for num in number[1:]:
        result-=num
    return result

def multi(number):
    if not number:
        return 0
    result=1
    for num in number:
        result*=num
    return result

def div(number):
    if not number:
        return 0
    result=number[0]
    for num in number[1:]:
        if num == 0:
            return "Error: can't divide by 0."
        result/=num
    return result


while True:
    print("------WELCOME------")
    print("To add,substract, multiply and divide--Enter: 0")
    print("For exponential-- Enter: 1")
    print("To exit-- Enter 2")

    try:
        op=int(input("enter your choice: "))
    except ValueError:
        op=-1
    if op==0:
        while True:
            print("operations: add[+] substract[-] multiply[*]  divide[/] quit[q]")

            choice=input("enter your choice: ")
        
            if choice == 'q':
                print("Thank You!")
                break
            if choice not in ['+','-','/','*','q']:
                print("invalid input")
                continue
            number_list=[]
            print("enter number one by one")
            print("type 'E' or 'e' to exit the calculator")
            while True:
                user_input=input("Enter a number(or 'E' to exit)")
                if user_input=='E'or user_input=='e':
                    break
                try:
                    num=float(user_input)
                    number_list.append(num)
                except ValueError:
                    print("Error: Invalid input")
            if not number_list:
                print("Error: no number was entered.")
                continue
        
            if choice=='+':
                print("result=",add(number_list))
            elif choice=='-':
                print("result=",sub(number_list))
            elif choice=='*':
                print("result=",multi(number_list))
            elif choice=='/':
                print("result=",div(number_list))
    elif op==1:
        try:
            num=float(input("enter the number: "))
            power=float(input("enter the power: "))
            result=num**power
            print("result:",result)
        except ValueError:
            print("Error: Please enter valid number")
    elif op==2:
        print("THANKS!")
    else:
        print("Invalid input,Please enter valid input")
