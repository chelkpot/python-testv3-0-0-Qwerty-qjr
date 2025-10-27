# tasks/task5.py

def solve():
# Ниже пишите решение задачи

    n = int(input())
    min1 = n // 60
    hour = min1 // 60
    min = min1 % 60
    sec = n % 60
    print (hour % 24, min, sec)
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()