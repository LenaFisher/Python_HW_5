# # Создайте программу для игры в ""Крестики-нолики"".

MATRIX_SIZE=3
X_SYMBOL = "X"
O_SYMBOL = "O"
EMPTY = " "
matrix = []

def Create_matrix():
    for i in range(MATRIX_SIZE):
        a =[]  
        for j in range(MATRIX_SIZE): 
            a.append(EMPTY)  
        matrix.append(a)
    
def Print_matrix():
    for i in range(MATRIX_SIZE):  
        for j in range(MATRIX_SIZE):  
            print(matrix[i][j], end = " ")  
        print()

def Get_Winner():
    if (matrix[0][0]==X_SYMBOL and matrix[0][1]==X_SYMBOL and matrix[0][2]==X_SYMBOL or matrix[0][0]==X_SYMBOL and matrix[1][0]==X_SYMBOL and matrix[2][0]==X_SYMBOL or matrix[1][0]==X_SYMBOL and matrix[1][1]==X_SYMBOL and matrix[1][2]==X_SYMBOL or matrix[2][0]==X_SYMBOL and matrix[2][1]==X_SYMBOL and matrix[2][2]==X_SYMBOL or matrix[0][1]==X_SYMBOL and matrix[1][1]==X_SYMBOL and matrix[2][1]==X_SYMBOL or matrix[0][2]==X_SYMBOL and matrix[1][2]==X_SYMBOL and matrix[2][2]==X_SYMBOL or matrix[0][0]==X_SYMBOL and matrix[1][1]==X_SYMBOL and matrix[2][2]==X_SYMBOL or matrix[0][2]==X_SYMBOL and matrix[1][1]==X_SYMBOL and matrix[2][0]==X_SYMBOL):
        return "первый"
    if (matrix[0][0]==O_SYMBOL and matrix[0][1]==O_SYMBOL and matrix[0][2]==O_SYMBOL or matrix[0][0]==O_SYMBOL and matrix[1][0]==O_SYMBOL and matrix[2][0]==O_SYMBOL or matrix[1][0]==O_SYMBOL and matrix[1][1]==O_SYMBOL and matrix[1][2]==O_SYMBOL or matrix[2][0]==O_SYMBOL and matrix[2][1]==O_SYMBOL and matrix[2][2]==O_SYMBOL or matrix[0][1]==O_SYMBOL and matrix[1][1]==O_SYMBOL and matrix[2][1]==O_SYMBOL or matrix[0][2]==O_SYMBOL and matrix[1][2]==O_SYMBOL and matrix[2][2]==O_SYMBOL or matrix[0][0]==O_SYMBOL and matrix[1][1]==O_SYMBOL and matrix[2][2]==O_SYMBOL or matrix[0][2]==O_SYMBOL and matrix[1][1]==O_SYMBOL and matrix[2][0]==O_SYMBOL):
        return "второй"
    return "никто"

def Fill_matrix():
    counter = 0
    isFirstUserStep=True
    while (Get_Winner() != "первый" and Get_Winner() != "второй"):
        user = 'первого' if isFirstUserStep else 'второго'
        symbol = X_SYMBOL if isFirstUserStep else O_SYMBOL
        x1,y1 =input(f"Ход {user} игрока, введите координаты через пробел:").split(" ")
        if  (x1.isdigit() and y1.isdigit() 
            and 0 <= int(x1) <= MATRIX_SIZE 
            and 0 <= int(y1) <= MATRIX_SIZE 
            and matrix[int(x1)][int(y1)] == EMPTY):
            matrix[int(x1)][int(y1)] = symbol
            isFirstUserStep = not isFirstUserStep
            Print_matrix()
            counter += 1
        else:
            print("Введите другую координату")
    if counter == 9:
        print("Ничья")
    elif Get_Winner() == "первый":
         print("Победил первый игрок")
    elif Get_Winner() == "второй":
        print("Победил второй игрок")

def Play_game():
    Create_matrix()
    Fill_matrix()

Play_game()
