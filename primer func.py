# пример сортировки
def sort2(a, b):
    if a > b:
        return a, b
    return b, a


maxi, mini = sort2(input(), input())
print(maxi, mini)

# функция проверки четности
def isEven(n):
    return n % 2 == 0

n = int(input())
if isEven(n):
    print('Even')
else:
    print('Odd')
