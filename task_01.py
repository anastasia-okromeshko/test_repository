# Создать три класса, описывающие реальные объекты.
# Кажды класс должен содержать минимум три
# приватных атрибута, конструктор, геттеры и сеттеры
# для каждого атрибута, два метода.


class Animal():
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    def play(self: str)-> str:
        """ Text output 'play'
        """
        print('Play!')

    def eat(salf: str)-> str:
        """ Text output 'Yum, yum'
        """
        print('Yum, yum')



class Music():
    def __init__(self, singer, style, volume):
        self.__singer = singer
        self.__style = style
        self.__volume = volume

    @property
    def singer(self):
        return self.__singer

    @singer.setter
    def singer(self, new_singer):
        self.__singer = new_singer

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, new_style):
        self.__style = new_style

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    def play(self: str)-> str:
        """ Text output 'play'
        """
        print('Play!')

    def off(salf: str)-> str:
        """ Text output 'Off'
        """
        print('Off')



class Shop():
    def __init__(self, product, weight, price):
        self.__product = product
        self.__weight = weight
        self.__price = price

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, new_product):
        self.__product = new_product

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    def check(self: float)-> str:
        """ Displays the text how much money did you spend
        """
        if self.__price > 50:
            print('You spent a lot of money today')
        else:
            print('Have a nice shopping')

    def welcome(salf: str)-> str:
        """ Text output 'Welcome to the shop'
        """
        print('Welcome to the shop')


def main():
    cat = Animal('Barsik', 2, 'black')
    cat.name = 'Mua'
    cat.play()
    print(cat.name)

    track = Music('AC/DC','rock', 10)
    print(track.singer ,track.style, track.volume)

    purchase = Shop('Cheese', 300, 5)
    purchase.price = 60
    purchase.check()

if __name__=='__main__':
    main()
