# tasks/task2.py

def solve():
# Ниже пишите решение задачи

     n = int(input("Введите трёхзначное число: "))
     hours = n // 60 % 24
     min = n % 60
     print(hours, min)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()