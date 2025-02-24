
from task_1 import Book, Moneybox, Vector

if __name__ == "__main__":

    book = Book("Harry Potter", 1000, 6.4)
    moneybox = Moneybox(500, 0)
    vector = Vector(2.5, 6)


    try:
     vector.mult_by_num("a")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     moneybox.add_money_to_moneybox("200")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
     book.change_rating("8.9")
    except TypeError:
        print('Ошибка: неправильные данные')
