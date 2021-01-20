# Создать универсальный декоратор , который меняет порядок аргументов в функции
# на противоположный
def dekorator(func: str) -> str:
    """ Decorator that reverses the order of arguments in a function
    """
    
    def wrapper(*args):
        list = []
        for a in args:
            list.append(a)
        list.reverse()
        print (list)
    return wrapper

@dekorator
def start(*args):
    print(agrs)

start('Anastasia','Artur')
