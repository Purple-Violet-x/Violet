import random
pravila = {'к','н','н','б','б','к'}
print("Играем!")
player = input("Выбирай предмет (к, н, б): ").lover()
if player in pravila:
    komp = random.choice(['к','н','б'])
    print(f"Мой выбор {komp}")
    if player == komp:
        print("Ничья")
    elif pravila[player] == komp:
        print("Ты победил!")
    else:
        print("Компьютер победил")
else:
    print("Жульничаешь!")