def aver_num():
    list = []
    sum = 0
    answer = 0
    for i in range(2):
        ans = int(input("Добав значення - "))
        list.append(ans)
    while True:
        ask = input("Хочеш додати значення? - ")
        if ask.lower() == "т" or ask.lower() == "так":
            ans = int(input("Добав значення - "))
            list.append(ans)
        elif ask.lower() == "н" or ask.lower() == "ні":
            break
        else:
            print("Некоректна відповідь")
    for i in list:
        sum += i
    answer = sum / len(list) + 1
    print("Середнє арифметичне - ", answer)

aver_num()