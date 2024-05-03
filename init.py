
def game():
    score = 0
    while True:
        print('======== Menu ========'
            '\n1. Add'
            '\n2. Divide'
            '\n3. Multiply'
            '\n4. Substract'
            '\n5. Power'
            '\n6. Module'
            '\n0. Exit')
        option = int(input('\nChose an option: '))
        if option == 0:
         break
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    answer = int(input('Enter your answer: '))
    if option == 1:
        result = add(num1, num2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
    if option == 2:
        result = division(num1, num2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
    if option == 3:
        result = multiplicacion(num1, num2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
    if option == 4:
        result = resta(num1, num2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
    if option == 5:
        result = potenciacion(num1, num2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
    if option == 6:
        result = modulo(num1, num2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
    print(f'======== Game Over ========'
          f'\nYou score is {score}'
            '\nKeep going!')
game()