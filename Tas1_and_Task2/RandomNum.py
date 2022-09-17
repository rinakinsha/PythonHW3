from random import randint

def newlist():               # создаем список случайной длины со случайными целыми числами. Используем функцию, чтобы использовать ее же в следующих заданиях и не копировать
    listnum = []
    for i in range(randint(5, 11)): 
        listnum.append(randint(0, 20))
    return listnum