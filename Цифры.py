def num_to_words(num):
    if num < 0 or num > 100000:
        print("Число должно быть от 1 до 100000")
    else:
        num_words = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять",
                     "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
                     "семнадцать", "восемнадцать", "девятнадцать"]
        tens_words = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
                      "девяносто"]
        hundreds_words = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",
                          "девятьсот"]
        thousands_words = ["тысяч"]
        rubles_words = ["рубл"]

        # определяем разряды числа
        units = num % 10  # единицы
        tens = (num // 10) % 10  # десятки
        hundreds = (num // 100) % 10  # сотни
        thousands = num // 1000  # тысячи
        thousands1 = num // 10000%10
        # определяем порядок числа
        order = ""
        if thousands > 0:
            order = "тысяч"
            if thousands == 1:
                order = "тысяч"
            elif thousands >= 2 and thousands <= 4:
                order = "тысяч"
        elif num == 0:
            order = "рублей"

        # определяем окончание для рублей
        rubles_end = ""
        if units == 1 and tens != 1:
            rubles_end = "ь"
        elif units >= 2 and units <= 4 and tens != 1:
            rubles_end = "я"
        else:
            rubles_end = "ей"

        # определяем окончание для тысяч
        thousands_end = ""
        if thousands == 1 :
            thousands_end = "а"
        elif thousands >= 2 and thousands <= 4:
            thousands_end = "и"

        # формируем словесное представление числа
        num_in_words = ""
        if num == 0:
            num_in_words = "Ошибка! Число должно быть от 1 до 100000."
        else:
            if thousands == 1 :
                num_in_words += "одна тысяч" + thousands_end + " "  
            if thousands > 1 :
                if thousands < 20 :
                    num_in_words += num_words[thousands] + " " + order + thousands_end + " "
                else:
                    num_in_words += tens_words[num//10000-2] + " " + num_words[num//1000%10] + " " + order + thousands_end + " "
            if hundreds > 0:
                num_in_words += hundreds_words[hundreds - 1] + " "
            if tens > 1:
                num_in_words += tens_words[tens - 2] + " "
            if tens == 1:
                num_in_words += num_words[num % 100] + " "
            elif units > 0:
                num_in_words += num_words[units] + " "
            num_in_words += rubles_words[0] + rubles_end

        # выводим результат
        print(num_in_words)
try:
    num = int(input("Введите число от 1 до 100000: "))
    num_to_words(num)
except ValueError:   
        print("Ошибка! Введите число от 1 до 100000.")   