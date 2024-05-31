#def functions add sub mult div
#Print options to the user
#ask for values
#call the functions
#ask for values

def add(a, b):
    answer = a + b
    print(f"{str(a)} + {str(b)} = {str(answer)} \n")

def sub(a, b):
    answer = a - b
    print(f'{str(a)} - {str(b)} = {str(answer)}\n')

def mult(a, b):
    answer = a * b
    print(f'{str(a)} * {str(b)} = {str(answer)}\n')

def div(a, b):
    answer = a / b
    print(f'{str(a)} / {str(b)} = {str(answer)}\n')

while True: #use a while loop to keep the program working until the exited
    print('''
        A. Addition
        B. Subtraction
        c. Multiplication
        D. Division
        E. Exit
        ''')

    choice = input('Enter the operatin you want to calcuate: ')

    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number:'))
        add(a, b)
    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))
        sub(a, b)
    elif choice == 'c' or choice == 'C':
        print('Multiplication')
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))
        mult(a, b)
    elif choice == 'd' or choice == 'D':
        print('Division')
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))
        div(a, b)
    elif choice == 'e' or choice == 'E':
        print('Program ended')
        quit()


