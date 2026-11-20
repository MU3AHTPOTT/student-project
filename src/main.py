### Учебная программа разработана в соответствие с курсом ###
ADULT_TICKET_PRICE = 2000
CHILDREN_TICKET_PRICE = 1000
FOUR_TO_SIX_PEOPLE_DISCOUNT = 5
SEVEN_AND_MORE_PEOPLE_DISCOUNT = 10


def tickets_amount(adults, children):
    people = adults + children
    if people < 4:
        return ADULT_TICKET_PRICE * adults + CHILDREN_TICKET_PRICE * children
    elif people >= 4 and people <= 6:
        return ADULT_TICKET_PRICE * adults + CHILDREN_TICKET_PRICE * children

def output():
    print("=" * 40)
    print(f"{"ЧЕК":^40}")
    print("=" * 40)
    return 

def input():
    while adults < 1 and adults > 5:
        adults = int(input("Введите число взрослых: "))
    while children < 0:
        children = int(input("Введите число детей: "))
    return
    


while True:
    input()
    tickets_amount()
    output()
    
    # Условие зацикливания 

