def func():
    num = int(input("Введіть число: "))
    if num == 1:
        print("Число ні просте ні складене")
    if num == 2 or num == 3 or num == 5 or num == 7:
        print("Число просте")
    elif num%2 == 0 or num%3 == 0 or num%4 == 0 or num%5 == 0 or num%6 == 0 or num%7 == 0 or num%8 == 0 or num%9 == 0:
        print("Число складене")
    else:
        print("Число просте")
func()