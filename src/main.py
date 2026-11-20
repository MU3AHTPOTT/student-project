"""
Программа для расчета стоимости билетов с учетом количества посетителей
и предоставления групповых скидок.
Автор: Баскаков Алексей, СИБ-23-13
"""

ADULT_TICKET_PRICE = 2000
CHILDREN_TICKET_PRICE = 1000
FOUR_TO_SIX_PEOPLE_DISCOUNT = 5
SEVEN_AND_MORE_PEOPLE_DISCOUNT = 10

# Вывод таблицы стоимости билетов для двух взрослых и от одного до пяти детей
def table_output():
    print("")
    print("=" * 55)
    print(f"{"Взрослые":<12}{"Дети":<10}{"Всего билетов":<18}{"Итого":>15}")
    print("=" * 55)
    for children in range(1, 6):
        adults = 2
        people = adults + children
        price = ADULT_TICKET_PRICE * adults + CHILDREN_TICKET_PRICE * children
        if people < 4:
            discount = 0
        elif people <= 6:
            discount = FOUR_TO_SIX_PEOPLE_DISCOUNT
        else:
            discount = SEVEN_AND_MORE_PEOPLE_DISCOUNT
        total = price * (1 - discount / 100)
        print(f"{adults:<12}{children:<10}{people:<18}{total:>15.2f}")
    print("=" * 55)
    print("")

# Ввод с клавиатуры количества взрослых и детей и возврат их количества
def amount_people_input():
    adults = 0
    children = -1
    while adults < 1 or adults > 5:
        adults = input("Введите число взрослых: ").strip()
        adults = int(adults)
        if adults < 1 or adults > 5:
            print("Введите число в диапазоне от 1 до 5")
    while children < 0:
        children = input("Введите число детей: ").strip()
        children = int(children)
        if children < 0:
            print("Введите положительное число")
    print("")
    return adults, children

# Рассчет стоимости билетов, скидки и вывод чека
def output(adults, children):
    people = adults + children
    price = ADULT_TICKET_PRICE * adults + CHILDREN_TICKET_PRICE * children
    if people < 4:
        discount = 0
    elif people <= 6:
        discount = FOUR_TO_SIX_PEOPLE_DISCOUNT
    else:
        discount = SEVEN_AND_MORE_PEOPLE_DISCOUNT  
    total = price * (1 - discount / 100)
    print("=" * 40)
    print(f"{'ЧЕК':^40}")
    print("=" * 40)
    print(f"{"Взрослые:":<22}{adults:>18}")
    print(f"{"Дети:":<22}{children:>18}")
    print(f"{"Общее число билетов:":<22}{people:>18}")
    print(f"{"Исходная стоимость:":<22}{price:>15.2f} тг")
    print(f"{"Скидка:":<22}{discount:>17.1f}%")
    print(f"{"Сумма скидки:":<22}{price - total:>15.2f} тг")
    print(f"{"Итого:":<22}{total:>15.2f} тг")
    print("=" * 40)
    print("")

# Запрос повторного расчета заказа и возврат решения пользователя
def cycle_input():
    while True:
        cycle = input("Рассчитать другой заказ? (да/нет): ").strip().lower()
        if cycle == "да":
            return True
        elif cycle == "нет":
            return False
        else:
            print("Введите да или нет")

while True:
    table_output()
    adults, children = amount_people_input()
    output(adults, children)
    if cycle_input() == False:
        print("Работа программы завершена")
        break